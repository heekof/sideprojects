import pandas as pd
import config.settings as sett
import os


def process_dframe(dframe):
	sett.total += dframe.values.sum()
	sett.round += 1
	print





def get_info(path,ext, maxx=0):
	"""
	This is the Documentation you can call it by __doc__
	"""
	files = []
	infoo = []
	for fil in os.listdir(path):
		if fil.endswith(ext):
			files.append(fil)
			infoo.append(os.stat(path+fil).st_size)

	if not maxx:
		return (files,infoo)
	else:
		for  name,sizz in zip(files,infoo):
			if max(infoo) == sizz:
				return (name,sizz)
