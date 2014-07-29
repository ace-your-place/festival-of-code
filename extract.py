import csv
import pandas

#with open("data/crime/2014-05-avon-and-somerset-street.csv", "r") as file:
#	file.readline()
#	print(file.readline())

Crime_Data = list()

cr = csv.reader(open("data/crime/2014-05-avon-and-somerset-street.csv","rb"))
for row in cr:    
	data = pandas.read_csv("data/crime/2014-05-avon-and-somerset-street.csv", usecols=[4,5])
	Crime_Data.append(data)

Crime_Data.append("test")

print(Crime_Data)
	


	# [
	# (a, b),
	# ]

