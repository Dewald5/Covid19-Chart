# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import matplotlib.pyplot as plt 
from PIL import Image
import sys

found = False
Country = input("Enter a countries ISO code\n")

if len(Country) >= 4:
    print("Enter a ISO Code with the correct length")
    sys.exit()
  
new_case = []
case_count =[]
new_death = []
death_count = []
date = []
fnew_case = []
fnew_death = []
fdeath_count = []
fcase_count = []

with open('Data_WHO.csv','r')as f:
  data = csv.reader(f)
  for row in data:
        if Country.upper() == row[1]:
          
          country_name = str(row[2])   
          date.append(str(row[3]))
          new_case.append(row[4])
          case_count.append(row[5])
          new_death.append(row[6])
          death_count.append(row[7])
          found = True 
  
if found == False:
  print("Please enter a valid ISO code")
  sys.exit()     

nlist = str(date)
nlist = nlist.replace("T00:00:00.000Z","")   
#nlist = nlist.replace("2020-","")
ndate = list(nlist.split(" "))

for i in new_case:
    fnew_case.append(float(i))
for i in new_death:
    fnew_death.append(float(i))
for i in death_count:
    fdeath_count.append(float(i))
for i in case_count:
    fcase_count.append(float(i))    

plt.figure(figsize=(25, 25))       
plt.plot(ndate,fnew_case)
plt.plot(ndate,fnew_death)
plt.plot(ndate,fdeath_count)
plt.plot(ndate,fcase_count)

plt.legend(["New Cases", "New Deaths","Death Count","Case Count"], prop={"size":40})
plt.xlabel("Time (Days)", fontsize = 40)
plt.ylabel("Amount of Cases in {}".format(country_name), fontsize = 40)
plt.yticks(rotation = 0, fontsize = 20)
plt.xticks(rotation = 40, fontsize = 11)
plt.savefig("Cov-19Graph.png")


img = Image.open('Cov-19Graph.png')
img.show()
