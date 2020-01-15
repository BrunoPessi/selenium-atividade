from script_pt2 import *
import csv
import json
import pandas as pd
import sys
import getopt
import pprint
from pymongo import MongoClient

# Convertendo o CSV para JSON
csvfile = open('/Users/brunopessi/Desktop/Consumo_cerveja.csv', 'r')
reader = csv.DictReader(csvfile)
client = MongoClient("mongodb://Pessi:cerjeva@aulaaberta-shard-00-00-tzrpi.mongodb.net:27017,"
                     "aulaaberta-shard-00-01-tzrpi.mongodb.net:27017,"
                     "aulaaberta-shard-00-02-tzrpi.mongodb.net:27017/test?ssl=true&replicaSet=AulaAberta-shard-0"
                     "&authSource=admin&retryWrites=true&w=majority")
db = client['cerveja']
db.segment.drop()
header = ['Data', 'Temperatura Media (C)', 'Temperatura Minima (C)', 'Temperatura Maxima (C)', 'Precipitacao (mm)',
          'Final de Semana', 'Consumo de cerveja (litros)']

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]
    print(db.segment.insert(row))
