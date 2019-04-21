# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 22:19:15 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
import schedule
import time

class scheduler:

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')

    def schedule_run(self):
        print("10 mins schedule")

def main():
    sc = scheduler()

    schedule.every(interval=10).minutes.do(schedule_run)


if __name__ == "__main__":
    main()

""" End -of class """
