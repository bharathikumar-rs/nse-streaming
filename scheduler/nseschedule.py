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
from scheduler.orchestrator import orchestrator

class scheduler:

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')

    def schedule_run(self):

        self.log.info("!!!!!!!!!!!!!!!!!schedule started for every 1 hour")
        o = orchestrator()
        o.orchestrate_workflow()

def main():
    sc = scheduler()
    schedule.every(1).hour.do(sc.schedule_run())
    while True:
    	# Checks whether a scheduled task
    	# is pending to run or not
    	schedule.run_pending()
    	time.sleep(1)


if __name__ == "__main__":
    main()

""" End -of class """
