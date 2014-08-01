from random import choice
import csv
import pandas
from collections import deque

crimes = deque(maxlen=20)
schools = deque(maxlen=20)

lsoas = deque(maxlen=20)

crime_high = 0
education_high = 0

latlongs = [
	[52.4863520771, 1.7524139512],
	[52.4820583105, 1.7403722789],
    [53.7155898244, -1.6676645531],
    [53.3694336227, -2.7122767367]
]


def getLocation(crime = 0, education = 0):
	line = 0
	with open('../data/merge.csv', 'rb') as table:
		reader = csv.reader(table)
		for row in reader:
			line += 1
			if line > 1:
				row[3] = float(row[3])
				row[2] = float(row[1])
				best_val_for_crime = crime * row[3]
				best_val_for_schools = education * row[1]
				crimes.append(best_val_for_crime)
				schools.append(best_val_for_schools)
				for i in crimes:
					best_overall = crimes[i] + schools[i]
	print best_overall

print lsoas
print crimes
print schools

getLocation(crime=5, education=4)

def getLocationRand(crime = 0, education = 0):
    random_latlong_1 = choice(latlongs)
    random_latlong_2 = choice(latlongs)
    return [random_latlong_1, random_latlong_2]