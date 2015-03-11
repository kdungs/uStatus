#!/usr/bin/env python
# coding: utf8

import psutil
import rumps


def default_format(status):
    return '{}: {:3.0f}%'.format(status.name, status.query())


class Status(object):
    def __init__(self, name, query, format=default_format):
        self._name = name
        self.query = query
        self._format = format

    @property
    def name(self):
        return self._name

    def format(self):
        return self._format(self)


class StatusCollection(Status):
    def __init__(self, *statuses):
        self.statuses = list(statuses)

    @property
    def name(self):
        pass

    def format(self):
        pass

    def update(self, index=None):
        if not index:
            for status in self.statuses:
                status.update()
        else:
            self.statuses[index].update()


class StatusComposer(StatusCollection):
    def __init__(self, *statuses, **kwargs):
        super(StatusComposer, self).__init__(*statuses)
        self.separator = kwargs.get('separator', ' | ')

    @property
    def name(self):
        return 'Composer'

    def format(self):
        return self.separator.join(status.format() for status in self.statuses)


class StatusCycler(StatusCollection):
    def __init__(self, *statuses, **kwargs):
        super(StatusCycler, self).__init__(*statuses)
        self.active = kwargs.get('active', len(self.statuses) - 1)

    @property
    def name(self):
        return 'Cycler'

    def format(self):
        return self.statuses[self.active].format()

    def update(self):
        self.update(self.active)

    def next(self):
        self.active = (self.active + 1) % len(self.statuses)


def set_title(app, title):
        app.title = title


def configure_app(*statuses, **kwargs):
    refresh = kwargs.get('refresh', 1)
    composer = kwargs.get('composer', False)
    sc = None
    if composer:
        sep = kwargs.get('separator', ' | ')
        sc = StatusComposer(*statuses, separator=sep)
    else:
        sc = StatusCycler(*statuses)
        cycle = kwargs.get('cycle', 5)
        rumps.Timer(lambda _: sc.next(), cycle).start()
    app = rumps.App(u"µStatus", title=sc.format())
    rumps.Timer(lambda _: set_title(app, sc.format()), refresh).start()
    return app


if __name__ == '__main__':
    configure_app(
        StatusComposer(
            Status('CPU', lambda: psutil.cpu_percent()),
            Status('CPU1', lambda: psutil.cpu_percent(0)),
            Status('CPU2', lambda: psutil.cpu_percent(1)),
            separator=', '
        ),
        Status('RAM', lambda: psutil.phymem_usage().percent),
        Status('Disk /', lambda: psutil.disk_usage('/').percent),
    ).run()
