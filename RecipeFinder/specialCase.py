import datetime

'''
This class is for project notes. Considering the special cases,
whether the items is outdated or not, whether there are the items 
in the fridge or not and so on.

   @version         1.0 03 July 2018
   @author          Jiameng Cen '''

class SpecialCase:

    def __init__(self, preprocessFridge, recipe, compare):
        self.fridge = preprocessFridge
        self.recipe = recipe
        self.compare = compare
    arrayOfItemDate = []

    def useByDate(self, Itemsdate):
        itemDate = Itemsdate
        today = str(datetime.date.today())
        todayDate = datetime.datetime.strptime(today, "%Y-%m-%d")
        if itemDate <= todayDate:
            return True
        else:
            return False
            print("this item is outdated")

    def itemOfCloseDay(self, Dict):
        dateDictList  = sorted(Dict.items(), key=lambda x: x[1][2])
        return(dateDictList[0][0])

    def moreRecipeChoice(self):
        transdict = self.fridge.getTransDict()
        matchItemList = self.compare.getMatchRecipe()
        if len(matchItemList) >= 2:
            closeItem = self.itemOfCloseDay(transdict)
            loadDict = self.recipe.getLoadDict()
            for each in loadDict:
                allItems = self.recipe.getAllItem(each)
                for eachitem in allItems:
                    if closeItem == eachitem:
                        print('final name', each['name'])
                        print('final recipe', each)
                    else:
                        pass
            return each['name']
        else:
            return False

    def noFound(self):
        ItemLists = self.compare.getMatchRecipe()
        if len(ItemLists) == 0:
            print('Order Takeout')
        else:
            return True