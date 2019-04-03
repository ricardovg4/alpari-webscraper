# web scraper for apari, data in ticks(download stopped, could be up to a tera)
# http://ticks.alpari.org/

import numpy as np  
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.request
import os
import wget

url ='http://ticks.alpari.org/'
html = urllib.request.urlopen(url).read() #reads html source
soup = bs(html) #prettify html
tags0 = soup('a') #extracts 'a' anchor tags
tags1 = []
a = [3,4,5,7,8]
for asd in a:
    tags1.append(tags0[asd])
tags1

def downloader(link_level, level):
    ''' function to download an item if is .zip'''
    
    if level == '4':
        if "zip" in link_level:
            try:
                os.makedirs('/home/ricardo/Dropbox/forex/data/alpari/'+link_dest+link_dest2+link_dest3)
            except FileExistsError:
                pass
        resp = urllib.request.urlopen('http://ticks.alpari.org/'+link_dest+link_dest2+link_dest3+link_dest4)
        respHtml = resp.read()
        binfile = open('/home/ricardo/Dropbox/forex/data/alpari/'+link_dest+link_dest2+link_dest3+link_dest4, "wb")
        binfile.write(respHtml)
        binfile.close()
#too slow
#        urllib.request.urlretrieve('http://ticks.alpari.org/'+link_dest+link_dest2+link_dest3+link_dest4, '/home/ricardo/Dropbox/forex/data/alpari/'+link_dest+link_dest2+link_dest3+link_dest4)
   
    elif level == '5':
        if "zip" in link_level:
            try:
                os.makedirs('/home/ricardo/Dropbox/forex/data/alpari/'+link_dest+link_dest2+link_dest3+link_dest4)
            except FileExistsError:
                pass
        resp = urllib.request.urlopen('http://ticks.alpari.org/'+link_dest+link_dest2+link_dest3+link_dest4+link_dest5)
        respHtml = resp.read()
        binfile = open('/home/ricardo/Dropbox/forex/data/alpari/'+link_dest+link_dest2+link_dest3+link_dest4+link_dest5, "wb")
        binfile.write(respHtml)
        binfile.close()
#        urllib.request.urlretrieve('http://ticks.alpari.org/'+link_dest+link_dest2+link_dest3+link_dest4+link_dest5, '/home/ricardo/Dropbox/forex/data/alpari/'+link_dest+link_dest2+link_dest3+link_dest4+link_dest5)


for i in tags1:
    link_dest = i.get('href', None)
    print("LEVEL1:", link_dest)
    current_url = url+link_dest
    html2 = urllib.request.urlopen(current_url).read()
    soup2 = bs(html2)
    tags2 = soup2('a')
    for i2 in tags2[1:]:
        link_dest2 = i2.get('href', None)
        print('LEVEL2:',link_dest2)
        current_url2 = current_url+link_dest2
        html3 = urllib.request.urlopen(current_url2).read()
        soup3 = bs(html3)
        tags3 = soup3('a')
        for i3 in tags3[1:]:
            link_dest3 = i3.get('href', None)
            print("LEVEL3:", link_dest3)
            current_url3 = current_url2+link_dest3
            html4 = urllib.request.urlopen(current_url3).read()
            soup4 = bs(html4)
            tags4 = soup4('a')
            for i4 in tags4[1:]:                       #This level has monthly zips.
                link_dest4 = i4.get('href', None)
                print("LEVEL4:", link_dest4)
                if "zip" in link_dest4:
                    downloader(link_dest4,'4')
                elif "zip" not in link_dest4:
                    current_url4 = current_url3+link_dest4
                    html5 = urllib.request.urlopen(current_url4).read()
                    soup5 = bs(html5)
                    tags5 = soup5('a')
                
#Duplicate information, daily not needed, included in monthly zip.                    
#                    for i5 in tags5[1:]:                   #This level has daily zips.
#                        link_dest5 = i5.get('href', None)
#                        print("LEVEL5:", link_dest5, "DESTINATION:",link_dest+link_dest2+link_dest3+link_dest4+link_dest5)
#                        if "zip" in link_dest5:
#                            downloader(link_dest5,'5')
#                        elif "zip" not in link_dest5:
#                            current_url5 = current_url4 + link_dest5
#                            html6 = urllib.request.urlopen(current_url5).read()
#                            soup6 = bs(html6)
#                            tags6 = soup6('a')
#
#                            
#                            if not tags6:
#                                tags6 = None
#                        else:
#                            tags6 = None
#
#                            try:
#                                for i6 in tags6[1:]:
#                                    link_dest6 = i6.get('href', None)
#                                    print("LEVEL6:",link_dest6)
#                            except:
#                                link_dest6=""
#                                print("NO MORE LEVELS")
#





