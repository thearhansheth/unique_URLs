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

#introducing final list to seperate unique urls
final_list = []

# processing unique urls from file 1
for i in url_list1:
    if i not in final_list:
        final_list.append(i)

# processing unique urls from file 2
for j in url_list2:
    if j not in final_list:
        final_list.append(j)


# repeating processing steps for csv file of followed people
master_file = "/Users/arhan.sheth/Documents/Codes/DX/Projects/unique_URLs/CMO(Followed_people).csv"
with open(master_file, mode = 'r', encoding = 'Windows-1252') as file3:
    merged3 = csv.reader(file3)
    list3 = list(merged3)
    url_list3 = []
    for i in range (1, len(list3)):
        url_list3.append(list3[i][24])

# processing unique urls from master file
for x in url_list3:
    if x not in final_list:
        final_list.append(x)

# initialize csv_list as list of all unique records
csv_list = []

# import all unique records into csv_list from all files
for i in range(4, len(list1)):
    if list1[i][6] in final_list:
        if list1[i] not in csv_list:
            csv_list.append(list1[i])

for j in range(4, len(list2)):
    if list2[j][3] in final_list:
        if list2[j] not in csv_list:
            csv_list.append(list2[j])

for x in range(1, len(list3)):
    if list3[x][24] in final_list:
        if list3[x] not in csv_list:
            csv_list.append(list3[x])

print(len(final_list))
print(len(csv_list))