# 教學 https://ithelp.ithome.com.tw/articles/10202121
# pip報錯 https://www.crifan.com/windows_python_install_error_could_not_install_/

import requests
from bs4 import BeautifulSoup

# url

for cate in range(34,50):
    for typ in range(0,6):
        url = "http://bs.chinese-linguipedia.org/api/web/diff/search?category=" + str(cate) + "&page=" + "&word=" + "&type=" + str(typ)  #+"&_=1633335898303"

        r = requests.get(url) #category,page迴圈 #type
        print(r.json())
        #soup = BeautifulSoup(r.text,"html")
