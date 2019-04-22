# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:33:11 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig


class submod:

    nse = Nse()


    def domethod():
        print("ran in sub mode" + submod.nse.get_quote_url)

    def domore():
        submod.domethod()

""" End -of class """
