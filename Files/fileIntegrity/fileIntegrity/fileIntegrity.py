import os
import hashlib
import time
#create hash
def fileHash(filePath):
    with open(filePath, "rb") as f:
        fileHash = hashlib.sha256(f.read()).hexdigest()
    return fileHash
#getting user input
userInput = ""
while (userInput!='A') and (userInput!= 'B'):
    userInput = input("What would yo like to do? \n A) Collect new baseline? \n B) Begin monitoring files with saved Baseline? \n").upper()

filePath = "C:/Users/jonat/OneDrive - University of Salford/university work/python projects/Files/testFiles/";
baselinePath = "C:/Users/jonat/OneDrive - University of Salford/university work/python projects/Files/baseline.txt"
DirectoryFiles = os.listdir(filePath)
#new baseline
if userInput == 'A':
    with open(baselinePath, "w") as f:
        f.write("")
    for file in DirectoryFiles:
        absPath = filePath + file
        with open(baselinePath, "a") as f:
            f.write(absPath + "|" + fileHash(absPath) + "\n") 
#monitor files
else:
    DictionaryOfFileHashes = {}
    baseline = open(baselinePath, 'r')
    for line in baseline:
        DictionaryOfFileHashes[line.split("|")[0]] = line.split("|")[1]
    while(True):
        time.sleep(1)
        DirectoryFiles = os.listdir(filePath)
        for file in DirectoryFiles:
            absPath = filePath + file;
            compareHash = fileHash(absPath)
            try:
                value = DictionaryOfFileHashes[absPath][:-1]
                if value != compareHash:
                    print(file + "has been changed")
            except:
                print(file + "has been created")
        if len(DirectoryFiles)<len(DictionaryOfFileHashes):
            for key in DictionaryOfFileHashes.keys():
                if(os.path.exists(key)) == False:
                   print(key + "has been deleted or moved")