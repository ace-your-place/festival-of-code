from pandas import DataFrame, read_csv

data = read_csv('data/broadband/ofcom-uk-broadband-speed-data-2013.csv', usecols=[0,2])
#BB_data = []
#for row in data:
#	BB_data.append(data)

#print(BB_data)

data.to_csv('data/bbdata.csv', index=False)