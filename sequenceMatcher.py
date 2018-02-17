### Lack of a logical data model for certain databases. ###
### There is a data dictionary however the physical database has not always had the same naming convention applied ###
### The data dictionary contains a logical name for the physically implemented name ###
### As there is no naming convention the logical and physical names do not always align i.e 'WMV_ACC_NME' - 'Account Name'###
### Script will match the physical name given to the field against the logical name in the data dictionary ###


import csv
from difflib import SequenceMatcher
import numpy as np

with open('test_csv.csv', newline='') as csvfile: #opens the csv file

    tosee = csv.reader(csvfile)
    for row in tosee: # iterates over each row from the csv
        print(row)

        logNme = row.pop(-1) # pops the last result in the list out and assigns it to a variable
        # print(logNme)
        physNme = row.pop(-1) # pops the last result in the list out and assigns it to a variable
        # print(physNme)

        splPhysNme =physNme.split("_") # splits out the words from the string using '_' as the delimiter
        # print(splPhysNme)

        splLogNme =logNme.split(" ")  # splits out the words from the string using ' ' as the delimiter
        # print(splLogNme)

        for word in splLogNme: # splits out the logical words in the list and assigns to the variable newWord
            newWord = word
            # print(newWord)

            alst = [] # creates a list that will be used to hold the scores from the matcher

            for i in splPhysNme: # iterates over each word
                def similar(a, b): # uses the imported package to compare the phys name against the logical string
                    return SequenceMatcher(None, a, b).ratio()
                # we are only picking up the last logical word for comparison. Would require to pick up both.
                comp = similar(i.upper(), newWord.upper())
                # print('\n'.join(list(similar)))
                # print("compared '{}' with '{}', match confidence: {}".format(i, newWord, a))
                print("compared '{}' with '{}'".format(i, newWord))
                # conc = comp + i + newWord
                alst.append(comp) # appends the matched scores in to the list

            # def softmax(alst):
            #     return np.exp(alst) / np.sum(np.exp(alst), axis=0) # Compute softmax values for each sets of scores in the list.
            # print(softmax(alst))

            print(alst)

        # print(alst)
        print()
        print('*' * 40)
        print()
