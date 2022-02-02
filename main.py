import csv 
#lets you use csv lib

data = []  #save file data - one row at a time
output_data = [] #storges data going out


subject_list = ["Fiction", "fiction","Fantasy", "Drama", "Biography","Humor","Handbooks","science","Art","Biology","Economics", "Poetry","Philosophy","Political","English","French","drama","History","Bible","Classical","Mythology","Socialism","African"]
     #use to seach for a key word. in this case it's a subject.
subject_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
with open("books.csv", 'r', encoding='utf-8') as f:
    bookdata = csv.reader(f)
    for row in bookdata: # reads line by line and adds it to the data variable
        data.append(row) 

for book in range (1,670):

    for subject in subject_list: 
        if subject in data[book][2]: 
            index = subject_list.index (subject)
            subject_count[index] +=1
            outtext = subject[:3].upper() +"_"+str(subject_count[index])
            row = [outtext, data[book][3], data[book][11],data[book][8], data[book][16]]
            print(row)
            print(index)
        
            output_data.append(row)
            break
book = 0
print(subject_count)
while book < len(output_data):
    with open('save.csv', 'a', newline='') as f:
        writer  = csv.writer(f)
        writer.writerow(output_data[book])

    book = book + 1


