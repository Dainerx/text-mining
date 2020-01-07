import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.tokenize import RegexpTokenizer
import os
import io

nltk.download('punkt')
def countWords(file_path):
    f = io.open(file_path, mode="r", encoding="utf-8")
    content = f.read()
    tokens = []
    if file_path == "data/1130142475.txt":
        tokens = word_tokenize(content, language='french')
        print(tokens) 
    return len(tokens)
def countSentences(file_path):
    f = io.open(file_path, mode="r", encoding="utf-8")
    content = f.read()
    tokens = sent_tokenize(content, language='french')
    return len(tokens)

directory = "data/"

totalWordCount = 0
totalSentenceCount = 0
for file in os.listdir(directory):
     filename = directory + file
     cw = countWords(filename)
     sw = countSentences(filename)
     #print(file," - words count: ", cw, " - sentences count: ", sw)
     totalWordCount+=cw
     totalSentenceCount+=sw
     
print("Total word:",totalWordCount)
print("Total sentence:",totalSentenceCount)
