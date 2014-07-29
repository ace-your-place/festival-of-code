from pandas import DataFrame, read_csv
import conversion as cv
import csv

ofile  = open('data/railways.csv', "wb")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
lines = 0

with open('data/railways.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        lines += 1
        #print lines
        if lines != 1:
            data = cv.ENtoLL84(row[0], row[1])
        #print data
            writer.writerow(data)
