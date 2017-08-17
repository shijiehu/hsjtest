
#from .bayes import *
from Ch10 import kMeans
from  numpy import *


# datMat =mat( kMeans.loadDataSet('testSet.txt'))
# #print(datMat)
#
# centroids, clusterAssment =kMeans.kMeans(datMat,4)
# print('---------------------------------')
# print(centroids)
# print('---------------------------------')
# print(clusterAssment)

geoResults = kMeans.geoGrab('1 VA center','Augusta,ME')
print(geoResults)