#Code that cleans the data and stores it into a json and csv file. 
# I removed all the rows and columns that I thought made little or no sense. 
# Author: Bhavesh Gupta

import json
import csv
qbfile = open('MSD.txt', 'r')
qbfile.next()
Songid={}

for aline in qbfile:
    values = aline.split('###')
    
    
    if values[3]=='nan' or values[4]=='nan' or values[9]=='nan' or values[10]=='nan' or values[11]=='nan' or values[12]=='nan' or values[13]=='nan' or values[15]=='nan' or values[16]=='nan' or values[21]=='nan' or values[23]=='nan' or int(values[23])==0 or float(values[21])==0.0 :
        continue
    
    try:
        float(values[3])        
    except ValueError:
        continue

    try:
        float(values[4])        
    except ValueError:
        continue

    try:
        float(values[9])    
    except ValueError:
        continue

    try:
        float(values[10])    
    except ValueError:
        continue
    
    try:
        float(values[19])        
    except ValueError:
        continue

    try:
        float(values[17])        
    except ValueError:
        continue
    
    values[11]=values[11].replace(",", "");

    
    Songid[values[0]]= {'artist familiarity': values[3], 'artist hotness': values[4], 'latitude': values[9], 'longitude':values[10], 'artist location': values[11] , 'artist name' : values[12] , 'album name': values[13], 'song hotness': values[15], 'Song name':values[16] , 'tempo': values[21], 'year':values[23]}
    


newlist= sorted(Songid.iteritems(), key = lambda x:x[1]['song hotness'], reverse=True)

with open('csvdata.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["song_id", "artist_familiarity","artist_hotness","latitude","longitude","artist_location","artist_name","album_name","song_hotness","Song_name","tempo","year"])

    for (a,b) in newlist:
    	writer.writerow([a,b["artist familiarity"], b["artist hotness"], b["latitude"], b["longitude"], b["artist location"] , b["artist name"] , b["album name"], b["song hotness"], b["Song name"], b["tempo"],b["year"]])


final={ x: y for (x, y) in newlist}
with open('fire.json', 'w') as outfile:
     json.dump(final, outfile)

