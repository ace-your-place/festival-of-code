from pandas import DataFrame, read_csv
import conversion as cv
import csv

of = open('data/lsoas.csv', "wb")
writer = csv.writer(of, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
lines = 0

with open('data/lsoas/ONSPD_FEB_2012_UK_uk_datazone_centroids.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
	print row
        lines += 1
        #print lines
        if lines > 2:
            data = [row[0], cv.ENtoLL84(row[1], row[2])[0], cv.ENtoLL84(row[1], row[2])[1]]

            writer.writerow(data)
            print data
