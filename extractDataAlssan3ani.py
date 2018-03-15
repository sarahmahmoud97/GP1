# -*- coding: cp1256 -*-
from urllib2 import urlopen
#from bs4 import BeautifulSoup
from lxml import html
import requests
import json
import urllib2
from pprint import pprint
import os
import codecs

poetryFile = codecs.open("C:\Users\Sarah\Downloads\Alsan3aniTrain.txt",encoding="utf8")
listOfPages = poetryFile.read().splitlines()
#l7atta nt2akkad ennu ma fe tikrar sar bl 3'alat ay url b3mllo
#processing b7otto juwwa list tanyi w bser af7as iza elli 3leh eldoor majood
#bl list altanyi aw la w hakaza
i = 1
pathO= r"D:\GraduationProject1\datasets\arabicPoetries\Al Ameer Alsan3ani\train"
os.chdir(pathO)
for path in listOfPages:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')
    logPath = "poetry" + str(i) +".txt"
    with codecs.open(logPath, mode = 'w' ,encoding = 'utf-8') as f:
        f.write('Alsan3ani'+ str(i) + ':' + '\n\r')
        for shtr in shatr:
            f.write(''.join(shtr) + '\r\n')
            index = shatr.index(''.join(shtr))
            f.write(''.join(ajoz[index]) + '\r\n')
            f.write("*" + '\r\n')
            f.write("\n\r")

    print('doneTrain' + str(i))
    i = i + 1


#**************************************************************************
poetryFile = codecs.open("C:\Users\Sarah\Downloads\Alsan3aniTest.txt",encoding="utf8")
testList = poetryFile.read().splitlines()
pathO= r"D:\GraduationProject1\datasets\arabicPoetries\Al Ameer Alsan3ani\test"
os.chdir(pathO)

for path in testList:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')
    logPath = "poetry" + str(i) +".txt"
    with codecs.open(logPath, mode = 'w' ,encoding = 'utf-8') as f:
        for shtr in shatr:
            f.write(''.join(shtr) + '\r\n')
            index = shatr.index(''.join(shtr))
            f.write(''.join(ajoz[index]) + '\r\n')
            f.write("*" + '\r\n')
            f.write("\n\r")
 
    print('doneTest' + str(i))
    i = i + 1
