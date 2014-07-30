from pandas import DataFrame, read_csv
import csv, math, time
now = time.now()

of = open('data/crime_lsoas.csv', "wb")
writer = csv.writer(of, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
lines = 0

def get_closest(float(lat),float(lng): # get closest LSOA code from supplies vars
                with open("data/lsoas.csv") as lsoa_f:
                    reader_lsoa = csv.reader(lsoa_f)
                    for lsoa_line in reader_lsoa:
                        lat_diff = lat - lsoa_line[0]
                        lng_diff = lng - lsoa_line[1]
                        lat_diff = math.pow(lat_diff, 2)
                        lng_diff = math.pow(lng_diff, 2)
                        absolute_diff = math.sqrt(lat_diff + lng_diff)

with open('data/crime_data.csv', 'rb') as crimes_f:
    reader_crimes = csv.reader(crimes_f)
    for row_crimes in reader_crimes:
        lines += 1
        #print lines
        if lines != 1:
            print get_closest(row_crimes[1],row_crimes[2])


