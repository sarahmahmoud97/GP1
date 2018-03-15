from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests
import json
import urllib.request
from pprint import pprint
import os

listOfPages =  ['http://www.poetsgate.com/ViewPoem.aspx?id=80694',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80601',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80652',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80653',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80631',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80698',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80654',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80656',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80639',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80655',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80657',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80679',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80621',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80658',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80650',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80696',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80687',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80697',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80651',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80666',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80641',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80640',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80663',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80684',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80616',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80643',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80681',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80664',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80662',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80677',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80625',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80617',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80645',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80626',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80693',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80615',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80669',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80692',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80695',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80611',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80614',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80691',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80612',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80649',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80700',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80678',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80644',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80638',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80610',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80665',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80609',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80634',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80648',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80661',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80683',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80672',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80628',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80619',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80689',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80668',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80667',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80674',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80646',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80608',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80636',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80637',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80675',
                'http://www.poetsgate.com/ViewPoem.aspx?id=4538',
                'http://www.poetsgate.com/ViewPoem.aspx?id=4532',
                'http://www.poetsgate.com/ViewPoem.aspx?id=4535',
                'http://www.poetsgate.com/ViewPoem.aspx?id=22260',
                'http://www.poetsgate.com/ViewPoem.aspx?id=4534',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80680',
                'http://www.poetsgate.com/ViewPoem.aspx?id=4536',
                'http://www.poetsgate.com/ViewPoem.aspx?id=4537',
                'http://www.poetsgate.com/ViewPoem.aspx?id=4533',
                'http://www.poetsgate.com/ViewPoem.aspx?id=22259',
                'http://www.poetsgate.com/ViewPoem.aspx?id=22261',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80624',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80613',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80620',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80701',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80686',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80600',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80627',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80690',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80618',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80630',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80660',
                'http://www.poetsgate.com/ViewPoem.aspx?id=80605']
#l7atta nt2akkad ennu ma fe tikrar sar bl 3'alat ay url b3mllo
#processing b7otto juwwa list tanyi w bser af7as iza elli 3leh eldoor majood
#bl list altanyi aw la w hakaza
i = 1
pathO= r"D:\GraduationProject1\datasets\arabicPoetries\عمرو بن معدي كرب\train"
os.chdir(pathO)
for path in listOfPages:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')
    with open("poetry" + str(i) +".txt", "w" , encoding="utf8") as f:
        f.write("عمرو كرب"+ str(i) + ':')
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

testList = ['http://www.poetsgate.com/ViewPoem.aspx?id=80670',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80671',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80682',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80607',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80602',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80685',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80622',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80699',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80676',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80604',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80673',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80647',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80688',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80659',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80629',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80633',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80603',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80606',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80635',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80632',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80642',
            'http://www.poetsgate.com/ViewPoem.aspx?id=80623']

pathO= r"D:\GraduationProject1\datasets\arabicPoetries\عمرو بن معدي كرب\test"
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

