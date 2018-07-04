import csv
import datetime
import logging

'''
This class is for preprocessing. such as whether the file is null or not,
whether the format of date is consistent not,whether the units is only enum 
types or not. 

   @version         1.0 03 July 2018
   @author          Jiameng Cen '''

class PreprocessFridge(object):
    def __init__(self, filePath):
        self.transDict = {}
        self.dicFridge = {}
        self.dict = []

        with open(filePath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.dicFridge[row['Item']] = [row['Amount'], row['Unit'], row['Use-By(date)']]
            print(self.dicFridge)

    def enumOfFour(self, dictionary, item):
            if(isinstance(dictionary[item][1], str)):
                unit = dictionary[item][1]
                if(unit == 'slices' or unit == 'of' or unit == 'grams' or
                    unit == 'milliliters'or unit == 'ml'):
                    self.transDict[item].append(dictionary[item][1])
                else:
                    print("This unit is not allowed")
            else:
                return False
                print('This' + item + 'Unit can not be transferred to')

    def transInt(self, dictionary, item):
        try:
            self.transDict[item].append(int(dictionary[item][0]))
        except TypeError as ex:
            print('This' + item + 'Amount can not be transferred to ')
            #logging.exception("{}: GET {} error: {}".format(LOG_PREFIX, request.url_rule, str(ex)))
            raise

    def transDate(self, dictionary, item):
        if(isinstance(dictionary[item][2], str)):
            try:
                strftime = datetime.datetime.strptime(dictionary[item][2], "%Y-%m-%d")
                self.transDict[item].append(strftime)
                return strftime
            except TypeError as ex:
                print('This' + item + 'Amount can not be transferred to ')
                # logging.exception("{}: GET {} error: {}".format(LOG_PREFIX, request.url_rule, str(ex)))
                raise
        else:
            return False
            print('This' + item + 'Date can not be transferred to')

    def getTransDict(self):
        return self.transDict

    def getTransDate(self,dictionary, item):
        return self.transDate(dictionary, item)
