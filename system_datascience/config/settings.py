# -*- coding: utf-8 -*-
# settings.py
import logging
from logging.handlers import RotatingFileHandler
# Pour indiquer que M est un répertoire module, il faut un fichier supplémentaire __init__.py qui sera lu lors de la lecture de
import config as conf



'''
TODO: You should add in the logging the file that calls the logger
'''
def init():
	global myList
	global total
	global round
	round = 0
	total = 0
	myList = []

	# Init logging for production
	log_path = conf.settings["config"]["log_dir"]+conf.settings["config"]["log_file"]
	#logging.basicConfig(filename=log_path,level=logging.DEBUG,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

	# création de l'objet logger qui va nous servir à écrire dans les logs
	global logger
	logger = logging.getLogger()
	# on met le niveau du logger à DEBUG, comme ça il écrit tout
	logger.setLevel(logging.DEBUG) #####################################################

	# création d'un formateur qui va ajouter le temps, le niveau
	# de chaque message quand on écrira un message dans le log
	formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
	# création d'un handler qui va rediriger une écriture du log vers
	# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
	file_handler = RotatingFileHandler(log_path, 'a', 1000000, 1)
	# on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
	# créé précédement et on ajoute ce handler au logger
	file_handler.setLevel(logging.DEBUG)
	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)

	# création d'un second handler qui va rediriger chaque écriture de log
	# sur la console
	steam_handler = logging.StreamHandler()
	steam_handler.setLevel(logging.DEBUG)
	logger.addHandler(steam_handler)
	logger.debug(sys.version)
	logger.debug(platform.platform())
	logger.debug("initializig the logger. Log file is in {} ".format(str(conf.settings["config"]["log_dir"]+conf.settings["config"]["log_file"])))
	print
