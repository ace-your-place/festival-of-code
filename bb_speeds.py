from pandas import DataFrame, read_csv

data = read_csv('data/broadband/ofcom-uk-broadband-speed-data-2013.csv', usecols=[0,2])

data.to_csv('data/bbdata.csv', index=False)
