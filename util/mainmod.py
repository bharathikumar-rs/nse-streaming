# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:33:24 2019

@author: ArchuBharathi
"""

from io import StringIO
import sys
from nsetools import Nse
import pandas as pd
import logging
from logging.config import fileConfig
from util.submod import submod


class mainmod:

    def __init__(self):
        self.nse = Nse()

    def test(self):
        print ("ran success")

def main():
    m= mainmod()
    m.test()
    submod.domore()

if __name__ == "__main__":
    main()

""" End -of class """
