import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.tokenize import RegexpTokenizer
import os
import io

nltk.download('punkt')

def getUT8Content(file_path):
    f = io.open(file_path, mode="r", encoding="utf-8")
    return f.read()
def mostFrequentWord(file_path):
    content = getUT8Content(file_path)
    tokens = word_tokenize(content, language='french')
    wordDist = nltk.FreqDist(w.lower() for w in tokens)
    return wordDist.most_common(10)
def countWords(file_path):
    content = getUT8Content(file_path)
    tokens = word_tokenize(content, language='french')
    return len(tokens)
def countSentences(file_path):
    content = getUT8Content(file_path)
    tokens = sent_tokenize(content, language='french')
    return len(tokens)

directory = "data/"

totalWordCount = 0
totalSentenceCount = 0
for file in os.listdir(directory):
     filename = directory + file
     cw = countWords(filename)
     sw = countSentences(filename)
     print(file," - words count: ", cw, " - sentences count: ", sw, "- frequency: ",mostFrequentWord(filename))
     totalWordCount+=cw
     totalSentenceCount+=sw
     
print("Total word:",totalWordCount)
print("Total sentence:",totalSentenceCount)
