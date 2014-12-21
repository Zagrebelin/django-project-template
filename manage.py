#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    if os.path.isfile('environment.txt'):
        envs = open('environment.txt').readlines()
        envs = (e.strip() for e in envs)
        envs = (e.split('=', 1) for e in envs)
        for name, value in envs:
            os.environ.setdefault(name, value)

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
