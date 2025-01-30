
# importing module 
from pymongo import MongoClient 

import json





# creation of MongoClient 
client=MongoClient() 

# Connect with the portnumber and host 
client = MongoClient('mongodb+srv://simantini091:GP996qqggkZkjuN9@cluster0.oy1dcep.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0') 

# Access database 
mydatabase = client['Gender_Biased_discrimination'] 

# Access collection of the database 
mycollection=mydatabase['Table_1'] 

# dictionary to be added in the database 
record={ 
'title': 'MongoDB', 
'description': 'MongoDB is no SQL database', 
'tags': ['mongodb', 'database', 'NoSQL'], 
'viewers': 104
} 

# inserting the data in the database 
rec = mydatabase.myTable.insert_one(record) 
client.close()
