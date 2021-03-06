from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests
import json
import urllib.request
from pprint import pprint
import os

listOfPages = ['http://www.poetsgate.com/ViewPoem.aspx?id=11422',
               'http://www.poetsgate.com/ViewPoem.aspx?id=32628',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39363',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11528',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39520',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39450',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39349',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39347',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39690',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39492',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39389',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39397',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39724',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39393',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39651',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11418',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11527',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11529',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11419',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39343',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39365',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39362',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39364',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39355',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39708',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39435',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39346',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39655',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39529',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39357',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11417',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11420',
               'http://www.poetsgate.com/ViewPoem.aspx?id=11421',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39420',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39345',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39739',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39737',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39361',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39634',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39351',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39734',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39383',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39565',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39674',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39730',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39373',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39353',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39366',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39659',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39525',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39560',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39469',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39369',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39715',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39718',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39482',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39442',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39425',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39699',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39348',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39356',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39344',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39457',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39633',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39449',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39625',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39419',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39377',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39490',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39732',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39685',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39447',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39391',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39352',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39736',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39358',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39680',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39619',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39398',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39481',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39467',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39710',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39688',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39489',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39354',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39384',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39360',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39505',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39689',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39437',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39451',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39421',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39367',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39693',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39570',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39424',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39706',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39375',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39667',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39615',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39729',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39599',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39733',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39600',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39350',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39456',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39374',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39376',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39436',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39585',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39720',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39359',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39702',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39385',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39422',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39512',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39541',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39418',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39372',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39606',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39591',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39652',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39429',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39395',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39433',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39491',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39596',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39575',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39679',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39535',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39394',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39635',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39371',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39461',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39518',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39452',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39731',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39707',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39660',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39497',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39701',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39586',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39386',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39738',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39632',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39474',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39658',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39700',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39401',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39574',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39439',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39719',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39712',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39716',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39370',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39477',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39513',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39697',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39616',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39380',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39673',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39445',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39554',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39511',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39698',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39521',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39597',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39390',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39523',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39528',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39427',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39430',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39653',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39378',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39572',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39448',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39610',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39465',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39472',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39453',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39459',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39396',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39487',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39460',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39543',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39654',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39503',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39381',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39568',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39714',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39382',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39563',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39475',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39677',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39509',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39473',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39444',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39646',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39631',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39531',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39727',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39711',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39438',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39526',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39647',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39396',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39675',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39379',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39703',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39692',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39446',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39530',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39400',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39426',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39466',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39649',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39603',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39432',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39637',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39537',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39462',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39388',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39614',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39549',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39470',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39501',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39455',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39527',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39705',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39483',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39443',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39464',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39608',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39589',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39533',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39485',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39524',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39704',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39532',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39454',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39605',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39640',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39510',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39387',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39507',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39569',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39573',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39480',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39559',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39713',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39558',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39555',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39582',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39471',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39500',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39676',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39553',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39588',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39630',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39423',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39609',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39463',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39672',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39519',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39546',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39622',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39562',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39476',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39515',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39590',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39399',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39576',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39494',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39544',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39488',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39681',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39495',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39709',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39648',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39638',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39678',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39428',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39604',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39636',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39671',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39595',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39550',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39580',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39506',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39551',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39508',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39561',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39540',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39479',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39545',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39618',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39620',
               'http://www.poetsgate.com/ViewPoem.aspx?id=39564']
#l7atta nt2akkad ennu ma fe tikrar sar bl 3'alat ay url b3mllo
#processing b7otto juwwa list tanyi w bser af7as iza elli 3leh eldoor majood
#bl list altanyi aw la w hakaza
i = 1
pathO= r"D:\GraduationProject1\datasets\arabicPoetries\حسان بن ثابت\train"
os.chdir(pathO)
for path in listOfPages:
    page = requests.get(path)
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    shatr = tree.xpath('//div[@class="col1 first"]/text()')
    #This will create a list of prices
    ajoz = tree.xpath('//div[@class="col2 second"]/text()')
    with open("poetry" + str(i) +".txt", "w" , encoding="utf8") as f:
        f.write('حسان'+ str(i) + ':')
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

testList = ['http://www.poetsgate.com/ViewPoem.aspx?id=39662',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39567',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39602',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39504',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39431',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39663',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39392',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39547',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39478',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39656',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39368',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39579',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39644',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39601',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39534',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39517',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39682',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39557',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39548',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39556',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39498',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39539',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39612',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39536',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39542',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39687',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39593',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39584',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39522',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39496',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39493',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39669',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39592',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39617',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39552',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39484',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39514',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39566',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39581',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39598',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39486',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39664',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39516',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39538',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39458',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39499',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39613',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39691',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39587',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39594',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39629',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39583',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39468',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39578',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39665',
            'http://www.poetsgate.com/ViewPoem.aspx?id=39607']

pathO= r"D:\GraduationProject1\datasets\arabicPoetries\حسان بن ثابت\test"
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

