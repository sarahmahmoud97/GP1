from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests
import json
import urllib.request
from pprint import pprint
import os

listOfPages  = ['http://www.poetsgate.com/ViewPoem.aspx?id=79899',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79961',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79973',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79923',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79978',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79883',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79934',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79910',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79976',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79888',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79884',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79886',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79913',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79956',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79964',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79929',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79953',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79965',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79880',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79919',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79917',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79967',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79920',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79971',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79981',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79877',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79912',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79882',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79898',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79924',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79935',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79931',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79881',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79979',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79930',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79936',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79878',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79984',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79879',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79900',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79959',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79966',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79970',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79901',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79980',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79982',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79987',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79939',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79943',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79974',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79947',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79928',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79949',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79950',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79972',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79942',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79948',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79902',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79906',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79938',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79955',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79941',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79958',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79944',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79915',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79909',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79885',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79922',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79940',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79895',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79911',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79908',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79932',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79985',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79962',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79952',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79914',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79916',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79960',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79983',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79905',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79903',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79893',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79894',
                'http://www.poetsgate.com/ViewPoem.aspx?id=79904']
#l7atta nt2akkad ennu ma fe tikrar sar bl 3'alat ay url b3mllo
#processing b7otto juwwa list tanyi w bser af7as iza elli 3leh eldoor majood
#bl list altanyi aw la w hakaza
i = 1
pathO= r"D:\GraduationProject1\datasets\arabicPoetries\حريث بن محفض المازني\train"
os.chdir(pathO)
for path in listOfPages:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')
    with open("poetry" + str(i) +".txt", "w" , encoding="utf8") as f:
        f.write("الحريث"+ str(i) + ':')
        f.write("\n")
        for shtr in shatr:
            f.write(str(shtr))
            f.write("\n")
            index = shatr.index(str(shtr))
            f.write(str(ajoz[index]))
            f.write("\n")
            f.write("*")
            f.write("\n")

    print('doneTrain' + str(i))
    i = i + 1



#************** now test dataset  *******************************************

testList = ['http://www.poetsgate.com/ViewPoem.aspx?id=79937',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79957',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79986',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79988',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79925',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79907',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79887',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79933',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79989',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79954',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79975',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79897',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79918',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79963',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79891',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79889',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79946',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79927',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79951',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79977',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79968',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79921',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79892',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79945',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79969',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79876',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79990']

pathO= r"D:\GraduationProject1\datasets\arabicPoetries\حريث بن محفض المازني\test"
os.chdir(pathO)

for path in testList:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')

    with open("poetryTst" + str(i) +".txt", "w" , encoding="utf8") as f:
        for shtr in shatr:
            f.write(str(shtr))
            f.write("\n")
            index = shatr.index(str(shtr))
            f.write(str(ajoz[index]))
            f.write("\n")
            f.write("*")
            f.write("\n")
 
    print('doneTest' + str(i))
    i = i + 1

