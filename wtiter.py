import csv 
import os
import sys 

def clearCsv():
	csv = open(filename, "w+") 
	csv.close()

filename = "data.csv"
clearCsv()
csv = open(filename, "w") 
csv.write("hola, adios, camion, 2 \n")
csv.write("test, test2, camion, 3 \n")
csv.close()