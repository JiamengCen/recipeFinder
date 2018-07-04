from preprocess import PreprocessFridge
from compare import Compare
from recipe import Recipe
from specialCase import SpecialCase

'''
This project is for recipe finder.At first we need to have two files:fridge.csv,
recipe.json.And then fridge.csv should be transferred the format. With the consideration
of special cases, if the content of recipe can match to the content of fridge, the item 
which is satisfied with all requirements will be the answer.

This Main Function calls different class functions from other classes.
   @version         1.0 03 July 2018
   @author          Jiameng Cen '''

if __name__ == '__main__':

    newReprocess = PreprocessFridge('/Users/jiamengcen/Desktop/fridge.csv')
    newRecipe = Recipe('/Users/jiamengcen/Desktop/recipeJson.json')
    newCompare = Compare(newReprocess, newRecipe)
    newSpecialCase = SpecialCase(newReprocess, newRecipe,newCompare)

    if (len(newReprocess.dicFridge) == 0):
        print('This dictionary is null')
    else:
        newCompare.matchRecipe()
        for key in newReprocess.dicFridge:
            newReprocess.transDict[key] = []
            newReprocess.transInt(newReprocess.dicFridge, key)
            newReprocess.enumOfFour(newReprocess.dicFridge, key)
            newReprocess.transDate(newReprocess.dicFridge, key)
            Itemsdate = newReprocess.getTransDate(newReprocess.dicFridge, key)
            newSpecialCase.useByDate(Itemsdate)
        newSpecialCase.itemOfCloseDay(newReprocess.transDict)
        newSpecialCase.moreRecipeChoice()
        newSpecialCase.noFound()
