import csv 
import os
import sys 
import time

def clearCsv():
	csv = open(filename, "w+") 
	csv.close()


filename = "data.csv"

#clearCsv()

csv = open(filename, "wb") 
csv.write("jason py2tes, ewr, camion, 2 \n")
csv.close()

csv = open(filename, "w") 
while True:
	csv.write("asdasd")
	print("Action")
	time.sleep(0.2)

csv.close()



