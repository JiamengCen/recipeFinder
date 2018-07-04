
'''
This class is for comparsion with the items in fridge and recipe.
   @version         1.0 03 July 2018
   @author          Jiameng Cen '''
class Compare(object):

    def __init__(self, preprocessFridge, recipe):
        self.fridge = preprocessFridge
        self.recipe = recipe

    def matchRecipe(self):
        loadDict = self.recipe.getLoadDict()
        ItemLists = []
        for each in loadDict:
            itemList = []
            for eachItem in self.recipe.getAllItem(each):
                if eachItem in self.fridge.getTransDict().keys():
                    itemList.append(eachItem)
                else:
                    return False
                    print('the recipe',each['name'], 'can not support')
            ItemLists.append(itemList)
        print('FridgeItemMatchRecipe', ItemLists)
        return ItemLists

    def getMatchRecipe(self):
        return self.matchRecipe()
