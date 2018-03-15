from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction import *
import nltk
from sklearn.feature_extraction.text import *
import chardet
import pyarabic.araby as araby
#import byarabic.arabrepr as arabrepr
import pyarabic.number as number
import pyarabic.named as named
from pyarabic.araby import *
from pyarabic.named import *
from pyarabic.number import *
from pyarabic.unshape import *
from tashaphyne.stemming import ArabicLightStemmer
from tashaphyne.stemming import *
from collections import Counter
import codecs
'''
we should check the cases of harakat يعني اذا الحرف مش محرك افرضله حركة فرض
بحيث في معظم الحالات اذا الحرف مش محرك نفرضه ساكن الا اذا كان بعده الف بكون مفتوح واذا كان بعده واو بكون مضموم واذا كان بعده ياء بكون مكسور
'''
#tf3eelat bhoor al sh3r
bahrTaweel = [u"فعولُنْ مَفَاعيلُنْ فعولُنْ مَفَاعيلُنْ",u"فعولُنْ مَفَاعيلُنْ فعولُنْ مَفَاعيلُنْ"]
bahrWafir = [u"مُفَاعَلَتُنْ مُفَاعَلَتُنْ مُفَاعَلَتُنْ",u"مُفَاعَلَتُنْ مُفَاعَلَتُنْ مُفَاعَلَتُنْ"]
bahrKamil = [u"متفَاعِلُنْ متفَاعِلُن متفَاعِلُنْ",u"متفَاعِلُنْ متفَاعِلُن متفَاعِلُنْ"]
bahrSaree3 = [u"مُسْتَفعِلُنْ مُسْتَفعِلُنْ فاعِلُنْ",u"مُسْتَفعِلُنْ مُسْتَفعِلُنْ فاعِلُنْ"]
bahr5afeef = [u"فَاعِلاتُنْ مُسْتفْعِلُنْ فَاعِلاتُن",u"فَاعِلاتُنْ مُسْتفْعِلُنْ فَاعِلاتُن"]
bahrRajz = [u"مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ",u"مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ"]
bahrRaml = [u"فَاعِلاتُنْ فَاعِلاتُنْ فَاعِلاتُنْ",u"فَاعِلاتُنْ فَاعِلاتُنْ فَاعِلاتُنْ"]
bahrHazaj = [u"مَفَاعِيْلُنْ مَفَاعِيْلُنْ مَفَاعِيْلُنْ",u"مَفَاعِيْلُنْ مَفَاعِيْلُنْ مَفَاعِيْلُنْ"]
bahrMadeed = [u"فاعِلاتُن فاعلُن فاعِلاتُن فاعلُن",u"فاعِلاتُن فاعلُن فاعِلاتُن فاعلُن"]
bahrMonsari7 = [u"مُسْتَفْعِلُنْ مَفْعُولاتُ مُسْتَفْعِلُنْ",u"مُسْتَفْعِلُنْ مَفْعُولاتُ مُسْتَفْعِلُنْ"]
bahrBaseet = [u"مُسْتَفْعِلُن فاعِلُنْ مُسْتَفْعِلُن فاعِلُنْ",u"مُسْتَفْعِلُن فاعِلُنْ مُسْتَفْعِلُن فاعِلُنْ"]
bahrMutqarab = [u"فَعُولُنْ فَعُولُنْ فَعُولُنْ فَعُولُنْ",u"فَعُولُنْ فَعُولُنْ فَعُولُنْ فَعُولُنْ"]
bahrMuqtadab = [u"مَفْعُولاتُ مُستفْعِلُنْ مَفْعُولاتُ",u"مَفْعُولاتُ مُستفْعِلُنْ مَفْعُولاتُ"]
bahrModari3 = [u"مَفَاعِيلُنْ فاعِلاتُنْ مَفَاععِيلُنْ",u"مَفَاعِيلُنْ فاعِلاتُنْ مَفَاععِيلُنْ"]
bahrMotdarak = [u"فَاعِلُنْ فَاعِلُنْ فَاعِلُنْ فَاعِلُنْ",u"فَاعِلُنْ فَاعِلُنْ فَاعِلُنْ فَاعِلُنْ"]
bahrMojtath = [u"مسْتفْعِلُنْ فَاعِلاتُنْ فَاعِلاتُنْ",u"مسْتفْعِلُنْ فَاعِلاتُنْ فَاعِلاتُنْ"]
#taqtee3 bhoor al sh3r
taweel = "11121121112112*11121121112112"
wafir = "122121221212212*122121221212212"
kamil = "121221212212122*121221212212122"
saree3 = "12112111211*12112111211"
al5afeef = "112112111121*112112111121"
rajz = "121112111211*121112111211"
raml = "112111211121*112111211121"
hazaj = "111211121112*111211121112"
madeed = "12111211211121*12111211211121"
monsari7 = "121121111211*121121111211"
baseet = "12112111211211*12112111211211"
mutqarab = "112112112112*112112112112"
muqtadab = ""
modari3 = ""
motdarak = ""
mojtath = ""

poetryFile = codecs.open("C:\Program Files\Python36\Lib\poetryRead.txt",encoding="utf8")
#print(poetryFile.read())
'''
f = file.read().splitlines()
for sen in f:
    print(sen)
'''
wawAlef = [u"وا",u"واه",u"واهن",u"واحد",u"والى",u"واسى",u"وازى",u"وائم",u"وادي",u"وائل",u"واقع",u"وارد"]
ArListem = ArabicLightStemmer()
vectorizer = CountVectorizer()
print(vectorizer)
vec = DictVectorizer()
#hv = HashingVectorizer(n_features=10)
#hv.transform(corpus)
shatrBayt=u"أَعَينَيَّ جودا وَلا تَجمُدا"
ajozBayt=u"أَلا تَبكِيانِ لِصَخرِ النَدى"
asmaaIshara = [u'هذا',u'هذه',u'هذان',u'هؤلاء',u'هذين',u'لكن',u'ذلك',u'ذلكما',u'ذلكم']
#إذا، لماذا، هذا، كذا، إلا، ما، إذما، حاشا، خلا، عدا، كلا، لما
alfDroppedList = [u'لما',u'كلا',u'عدا',u'خلا',u'حاشا',u'إذما',u'ما',u'إلا',u'كذا',u'هذا',u'لماذا',u'اذا',u'إذا',u'الا',u'اذما']
hrfAtf = [u'و',u'ف',u'ثم',u'بل',u'أو',u'أم']
hrkat = []
letters = []
#strippedStr = strip_tashkeel(shatrBayt)
#list of words for bayt sh3r without harakat
#strippedListWords = araby.tokenize(strippedStr)
#list of words with harakat
listWords = araby.tokenize(shatrBayt)  ##['أَعَينَيَّ', 'جودا', 'وَلا', 'تَجمُدا']
#last word in shatr
lwish = listWords[-1]

for word in listWords:
    if word == u'عمرو':
        #remove lasChar 
        #listWords.replace(u'عمرو',u'عمر')
        word1 = word.replace(u'و',u'')
        index = listWords.index(word)
        listWords[index] = word1
        
    if word == u'طه':
        #replace it with طاها
        word1 = word[:1] + u'ا' + araby.last_char(word) + u'ا'
        index = listWords.index(word)
        listWords[index] = word1
        
    if araby.is_tanwin(last_char(word)):
        #replace it with harakah + نْ
        word.repalce(araby.TANWIN,u"نْ")
        
    if araby.has_shadda(word):
        #replace it with sokon + nafs alharf
        index = word.index(araby.SHADDA)
        word.replace(word[index],(u'ْ' + word[index-1]))

    if word == u'طاوس' or word == u'داود' or word == u'ناوس':
        #add و qabl last char
        word1 = word[:3] + u'و' + araby.last_char(word)
        index = listWords.index(word)
        listWords[index] = word1
        
    if word in alfDroppedList:
        #the last char (alef) will be dropped
        word1 = word.replace(u'ا',u'')
        index = listWords.index(word)
        listWords[index] = word1
        
    if word == u'اولو' or word == u'أولو' or word == u'اولات' or word == u'أولات' or word == u'اولئك' or word == u'أولئك' :
        #drop harf alwaw
        word1 = word.replace(araby.second_char(word),u'')
        index = listWords.index(word)
        listWords[index] = word1

    if word == u'أنا' or word == u'انا':
        #drop harf alef
        word1 = word.replace(araby.last_char(word),u'')
        index = listWords.index(word)
        listWords[index] = word1

    if word == u'مائة':
        #drop harf alef
        word1 = word.replace(araby.second_char(word),u'')
        index = listWords.index(word)
        listWords[index] = word1

    if (araby.waznlike(word,u'يفعلوا') or araby.waznlike(word,u'افعلوا') or araby.waznlike(word,u'فعلوا')) and (araby.last_char(word) == u'ا'):
        #drop harf alef
        word1 = word.replace(araby.last_char(word),u'')
        index = listWords.index(word)
        listWords[index] = word1
    
    if word in asmaaIshara:
        #replace the third char with ا iza kan al7arf al tani harakih w iza la bnbaddil il harf altani
        if araby.is_haraka(araby.second_char(word)):
            #replace the third char
            #word1 = araby.first_char(ss) + u'ا'+ ss[1:]
            index = listWords.index(word)
            listWords[index] = word1
        else:
            #replace second char
            word1 = araby.first_char(word) + u'ا' + word[1:]
            index = listWords.index(word)
            listWords[index] = word1
            
    #in these words we will add alef to the second last character
    if word == u'الله':
        word1 = word[:3] + u'ا' + araby.last_char(word)
        index = listWords.index(word)
        listWords[index] = word1
        
    if word == u'الرحمن':
        word1 = word[:5] + u'ا' + araby.last_char(word)
        index = listWords.index(word)
        listWords[index] = word1
    if word == u'اله':
        word1 = word[:2] + u'ا' + araby.last_char(word)
        index = listWords.index(word)
        listWords[index] = word1

    #in these words we will replace the last harakah with suitable harf waw or ya2 or alef
    if word == u'له':
        #this gonna be لهو or لها
        if araby.is_haraka(araby.last_char(word)) and araby.last_char(word) == araby.DAMMA:
            word1 = word + u'و'
            index = listWords.index(word)
            listWords[index] = word1
            
        elif araby.is_haraka(araby.last_char(word)) and araby.last_char(word) == araby.FATHA:
            word1 = word + u'ا'
            index = listWords.index(word)
            listWords[index] = word1
            
    if word == u'به':
        #this gonna be بهي or بها
        if araby.is_haraka(araby.last_char(word)) and araby.last_char(word) == araby.FATHA:
            word1 = word + u'ا'
            index = listWords.index(word)
            listWords[index] = word1

        elif araby.is_haraka(araby.last_char(word)) and araby.last_char(word) == araby.KASRA:
            word1 = word + u'ي'
            index = listWords.index(word)
            listWords[index] = word1
            
    if word == u'لكم':
        #this gonna be لكمو
        if araby.is_haraka(araby.last_char(word)) and araby.last_char(word) == araby.DAMMA:
            word1 = word + u'و'
            index = listWords.index(word)
            listWords[index] = word1
            
    if word == u'بكم':
        #this gonna be bikomoo
        if araby.is_haraka(araby.last_char(word)) and araby.last_char(word) == araby.DAMMA:
            word1 = word + u'و'
            index = listWords.index(word)
            listWords[index] = word1
            
    if word == u'اليكم':
        #this gonna be ilykmoo
        if araby.is_haraka(araby.last_char(word)) and araby.last_char(word) == araby.DAMMA:
            word1 = word + u'و'
            index = listWords.index(word)
            listWords[index] = word1
            

    if araby.last_char(lwish) == u'ُ' and (araby.secondlast_char(lwish) == u'م' or araby.secondlast_char(lwish) == u'ه'):
        #delete it and replace it with و
        word1 = lwish + u'و'
        index = listWords.index(lwish)
        listWords[index] = word1

    if araby.last_char(lwish) == u'ِ' and (araby.secondlast_char(lwish) == u'ه'):
        #delete it and replace it with ي
        word1 = lwish + u'ي'
        index = listWords.index(lwish)
        listWords[index] = word1

    if word.find(u'آ') != -1:
        #al madda found , replace it with أَاْ
        word1 = word.replace(u'آ',u'أاْ')
        listWords[listWords.index(word)] = word1
        
    ##اللام القمرية >> we should extract third character طبعا هاد في حالة فش حركات
    if araby.first_char(word) == 'ا' and araby.second_char(word) == 'ل': #regardless alharakat
        if word[2] in list(araby.SUN):
            #remove al ta3reef ال w add shadda to the first character
            word1 = word.replace(u'ال',u'')
            word2 = word1.replace(araby.first_char(word1),(araby.first_char(word1) + u'ْ' + araby.first_char(word1) + u'َ'))
            listWords[listWords.index(word)] = word2
            
        elif word[2] in list(araby.MOON):
            #remove only al alef w tabqa alllam al sakina
            word1 = word.replace(u'ا',u'')
            listWords[listWords.index(word)] = word1
    
    if word.find(u"ال") != -1 and (araby.first_char(word) == u'َل' or araby.first_char(word)) == u'لِ': 
        word1 = word.replace(u'ا',u'')
        listWords[listWords.index(word)] = word1
                                   
    #now we want to remove ك المخاطبة وهدول القصص
    if araby.first_char(word) == u'ا' and (listWords[listWords.index(word)-1] in hrfAtf):
        #remove alef
        word1 = word.replace(araby.first_char(word),u'')
        listWords[listWords.index(word)] = word1
    
    if (araby.first_char(word) == u'و' or araby.first_char(word) == u'ف') and araby.second_char(word) == u'ا':
        #bs we will notice that al alef shouldnt be an actual char in the word like واحد
        #لازم نستثني وامعتصماه وهدول
        #if word not in wawAlef:
        if named.is_proper_noun(word): #hon ma bdna yah
            pass
        else:
            if word not in wawAlef:
                word1 = word.replace(araby.second_char(word),u'')
                index = listWords.index(word)
                listWords[index] = word1
        
    # تحذف الألف والواو والياء الساكنتين من أواخر الأسماء والأفعال والحروف إذا وليها ساكن like انا الذي
    if (araby.last_char(araby.strip_tashkeel(word)) == u'ا' or araby.last_char(araby.strip_tashkeel(word)) == u'ى' or araby.last_char(araby.strip_tashkeel(word)) == u'و') and araby.first_char(listWords[listWords.index(word)+1]) == u'ْ':
        index = listWords.index(word)
        word1 = listWords[index+1]
        # halla2 here we could use araby.secondlast_char to avoid being haraka
        if (araby.secondlast_char(word) == u'ا' or araby.secondlast_char(word) == u'و' or araby.secondlast_char(word) == u'ي' or araby.secondlast_char(word) == u'ى') and araby.second_char(word1) == u'ْ':
            word1 = word.replace(araby.last_char(word),u"") #for skoon
            word2 = word1.replace(araby.secondlast_char(word1),u"") #for harf
            listWords[index] = word2
                                   

       
#shatrBayt = shatrBayt.replace(" ","")
#listCharz = list(shatrBayt) #with harakat

def qafiah(str):
    "this function is for finding al qafiyah"
    
