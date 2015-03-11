#!/usr/bin/env python
# coding: utf8

import psutil
import rumps


class Status(object):
    @property
    def name(self):
        pass

    def get(self):
        pass


class Formatter(object):
    def format(self):
        pass


class StatusFormatter(Formatter):
    def format(self):
        return '{}: {:3.0f}%'.format(self.name, self.get())


class CpuStatus(Status, StatusFormatter):
    @property
    def name(self):
        return 'CPU'

    def get(self):
        return psutil.cpu_percent()


class RamStatus(Status, StatusFormatter):
    @property
    def name(self):
        return 'RAM'

    def get(self):
        return psutil.phymem_usage().percent


class StatusCycler(Status, StatusFormatter):
    def __init__(self, *args):
        self.statuus = list(args)
        self.active_index = 0

    @property
    def active(self):
        return self.statuus[self.active_index]

    def next(self):
        self.active_index = (self.active_index + 1) % len(self.statuus)

    @property
    def names(self):
        return (s.name for s in self.statuus)

    @property
    def name(self):
        return self.active.name

    def get(self):
        return self.active.get()


class FormatterComposer(Formatter):
    def __init__(self, *args, **kwargs):
        self.separator = kwargs.get('separator', ' | ')
        self.formatters = list(args)

    def format(self):
        return self.separator.join(f.format() for f in self.formatters)


def set_title(app, title):
        app.title = title

if __name__ == '__main__':
    #s = StatusCycler(RamStatus(), CpuStatus())
    s = FormatterComposer(CpuStatus(), RamStatus(), separator=', ')
    app = rumps.App(u"µStatus", title=s.format())
    #rumps.Timer(lambda _: s.next(), 10).start()
    rumps.Timer(lambda _: set_title(app, s.format()), 1).start()
    app.run()
