from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests
import json
import urllib.request
from pprint import pprint
import os

listOfPages = ['http://www.poetsgate.com/ViewPoem.aspx?id=79269',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79297',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79248',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79267',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79293',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79280',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79251',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79292',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79287',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79298',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79290',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79229',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79281',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79233',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79260',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79265',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79273',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79271',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79249',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79236',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79222',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79238',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79242',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79257',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79198',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79301',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79239',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79252',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79250',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79221',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79206',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79202',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79199',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79256',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79235',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79231',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79210',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79208',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79204',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79205',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79212',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79232',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79234',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79201',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79219',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79244',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79200',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79275',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79214',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79253',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79258',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79227',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79207',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79268',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79259',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79203',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79211',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79224',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79240',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79285',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79241',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79243',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79218',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79262',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79247',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79276',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79295',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79274',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79246',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79302',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79226',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79270',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79220',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79299',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79225',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79291',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79277',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79266',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79288',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79216',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79264',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79215',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79230',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79263',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79283',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79237',
               'http://www.poetsgate.com/ViewPoem.aspx?id=79223']
#l7atta nt2akkad ennu ma fe tikrar sar bl 3'alat ay url b3mllo
#processing b7otto juwwa list tanyi w bser af7as iza elli 3leh eldoor majood
#bl list altanyi aw la w hakaza
i = 1
pathO= r"D:\GraduationProject1\datasets\arabicPoetries\العباس بن مرداس\train"
os.chdir(pathO)
for path in listOfPages:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')
    with open("poetry" + str(i) +".txt", "w" , encoding="utf8") as f:
        f.write("العباس"+ str(i) + ':')
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

testList = ['http://www.poetsgate.com/ViewPoem.aspx?id=79300'
            'http://www.poetsgate.com/ViewPoem.aspx?id=79228',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79254',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79279',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79245',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79272',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79261',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79217',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79255',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79284',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79278',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79282',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79213',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79209',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79294',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79286',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79289',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79296',
            'http://www.poetsgate.com/ViewPoem.aspx?id=79303']

pathO= r"D:\GraduationProject1\datasets\arabicPoetries\العباس بن مرداس\test"
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

