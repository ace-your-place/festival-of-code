from pandas import DataFrame, read_csv

data = read_csv('data/railways/RailReferences.csv', usecols=[6,7])

data.to_csv('data/railways.csv', index=False)
