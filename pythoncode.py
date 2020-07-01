import csv
filename="hakathon sheet.csv"
# initializing the titles and rows list 

rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row)
print(rows) 
count=0
x=input("enter the specialist")
for i in range(1,50):
    if(rows[i][1]==x):
        count=count+1
print(count)
