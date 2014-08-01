from random import choice
import csv
import pandas
from collections import deque

crimes = deque(maxlen=20)
schools = deque(maxlen=20)

lastSaved_crime_high = 0
lastSaved_school_high = 0

latlongs = [
	[52.4863520771, 1.7524139512],
	[52.4820583105, 1.7403722789],
    [53.7155898244, -1.6676645531],
    [53.3694336227, -2.7122767367]
]

line = 0

def getLocation(crime = 0, education = 0):
	with open('../data/merge.csv', 'rb') as table:
		reader = csv.reader(table)
		for row in reader:
			if line != 1:
				if (row[1] >= range(crime - 2, crime, crime + 2)) and (row[3] >= range(education - 2, education, education + 2)):
					print row[1]
					print row[3]
					lastSaved_crime_high = row[1]
					lastSaved_school_high = row[3]

	print("Highest school ratings: ", lastSaved_school_high)
	print("Highest crimes: ", lastSaved_crime_high)

#getLocation(crime=5, education=10)

def getLocationRand(crime = 0, education = 0):
    random_latlong_1 = choice(latlongs)
    random_latlong_2 = choice(latlongs)
    return [random_latlong_1, random_latlong_2]