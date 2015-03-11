# µStatus
Minimal status display for OS X tray using [psutil](https://github.com/giampaolo/psutil) and [rumps](https://github.com/jaredks/rumps) in Python.

![Here's what it looks like.](https://i.imgur.com/vknJ13g.png)

_Work in progress, please don't judge._

## Installation
To install dependencies do
```bash
$ sudo pip install psutil rumps
```

The program can then be run via
```bash
$ python ustatus.py
```

A standalone app version might follow.

## Configuration
You can configure the app to your liking by modifying the call to `configure_app` at the bottom of `ustatus.py`. Since `StatusCollection`s are also `Status`es, you can even nest them, how cool is that? The default set up should already cover most use cases.
