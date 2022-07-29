# loadData.py, writeData.txt and writeData.py are linked to each other
import pickle

l=[10,20,30,40]

file = open("writeData.txt","wb")

pickle.dump(l,file)

file.close()