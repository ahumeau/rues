#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pickle import Unpickler
from random import choice


DATA_FILE = 'data/paris'


def main():
    with open(DATA_FILE) as data_file:
        unpickler = Unpickler(data_file)
        streets = unpickler.load()
    print choice(streets)


if __name__ == '__main__':
    main()
