import csv
import numpy as np
import timeit as ti

# Uncomment the file you want to use
#filename = "user_artist_data_50,000.csv"
filename = "user_artist_data_1million.csv"
# filename = "user_artist_data_test.csv"
# filename = "user_artist_data_minitest.csv"

# initialization
previous_listener = 0
listenrs = []
artists = []
artistsdup = []

# Creating artists and listners vectors
starttime = ti.default_timer()
print("Extracting listeners and Artists vectors ...")
with open(filename, newline='') as csvfile:
    ua_interaction = csv.reader(csvfile, delimiter=',')
    for row in ua_interaction:
        listner = int(row[0])
        artist = int(row[1])
        times = int(row[2])
        artistsdup.append(artist)
        if previous_listener != listner:
            listenrs.append(listner)
            previous_listener = listner
csvfile.close()
artists = list(set(artistsdup))
elapsed = ti.default_timer() - starttime
print("Time for Creating Artists and Listeners Vectors - Optimized: ", elapsed)

# Create numpy array for the interaction matrix
lisart = np.zeros((len(listenrs), len(artists)), dtype=int)


# Creating look-up arrays
listnerindex = range(len(listenrs))
listnerdict = dict(zip(listenrs, listnerindex))
artistindex = range(len(artists))
artistdict =  dict(zip(artists, artistindex))

# Building the interaction matrix
starttime = ti.default_timer()
print("Building Listeners-Artists Interaction Matrix ...")
with open(filename, newline='') as csvfile:
    ua_interaction = csv.reader(csvfile, delimiter=',')
    for row in ua_interaction:
        listner = int(row[0])
        artist = int(row[1])
        times = int(row[2])
        lisart[listnerdict[listner], artistdict[artist]] = times
csvfile.close()
elapsed = ti.default_timer() - starttime
print("Time for Building Interaction Matrix - Optimized: ", elapsed)

# Error checking
checksum = np.sum(lisart)

# Printing results
print("Checksum:", checksum)
print("Listeners: ", len(listenrs))
print("Artists: ", len(artists))

