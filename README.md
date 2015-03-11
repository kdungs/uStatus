# µStatus
Minimal status display for OS X tray using psutils and rumps in Python.

![Here's what it looks like.](https://i.imgur.com/vknJ13g.png)

_Work in progress, please don't judge._

## Installation
To install dependencies do
```bash
$ sudo pip install psutils rumps
```

The program can then be run via
```bash
$ python ustatus.py
```

A standalone app version might follow.

## Options
The program can run in multiple flavours which you can choose by editing `ustatus.py`. When using a `StatusCycler` with a corresponding `rumps.Timer`, each status will be displayed individually for a fixed amount of time. The default setting is a `FormatterComposer` that shows a number of statuses next to each other. It is also possible to just show a single status.
