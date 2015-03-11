# µStatus
Minimal status display for OS X tray using [psutil](https://github.com/giampaolo/psutil) and [rumps](https://github.com/jaredks/rumps) in Python.

![Here's what it looks like.](https://i.imgur.com/vknJ13g.png)

_Work in progress, please don't judge._

## Installation
To install dependencies do
```bash
$ sudo pip install psutil rumps py2app
```
If you don't want to create a standalone version later on, you will not need `py2app`.

The program can then be run via
```bash
$ python ustatus.py
```

## Configuration
You can configure the app to your liking by modifying the call to `configure_app` at the bottom of `ustatus.py`. Since `StatusCollection`s are also `Status`es, you can even nest them, how cool is that? The default set up should already cover most use cases.


## Standalone
Using `py2app` you can easily create a standalone version of the program that runs like a normal OS X binary by calling
```bash
$ python setup.py py2app
```
