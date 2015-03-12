import psutil

from ustatus import (
    configure_app,
    Status,
    StatusComposer
)


def format_cpu_times(status):
    data = status.query()
    return '{} (User:{:3.0f}%, Idle:{:3.0f}%)'.format(status.name, data.user,
                                                      data.idle)

if __name__ == '__main__':
    configure_app(
        StatusComposer(
            Status(
                'CPU',
                lambda: psutil.cpu_percent(percpu=True),
                lambda s: ', '.join('CPU{}:{:3.0f}%'.format(i, p)
                                    for i, p in enumerate(s.query(), 1))
            ),
            Status('RAM', lambda: psutil.phymem_usage().percent),
            separator=', '
        ),
        Status(
            'CPU Times',
            lambda: psutil.cpu_times_percent(),
            format_cpu_times
        )
    ).run()
