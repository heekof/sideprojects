#!/bin/bash python


import os
import operator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="The number of lines printed", dest="maxx", type=int)
parser.add_argument("-p", dest="path", help="path of the directory")
args = parser.parse_args()

print "\n ", args.maxx, " max size files in  ",  args.path, "\n"

path = "/home/jaafar/WP6"
path = args.path

os.chdir(path)

file_path = []
file_info = []
file_last_time_access = []
file_last_time_modif = []


print "\n Please wait ... \n"

for root, directory, filename in os.walk(path):
    if not directory:
        for myfile in filename:
            file_path.append(os.path.join(root, myfile))
            file_info.append(os.stat(os.path.join(root, myfile)).st_size)
	    file_last_time_access.append(os.stat(os.path.join(root, myfile)).st_atime)
	    file_last_time_modif.append(os.stat(os.path.join(root, myfile)).st_mtime)


#file_dict = dict(zip(file_path,file_info,file_last_time_access,file_last_time_modif)))

file_dict = {z[0]:list(z[1:]) for z in zip(file_path,file_info,file_last_time_access,file_last_time_modif)}


sorted_dict = sorted(file_dict.items(), key=operator.itemgetter(1))


max_show = args.maxx
print "file path ; size; last time accessed; last time modified"
for i in range(max_show):
    print sorted_dict[len(sorted_dict) - 1 - i][0],';',sorted_dict[len(sorted_dict) - 1 - i][1][0], ';',sorted_dict[len(sorted_dict) - 1 - i][1][1],';', sorted_dict[len(sorted_dict) - 1 - i][1][2]
    if i > max_show:
        break
