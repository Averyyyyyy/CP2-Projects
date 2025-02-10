#Avery bowman. reading files

#with open('notes\reading.pythings.txt', 'r') as file:
 #   content = file.read()
  #  index = content.find ("write")
   # end = index+5
    #print(content[index:end])

import csv

content = open ('notes\reading.pythings.txt', 'r').read()

with open('notes\reading.pythings.txt', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:

    print(f'username {row[0]}, favorite color {row[3]}')