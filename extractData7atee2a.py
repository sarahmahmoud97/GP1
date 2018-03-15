from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests
import json
import urllib.request
from pprint import pprint
import os

listOfPages = ['http://www.poetsgate.com/ViewPoem.aspx?id=67743',
               'http://www.poetsgate.com/ViewPoem.aspx?id=18926',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19794',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19732',
               'http://www.poetsgate.com/ViewPoem.aspx?id=18844',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19790',
               'http://www.poetsgate.com/ViewPoem.aspx?id=24761',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19733',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19739',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19773',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19725',
               'http://www.poetsgate.com/ViewPoem.aspx?id=18843',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19752',
               'http://www.poetsgate.com/ViewPoem.aspx?id=18845',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19754',
               'http://www.poetsgate.com/ViewPoem.aspx?id=18927',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19741',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19722',
               'http://www.poetsgate.com/ViewPoem.aspx?id=18931',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19729',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19784',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19748',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19774',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19744',
               'http://www.poetsgate.com/ViewPoem.aspx?id=18842',
               'http://www.poetsgate.com/ViewPoem.aspx?id=78948',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19721',
               'http://www.poetsgate.com/ViewPoem.aspx?id=18928',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19808',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19777',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19747',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19805',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19749',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19816',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19768',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19770',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19723',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19814',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19767',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19809',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19730',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19734',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19753',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19750',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19736',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19811',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19726',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19803',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19728',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19763',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19806',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19775',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19766',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19781',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19789',
               'http://www.poetsgate.com/ViewPoem.aspx?id=24760',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19731',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19815',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19787',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19735',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19740',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19810',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19727',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19772',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19737',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19813',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19812',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19780',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19788',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19771',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19804',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19738',
               'http://www.poetsgate.com/ViewPoem.aspx?id=19742']
#l7atta nt2akkad ennu ma fe tikrar sar bl 3'alat ay url b3mllo
#processing b7otto juwwa list tanyi w bser af7as iza elli 3leh eldoor majood
#bl list altanyi aw la w hakaza
i = 1
pathO= r"D:\GraduationProject1\datasets\arabicPoetries\الحطيئة\train"
os.chdir(pathO)
for path in listOfPages:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')
    '''
    if i < 3 :
        for shtr in shatr:
            print(str(shtr))
            index = shatr.index(str(shtr))
            print(str(ajoz[index]))
            print('*')
    '''
    with open("poetry" + str(i) +".txt", "w" , encoding="utf8") as f:
        f.write('الحطيئة'+ str(i) + ':')
        f.write("\n")
        for shtr in shatr:
            f.write(str(shtr))
            f.write("\n")
            index = shatr.index(str(shtr))
            f.write(str(ajoz[index]))
            f.write("\n")
            f.write("*")
            f.write("\n")
    '''
    websource = urllib.request.urlopen('http://www.poetsgate.com/ViewPoem.aspx?id=12343')
    data = json.loads(websource.read().decode())
    pprint(data)
    '''
    
    print('doneTrain' + str(i))
    i = i + 1



#************** now test dataset  *******************************************

testList = ['http://www.poetsgate.com/ViewPoem.aspx?id=19785',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19743',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19778',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78925',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78951',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78939',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78949',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78932',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78943',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78941',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78929',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78935',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78930',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78936',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78937',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19765',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19786',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19751',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78927',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78956',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78934',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78926',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78921',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78931',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78954',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78952',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78928',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78924',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78933',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19807',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19791',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78957',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78955',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78944',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78942',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78950',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78945',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78938',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78922',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78923',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78940',
            'http://www.poetsgate.com/ViewPoem.aspx?id=78946',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19769',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19783',
            'http://www.poetsgate.com/ViewPoem.aspx?id=19746']

pathO= r"D:\GraduationProject1\datasets\arabicPoetries\الحطيئة\test"
os.chdir(pathO)

for path in testList:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')
    '''
    if i < 3 :
        for shtr in shatr:
            print(str(shtr))
            index = shatr.index(str(shtr))
            print(str(ajoz[index]))
            print('*')
    '''
    with open("poetryTst" + str(i) +".txt", "w" , encoding="utf8") as f:
        for shtr in shatr:
            f.write(str(shtr))
            f.write("\n")
            index = shatr.index(str(shtr))
            f.write(str(ajoz[index]))
            f.write("\n")
            f.write("*")
            f.write("\n")
    '''
    websource = urllib.request.urlopen('http://www.poetsgate.com/ViewPoem.aspx?id=12343')
    data = json.loads(websource.read().decode())
    pprint(data)
    '''
    print('doneTest' + str(i))
    i = i + 1
'''
print(shatr)
print(ajoz)

import scrapy

#the url of the page where we will scrape data
poetryURL = ''
# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(poetryURL)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, ‘html.parser’)
# Take out the <div> of name and get its value (this is example)
name_box = soup.find(‘h1’, attrs={‘class’: ‘name’})
name = name_box.text.strip() # strip() is used to remove starting and trailing

# get the index price
price_box = soup.find(‘div’, attrs={‘class’:’price’})
price = price_box.text
print price
'''
