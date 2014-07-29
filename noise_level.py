from pandas import DataFrame, read_csv

data = read_csv('data/noise/r2_strategic_noise_mapping.csv', usecols=[0,32,33])
#BB_data = []
#for row in data:
#	BB_data.append(data)

#print(BB_data)

data.to_csv('data/noise.csv', index=False, mode='a')