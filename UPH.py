import os
import matplotlib.pyplot as plt
#import csv
import pandas as pd
import glob
#import numpy as np

# This will join all pdf in the file into 1 connected file
path = r'C:\Users\jlgar\Desktop\UPH_Data\CSVfiles'
allFiles = glob.glob(os.path.join(path, "*.csv", ))

#reads the pdf and makes a Dataframe
concatDF = (pd.read_csv(f) for f in allFiles)
concatDF = pd.concat(concatDF, ignore_index=True)

#Format the UPH and IPH data to floats
concatDF['UPH'] = concatDF['UPH'].map(lambda x: x.rstrip('/ hour'))
concatDF['IPH'] = concatDF['IPH'].map(lambda x: x.rstrip('/ hour'))
concatDF['UPH'] = concatDF['UPH'].astype(float)
concatDF['IPH'] = concatDF['IPH'].astype(float)

#Hardcoded the x-axis as a list of Weekending... In the future will add weekending to the end of each
#pdf as a date stamp.
WKE = ["9-24", "10-01", "10-08", "10-15"]

#Make a Dataframe based on Users and UPH
userData = concatDF[['User', 'UPH']]

#Make a dictionary, the user being the key, and UPH as values
mydict = {}
for index in range(len(userData)):
    currentid = userData.iloc[index, 0]
    currentvalue = userData.iloc[index, 1]
    mydict.setdefault(currentid, [])
    mydict[currentid].append(currentvalue)

myDF = pd.DataFrame()
#Convert the dictionary into a Dataframe with index being User
myDF = pd.DataFrame.from_dict(mydict, orient='index', columns=WKE)
print(myDF)


print("Enter a user ID from the above list to see graph\nOr enter quit to plot everybody.")
choice = input()
while choice != "quit":
    if choice not in myDF.index:
        print(myDF)
        choice = input("Wrong input enter an user from the list")
        continue
    print("Heres " + choice + " you selected.\n")
    plt.plot(WKE, myDF.loc[choice])
    plt.ylabel("Units Per Hour")
    plt.xlabel("Weekending")
    plt.legend()
    plt.show()
    print(myDF)
    choice = input("Enter a user ID from the above list to see graph\nOr enter quit to plot everybody.")
    #Will not plot users with 1 UPH entry, needs fixing

#Afer entering quit, will plot all Users. Not pretty, need to rework this.
#Not
for idx in range(len(myDF)):
    plt.plot(WKE, myDF.iloc[idx])

plt.legend()
plt.ylabel("Units Per Hour")
plt.xlabel("Weekending")

plt.show()



#print(mydict)
# data = {"x": [], "y": [], "label": []}
# for label, coord in mydict.items():
#     if len(coord) < 4:
#         for i in range(len(coord)):
#             data["x"].append(WKE[i])
#     else:
#         data["x"].append(WKE)
#     data["y"].append(coord)
#     data["label"].append(label)
#
# print(data)



