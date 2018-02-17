#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:13:30 2018

@author: dannymccluskey
"""

import csv
from difflib import SequenceMatcher
import difflib
import numpy as np

with open('test_csv.csv', newline='') as csvfile: #opens the csv file

    tosee = csv.reader(csvfile)
    for row in tosee: # iterates over each row from the csv
        # print(row)

        logNme = row.pop(-1) # pops the last result in the list out and assigns it to a variable
        # print(logNme)
        physNme = row.pop(-1) # pops the last result in the list out and assigns it to a variable
        # print(physNme)

        splPhysNme =physNme.split("_") # splits out the words from the string using '_' as the delimiter
        #print(splPhysNme)

        splLogNme =logNme.split(" ")  # splits out the words from the string using ' ' as the delimiter
        #print(splLogNme)

        for i in splPhysNme: # iterates over each word
            comp = difflib.get_close_matches(i, splLogNme, 1)
            if len(comp) == 1:
                comp.append(i)
                print(comp)
                # print("{} {}".format(comp, i))

        print()
        print('*' * 40)
        print()
