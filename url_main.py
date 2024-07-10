# importing required libraries and frameworks
import csv

# path to file1 on local storage
filepath1 = "/Users/arhan.sheth/Documents/Codes/DX/Projects/unique_URLs/merge-csv.com__668e26acef672.csv"

# reading file1 and storing all personal linkedin urls in a seperate list
with open(filepath1, mode = 'r', encoding='Windows-1252') as file1:
    merged1 = csv.reader(file1)
    list1 = list(merged1)
    url_list1 = []
    for i in range (4, len(list1)):
        url_list1.append(list1[i][6])

# repeating above steps with file2
filepath2 = "/Users/arhan.sheth/Documents/Codes/DX/Projects/unique_URLs/merge-csv.com__668e26c2a5f36.csv"
with open(filepath2, mode = 'r', encoding = 'utf-8') as file2:
    merged2 = csv.reader(file2)
    list2 = list(merged2)
    url_list2 = []
    for i in range (4, len(list2)):
        url_list2.append(list2[i][3])