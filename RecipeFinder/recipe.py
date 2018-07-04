import json

'''
This class is for dealing with getting items from structured data.
these functions aim to get ingredients or items from json.

   @version         1.0 03 July 2018
   @author          Jiameng Cen '''

class Recipe(object):

    def __init__(self, jsonFilePath):
        self.load_dict = []
        with open(jsonFilePath, "r") as load_f:
            self.load_dict = json.load(load_f)

    def getAllItem(self, dict):
        items = []
        ingredientList = dict['ingredients']
        for each in ingredientList:
            items.append(each['item'])
        return items

    def getLoadDict(self):
        return self.load_dict

    def transDictToStr(self, list, index):
        json_str = json.dump(list[index])
        print(json_str)
        new_dict = json.loads(json_str)
        print(new_dict)









