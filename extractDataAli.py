from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests
import json
import urllib.request
from pprint import pprint
import os

listOfPages = ['http://www.poetsgate.com/ViewPoem.aspx?id=22713',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10079',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22734',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22629',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22737',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22665',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22551',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10101',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10042',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10099',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10874',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10084',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22546',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22779',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22722',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22746',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22739',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10877',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22711',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10045',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22725',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22736',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11530',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22740',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10868',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22771',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22727',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11535',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22654',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10046',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10041',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22816',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22664',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10078',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22705',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22550',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10870',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22704',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22710',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22543',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10080',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22553',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10044',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10077',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10076',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22748',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22823',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22735',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10872',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22626',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22728',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10869',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22759',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10878',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22822',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22721',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22741',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10054',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22726',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22641',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10102',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22549',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10096',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22815',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22645',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22820',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22747',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22757',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22663',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10043',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22637',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10100',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10082',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22738',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22766',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22656',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22556',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10865',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22752',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22554',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10875',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22765',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22718',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10867',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22719',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10048',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22760',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22754',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22640',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10866',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22733',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22774',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22764',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22758',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22708',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22780',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22814',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11534',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22753',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22751',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22767',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22715',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22762',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10083',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22755',
               'http://www.poetsgate.com/ViewPoem.aspx?id=10081',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22750',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22769',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22717',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22648',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22703',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22723',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22649',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22659',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22548',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11531',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22547',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22542',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22706',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22552',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22821',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22745',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11533',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22729',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22653',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22743',
               'http://www.poetsgate.com/ViewPoem.aspx?id=22714']
#l7atta nt2akkad ennu ma fe tikrar sar bl 3'alat ay url b3mllo
#processing b7otto juwwa list tanyi w bser af7as iza elli 3leh eldoor majood
#bl list altanyi aw la w hakaza
i = 1
pathO= r"D:\GraduationProject1\datasets\arabicPoetries\علي بن ابي طالب\train"
os.chdir(pathO)
for path in listOfPages:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')
    with open("poetry" + str(i) +".txt", "w" , encoding="utf8") as f:
        f.write('علي بن'+ str(i) + ':')
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

testList = ['http://www.poetsgate.com/ViewPoem.aspx?id=22655',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22651',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22763',
            'http://www.poetsgate.com/ViewPoem.aspx?id=10098',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22744',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22634',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22724',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22742',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22777',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22631',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22555',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22818',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22661',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22709',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22778',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22772',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22669',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22660',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22632',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22558',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22712',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22544',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22775',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22768',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22545',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22773',
            'http://www.poetsgate.com/ViewPoem.aspx?id=10098',
            'http://www.poetsgate.com/ViewPoem.aspx?id=10097',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22749',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22756',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22646',
            'http://www.poetsgate.com/ViewPoem.aspx?id=10876',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22731',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22776',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22817',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22720',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22730',
            'http://www.poetsgate.com/ViewPoem.aspx?id=22770']

pathO= r"D:\GraduationProject1\datasets\arabicPoetries\علي بن ابي طالب\test"
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

