import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.tokenize import RegexpTokenizer
import os
import io
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.feature_extraction.text import TfidfVectorizer  

from sklearn.cluster import KMeans
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

def matrix_token_count(texts):
    word_vectorizer = CountVectorizer(ngram_range=(3,3)) 
    matrix = word_vectorizer.fit_transform(texts)   
    return matrix

def matrix_tokenn_Tfidf(texts):
    tfidf_vectorizer = TfidfVectorizer()
    matrix = tfidf_vectorizer.fit_transform(texts)   
    return matrix

directory = "data/"

totalWordCount = 0
totalSentenceCount = 0
texts = []
documents = []
for file in os.listdir(directory):
     filename = directory + file
     texts.append(getUT8Content(filename)) #append a file text to the texts array
     documents.append(filename)
     cw = countWords(filename)
     sw = countSentences(filename)
     print(file," - words count: ", cw, " - sentences count: ", sw, "- frequency: ",mostFrequentWord(filename))
     totalWordCount+=cw
     totalSentenceCount+=sw
     
print("Total word:",totalWordCount)
print("Total sentence:",totalSentenceCount)


matrix = matrix_tokenn_Tfidf(texts)
number_of_clusters=10
km = KMeans(n_clusters=number_of_clusters)
# Normally people fit the matrix
km.fit(matrix)

import pandas as pd
results = pd.DataFrame({
    'category': km.labels_,
    'document': documents
})
print results