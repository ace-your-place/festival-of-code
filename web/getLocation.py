from random import choice
import csv
import pandas
import deque

crimes = deque(max=20)
schools = deque(max=20)

latlongs = [
	[52.4863520771, 1.7524139512],
	[52.4820583105, 1.7403722789],
    [53.7155898244, -1.6676645531],
    [53.3694336227, -2.7122767367]
]



def getLocation(crime = 0, education = 0):
	for row in table:
		

def getLocationRand(crime = 0, education = 0):
    random_latlong_1 = choice(latlongs)
    random_latlong_2 = choice(latlongs)
    return [random_latlong_1, random_latlong_2]
