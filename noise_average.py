from pandas import DataFrame, read_csv
import csv

ofile  = open('data/noise_average.csv', "wb")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
lines = 0

with open('data/noise.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        lines += 1
        #print lines
        if lines != 1:
            average = (float(row[1]) + float(row[2]))/2
            #print average
            data = [row[0], average]
            #print data
            writer.writerow(data)
