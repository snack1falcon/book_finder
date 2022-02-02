import csv
books = []
output_data = []
subject_list = ["Fiction", "fiction","Fantasy", "Drama", "Biography","Humor","Handbooks","science","Art","Biology","Economics", "Poetry","Philosophy","Political","English","French","drama","History","Bible","Classical","Mythology","Socialism","African"]
subject_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
class Book:
    def __init__(self, row, subject_list, subject_count):
        self.title =""
        self.year =""
        self.genre =""
        self.url =""
        self.author =""
        self.process_data(row)
        self.genres(row, subject_list, subject_count)
        
    def genres(self, row, subject_list, subject_count):
        for g in subject_list:
            if g.upper() in row[2].upper():
                index = subject_list.index(g)
                subject_count[index] +=1
                self.genre = row[2].upper()[:3]+"_"+str(subject_count[index])

    def process_data(self,row):
        
        self.title = row[3]
        self.author = row[11]
        self.url = row[8]
        self.year = row[16]
        
        
    def get_data(self): 
        return([self.genre, self.title, self.author, self.url, self.year])
    
    def get_genre(self):
        return self.genre
    
with open("books.csv", 'r', encoding='utf-8') as f:
    bookdata = csv.reader(f)
    for row in bookdata: 
        books.append(row)
        b = Book(row, subject_list, subject_count)
        books.append(b)
        print(b.get_data())
    






       