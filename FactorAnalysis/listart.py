import csv
import numpy as np
import timeit as ti

#Uncomment the file you want to use
#filename = "user_artist_data_50,000.csv"
filename = "user_artist_data_1million.csv"
#filename = "user_artist_data_test.csv"
#filename = "user_artist_data_minitest.csv"

#initialization
previous_listener = 0
listenrs = []
artists = []

# Creating artists and listners vectors
starttime = ti.default_timer()
print("Extracting listeners and Artists vectors ...")
with open(filename, newline='') as csvfile:
    ua_interaction = csv.reader(csvfile, delimiter=',')
    for row in ua_interaction:
        listner = int(row[0])
        artist = int(row[1])
        times = int(row[2])
        if previous_listener != listner:
            listenrs.append(listner)
            previous_listener = listner
        if artist not in artists:
            artists.append(artist)
csvfile.close()
elapsed = ti.default_timer() - starttime
print("Time for Creating Artists and Listeners Vectors - Unoptimized: ", elapsed)

# Numpy arrays for the interaction matrix, listener vectors, and artists vector
lisart = np.zeros((len(listenrs), len(artists)), dtype=int)
listenrs = np.array(listenrs)
artists = np.array(sorted(artists))

# Building the interaction matrix
starttime = ti.default_timer()
print("Building Listeners-Artists Interaction Matrix ...")
with open(filename, newline='') as csvfile:
    ua_interaction = csv.reader(csvfile, delimiter=',')
    for row in ua_interaction:
        listner = int(row[0])
        artist = int(row[1])
        times = int(row[2])
        lisart[np.where(listenrs == listner), np.where(artists == artist)] = times
csvfile.close()
elapsed = ti.default_timer() - starttime
print("Time for Building Interaction Matrix - Unoptimized: ", elapsed)

# Error checking
checksum = np.sum(lisart)

# Printing results
print("Listeners: ", listenrs.size)
print("Artists: ", artists.size)

