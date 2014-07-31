from pandas import DataFrame, read_csv

data = read_csv('data/schools/J390307_2030_GeoPolicy_LSOA.csv', usecols=[0,2])

data.to_csv('data/schools.csv', index=False)
