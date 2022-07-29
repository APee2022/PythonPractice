# loadData.py, writeData.txt and writeData.py are linked to each other
import pickle

file = open("writeData.txt","rb")

l=pickle.load(file)

print(l)