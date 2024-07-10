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
    file1.close()

# repeating above steps with file2
filepath2 = "/Users/arhan.sheth/Documents/Codes/DX/Projects/unique_URLs/merge-csv.com__668e26c2a5f36.csv"
with open(filepath2, mode = 'r', encoding = 'utf-8') as file2:
    merged2 = csv.reader(file2)
    list2 = list(merged2)
    url_list2 = []
    for i in range (4, len(list2)):
        url_list2.append(list2[i][3])
    file2.close()

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
    file3.close()

# processing unique urls from master file comapred with final_list
master_list = []
for x in url_list3:
    if x not in final_list:
        master_list.append(x)

print("Number of Unique Records in master file:", len(master_list))

# initialize csv_list as list of all unique records
csv_list = []

# import all unique records into csv_list from master file

for x in range(1, len(list3)):
    if (list3[x][24] in master_list):
             csv_list.append(list3[x])

columns = list3[0]

with open("/Users/arhan.sheth/Documents/Codes/DX/Projects/unique_URLs/masterFile.csv", mode = 'w') as master:
    master_writer = csv.writer(master)
    master_writer.writerow(columns)
    master_writer.writerows(csv_list)
    master.close()
