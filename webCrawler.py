# 抓取網頁原始碼(HTML)
import urllib.request as req
url = "http://www.chinese-linguipedia.org/search_difference_results.html?category=35" #這是小吃點心

#建立一個Request 物件，附加 Request Headers 的資訊 (讓自己看起來比較像正常使用者)
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
})

#(原本括號內是url)
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

# 解析原始碼，取的每篇文章標題(使用beautiful soup)
import bs4
root = bs4.BeautifulSoup(data, "html.parser") #讓BeautifulSoup協助我們解析HTML格式文件
#titles = root.find_all("div",class_ ="content") #尋找所有class="nav-list"的ul標籤 #find找標籤名稱,篩選條件

titles = root.find_all("a",".js-row-tw")

for title in titles:
     if title.a != None: #如果包含a標籤則印出
        print(titles.a.string)
