
import numpy as np
import pandas as pd
import config.config as conf
import config.settings as sett
import os
import lib.util as U
import sys
import matplotlib.pyplot as plt


print "Hello word"
print
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print


#dframe = pd.read_csv(path)
direc =  conf.settings["config"]["path"]
ext = conf.settings["config"]["ext"]
limit = conf.settings["config"]["limit"]

maxx = 1

if not maxx:
    x,y =  U.get_info(direc,ext,maxx)
    for a, b in zip(x,y):
        print a, b/1000000
else:
    print "Max selected as the tuple : {} ".format(U.get_info(direc,ext,maxx))
    global_path = direc + U.get_info(direc,ext,maxx)[0]
    print "Global path is {} ".format(global_path)


dframe = pd.read_csv(global_path,delimiter=';', index_col=0, parse_dates=True, infer_datetime_format=True,nrows=limit)
# fill NaN use "backfill" NEXT valid observation to fill gap
dframe.fillna(method="bfill",inplace=True,axis=0)
dframe.fillna(value=0,inplace=True)

X = dframe.values
print X.shape
file_name = "X.npy"

cwd = os.getcwd()
print os.listdir(os.getcwd())

if file_name in os.listdir(cwd):
    print file_name," exists"
    print "Loading ",file_name," Wait please :)"
    X = np.load(os.path.join(cwd,file_name))
else:
    print "file doesn't exist"
    print "saving file in ", file_name
    np.save("X.npy",X)
    print "exiting the program, bye"
    sys.exit()

print "Continue"

print X.shape

print U.get_info.__doc__

#plt.show()
