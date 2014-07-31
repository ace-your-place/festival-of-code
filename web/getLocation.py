import random

latlong = [[1.7524139512, 52.4863520771], [1.7136396631, 52.4626442228], [1.5613339044, 52.7500014395], [1.3810863335, 51.2198327852]]


def getLocation(crime, education):
    randomCase = random.randint(0,3)

    return latlong[randomCase]

#print getLocation(1,3)
