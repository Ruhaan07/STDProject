import math
import csv

with open ('StanderdDeviatinProjectData.csv',newline = '' ) as f:
    reader = csv.reader(f)
    file_data =list(reader)

data = file_data[0]

def mean (data):
    n = len(data)
    total = 0
    for x in data :
        total = total + int(x)

    mean = total/n
    return mean

square_list = []
for n in data :
    a = int(n)-mean(data)
    a = a ** 2
    square_list.append(a)

sum = 0
for i in square_list:
    sum = sum + i

result = sum/(len(data)-1)
std = math.sqrt(result)
print(std)