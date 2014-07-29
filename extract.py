import pandas
import csv
from glob import glob

files = glob("data/crime/*.csv")

#print files

for file in files:
    data = pandas.read_csv(file, usecols=[4,5])
    data.to_csv("data/crime_data.csv", index=False, cols=['Longitude', 'Latitude'], mode='a')
