
#from .bayes import *
from Ch04 import bayes
#import ch04
listOPosts,listClasses = bayes.loadDataSet()
myVocablist = bayes.createVocabList(listOPosts)
vec = bayes.setOfWords2Vec(myVocablist,listOPosts[0])
print("----------------")
print(myVocablist)
print(vec)
