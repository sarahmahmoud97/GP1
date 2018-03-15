from collections import *
import re
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
# -- classifiers -- #
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier, LogisticRegressionCV
from sklearn.svm import LinearSVC, NuSVC
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
import nltk.classify.util
import pyarabic.araby as araby
import pyarabic.named as named
#import spacy
#import byarabic.arabrepr as arabrepr
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import warnings
from nltk.tokenize.moses import MosesTokenizer, MosesDetokenizer
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim, logging
from nltk.stem import *
from gensim import corpora
from nltk.corpus import stopwords
import codecs
import spacy
from nltk.stem.porter import *
from nltk.stem.isri import ISRIStemmer
from nltk.stem.snowball import SnowballStemmer
from itertools import groupby
from gensim.models import KeyedVectors
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
aghradSh3rya = [u'المدح',u'الذم',u'الرثاء',u'الهجاء',u'الفخر',u'الوصف',u'الحكمة',u'الغزل']
#sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
#model = gensim.models.Word2Vec(sentences, min_count=1)
t, d = MosesTokenizer(), MosesDetokenizer()
poetryFile = codecs.open("C:\Program Files\Python36\Lib\poetryRead.txt",encoding="utf8")
f = poetryFile.read().splitlines()
dataset = set(f)
sentCorpus = []
tokens = []
#f.pop(0)
for line in f:
    t1 = t.tokenize(''.join(line))
    #print(''.join(line) + '\n')
    #print(t1)
    #print(' '.join(t1))
    for word in t1:
        #print(''.join(word))
        word1 = ''.join(word)
        tokens.append(araby.strip_tashkeel(word1))
##for item in tokens:
##    print (item,repr(item))
as_list = u"['" + u"', '".join(tokens) + u"']"

#as_list.remove(''.join(''))
print('whole list of words ')
print (as_list)
print('list of distict words ')
print(list(set(as_list)))
print('****************************this is word list*****************************************')
print(' '.join(tokens)) #this is word list
counts = Counter(' '.join(tokens))
#print(counts)
#print( tokens[1] + " " + str(named.get_previous_tag(araby.strip_tashkeel(tokens[1]))))
for line in f:
    sentCorpus.append(nltk.word_tokenize(araby.strip_tashkeel(line)))
#####Stemmming
#stemmer = SnowballStemmer("english")
arabicStemmer = ISRIStemmer()
w=u'حركات'
print(arabicStemmer.stem(w))
#print(sentCorpus)#it is set of set , set of abyat al sh3r
# , 'خُلي'], ['فَإِنَّكِ', 'لِلدَمعِ', 'لَم', 'تَبذُلي'], [
model = gensim.models.Word2Vec(sentCorpus, min_count=1 , workers=4)
#print(model)
#print(model.wv.vocab)
model.save("vecCorpus")
model = gensim.models.Word2Vec.load("vecCorpus")
#print(model.wv['تبخلي'])
#model.wv.similarity('woman', 'man')
#process f to be like sentences
#workers=4 is to speed up training
#Word2vec training is an unsupervised task
#sentences gonna be a list of (list of word) as seen above
reg = re.compile('\S{4,}')
x = 0
#f = poetryFile.read().splitlines()
for line in f:
    print(''.join(line))
    print(''.join(araby.strip_tashkeel(line)))
    c = Counter(ma.group() for ma in reg.finditer(araby.strip_tashkeel(line)))
    print (c)
    x = x+1

print("Number of Abyat al Sh3r :" + str(x/2))

#we can do the following , first make an array of words (distinct words without repitition) then apply counter method to original array in order
    #to be able to to access count of each word
from collections import defaultdict
from pprint import pprint
stoplist=stopwords.words('arabic')
#print(' '.join(stoplist))
stoplist1 =  set(stoplist)
##texts = [[word for word in araby.strip_tashkeel(document1).split() if word not in stoplist1]
##         for document1 in f]

texts = []
for document1 in f:
    document2 = araby.strip_tashkeel(document1)
    #print(''.join(document))
    document = nltk.word_tokenize(document2)
    #print(document) #list 
    for word in document:
        if word in stoplist:
            index = document.index(word)
            document.pop(index)
    texts.append(document)
pprint(texts)
##for word in texts:
##    print(''.join(word)) ##done removing stop words

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
#حذف الكلمات اللي تكرارها قليل
texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

dictionary = corpora.Dictionary(texts)
dictionary.save('D:\GraduationProject1\projectITSelf\myDict.dict')
print(dictionary)
print(dictionary.token2id)

#we want to check harakit alharf al a5eer mn l beet
aa5irHarf = []#list for iesh al7arf al a5eer aw 7rkto
for line in f:
    lastChar = araby.last_char(line)
    aa5irHarf.append(lastChar)
    if(araby.is_haraka(lastChar)):
        if(lastChar == araby.DAMMA):
            print(araby.DAMMA)

        elif(lastChar == araby.FATHA):
            print(araby.FATHA)

        elif(lastChar == araby.KASRA):
            print(araby.KASRA)

        elif(lastChar == araby.DAMMATAN):
            print(araby.DAMMATAN)

        elif(lastChar == araby.FATHATAN):
            print(araby.FATHATAN)

        elif(lastChar == araby.KASRATAN):
            print(araby.KASRATAN)

        else: #sokon
            print('sokon')
    else:
        print(''.join(lastChar))
            
freqOfAa5irHarf = [(key, len(list(group))) for key, group in groupby(aa5irHarf)]
print(freqOfAa5irHarf)
import collections
counter=collections.Counter(aa5irHarf)
print(counter)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
print(counter.values())
# [4, 4, 2, 1, 2]
print(counter.keys())
# [1, 2, 3, 4, 5]
print(counter.most_common(3))
# [(1, 4), (2, 4), (3, 2)]
print(counter.most_common(1))
kkey = counter.most_common(1)
#we should write to file or save it anywhere
#and also we should generalize it to all poems for each poet


#القافية :آخر ساكن وبدور عالساكن اللي قبله مع الحرف المتحرك اللي قبل الساكن ال ما قبل الاخير
print('********** Al Qafiya ************')
for line in f:
    line1 = araby.strip_tatweel(line)
    letters, hrkat =araby.separate(line1)
    #print(letters.encode('utf8'))
    for m in hrkat:
        #لازم نعمل تعديلات
        if not araby.is_tatweel(m):
            print(araby.name(m))
            print (''.join(m))

#Most Common Words بنعملهم بكل قصائد الشاعر

