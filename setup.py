"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ["time_count.txt", "ui.py", "countdown.py", "play_sound.py", "sound/bell_chime.mp3", "sound/times_up.mp3"]
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
