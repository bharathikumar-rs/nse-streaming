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
from scheduler.orchestratorv1 import orchestrator

class nsescheduler:

    def __init__(self):
        self.nse = Nse()
        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('scheduler intiated ')

    def schedule_run(self):

        self.log.info("!!!!!!!!!!!!!!!!!schedule started for every 1 hour")
        o = orchestrator()
        o.orchestrate_workflow()

    def geeks2(self):
        print("schedule is running about to trigger trading")

def main():
    sc = nsescheduler()
    sc.schedule_run()
    #schedule.every().hour.do(sc.schedule_run())
    #schedule.every(10).seconds.do(sc.schedule_run)
    #schedule.every().hour.do(sc.schedule_run)
    print ("Continuing with next run")


    while True:
    	# Checks whether a scheduled task
    	# is pending to run or not
    	schedule.run_pending()
    	time.sleep(1)

if __name__ == "__main__":
    main()

""" End -of class """
