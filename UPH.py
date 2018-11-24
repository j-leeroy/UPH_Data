import matplotlib.pyplot as plt
import PyPDF2
from tabula import read_pdf
import numpy as np
import csv
import pandas

x = ["09-24", "10-01", "10-08", "10-15"]

b374813 = [106.3, 133.3, 127.4, 122.4]
b399617 = [132.9, 145.6, 132.3, 138.1]
b575129 = [143.1, 153.0, 153.9, 161.1]
f199327 = [184.1, 204.3, 157.0, 170.8]
g444698 = [115.4, 119.0, 135.4, 117.0]
g585396 = [115.0, None, 94.3, 143.7]
i411561 = [106.8, 102.9, 118.2, 121.5]

plt.plot(x, b374813, label="b374813")
plt.plot(x, b399617, label="b399617")
plt.plot(x, b575129, label="b575129")
plt.plot(x, f199327, label="f199327")
plt.plot(x, g444698, label="g444698")
plt.plot(x, g585396, label="g585396")
plt.plot(x, i411561, label="i411561")

plt.xlabel('Week Ending')
plt.ylabel('UPH')

plt.legend()
#plt.show()
# plt.show()

# df = read_pdf('C://Users//jlgar//Desktop//UPH_Data//FASTweb-09-17_09-24.pdf')

"""x = []
y = []

with open('C:/Users/jlgar/Desktop/UPH_Data/tabula-FASTweb-09-17_09-24.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(float(row[1]))

plt.plot(x, y)
plt.show()"""
df = pandas.read_csv('C:/Users/jlgar/Desktop/UPH_Data/tabula-FASTweb-09-17_09-24.csv')
print(df)










