from pandas import DataFrame, read_csv
import csv

ofile  = open('data/crime_quantities.csv', "wb")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
lines = 0
lsoas ={}

with open('data/crime_data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        lines += 1
        if lines != 1:
            if(lsoas.has_key(row[0]) == True):
                lsoas[row[0]] += 1
            else:
                lsoas[row[0]] = 1
#IT WORKS

for k, v in lsoas.iteritems():
    #print "%s,%s" % (k, v)
    data = (k,v)
    writer.writerow(data)

