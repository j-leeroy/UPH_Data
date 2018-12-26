import os
import matplotlib.pyplot as plt
import csv
import pandas as pd
import glob
import numpy as np
# df = pandas.read_csv('C:\\Users\\jlgar\\Desktop\\UPH_Data\\CSVFiles\\tabula-FASTweb-09-17_09-24.csv')
# print(df)
#
#
# print(df.dtypes)
# print(df.describe())
#
# df['UPH'] = df['UPH'].map(lambda x: x.rstrip('/ hour'))
# df['IPH'] = df['IPH'].map(lambda x: x.rstrip('/ hour'))
#
# df['UPH'] = df['UPH'].astype(float)
# df['IPH'] = df['IPH'].astype(float)


path = r'C:\Users\jlgar\Desktop\UPH_Data\CSVfiles'
allFiles = glob.glob(os.path.join(path, "*.csv", ))

concatDF = (pd.read_csv(f) for f in allFiles)
concatDF = pd.concat(concatDF, ignore_index=True)

concatDF['UPH'] = concatDF['UPH'].map(lambda x: x.rstrip('/ hour'))
concatDF['IPH'] = concatDF['IPH'].map(lambda x: x.rstrip('/ hour'))
concatDF['UPH'] = concatDF['UPH'].astype(float)
concatDF['IPH'] = concatDF['IPH'].astype(float)
WKE = ["9-24", "10-01", "10-08", "10-15"]

userData = concatDF[['User', 'UPH']]

mydict = {}
for index in range(len(userData)):
    currentid = userData.iloc[index, 0]
    currentvalue = userData.iloc[index, 1]
    mydict.setdefault(currentid, [])
    mydict[currentid].append(currentvalue)

myDF = pd.DataFrame()
myDF = pd.DataFrame.from_dict(mydict, orient='index', columns=WKE)
print(myDF)


print("Enter a user ID from the above list to see graph\nOr enter quit to plot everybody.")
choice = input()
while(choice != "quit"):
    print("Heres " + choice + " you selected.\n")
    plt.plot(WKE, myDF.loc[choice])
    plt.ylabel("Units Per Hour")
    plt.xlabel("Weekending")
    plt.legend()
    plt.show()
    print(myDF)
    choice = input("Enter a user ID from the above list to see graph\nOr enter quit to plot everybody.")

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



