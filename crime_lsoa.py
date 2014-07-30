from pandas import DataFrame, read_csv
import csv

of = open('data/crime_lsoas.csv', "wb")
writer = csv.writer(of, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
lines = 0

with open('data/crime_data.csv', 'rb') as crimes_f:
    reader_crimes = csv.reader(crimes_f)
    for row_crimes in reader_crimes:
        lines += 1
        #print lines
        if lines != 1:
            with open("data/lsoas.csv") as lsoa_f:
                reader_lsoa = csv.reader(lsoa_f)
                for lsoa_line in reader_lsoa:
                    print lsoa_line
