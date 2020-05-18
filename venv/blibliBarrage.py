from bs4 import BeautifulSoup as bs
import re
import requests
import time
import jieba
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from wordcloud import WordCloud as wc

class Bilibili():
  def __init__(self,bv,p):
    self.headers = {
        'Host': 'www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': '',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers',
    }
    self.oid_headers = {
      'Host': 'api.bilibili.com',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
      'Accept': '*/*',
      'Accept-Language': 'en-US,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.5,zh-HK;q=0.3,en;q=0.2',
      'Accept-Encoding': 'gzip, deflate, br',
      'Origin': 'https://www.bilibili.com',
      'Connection': 'keep-alive',
      'Referer': 'https://www.bilibili.com/video/BV1zC4y1s7RW',
      'Cookie': "buvid3=C25B9DC5-A9BC-47B3-9C78-64F0CFEA678634440infoc; fts=1505660785; pgv_pvi=5002299392; rpdid=|(um~u)l)~))0J'ullY|JR|l); LIVE_BUVID=536a84d2108b9990436faa1a2e38708b; CURRENT_QUALITY=116; LIVE_BUVID__ckMd5=accab470ef1e68d3; im_notify_type_6692208=0; CURRENT_FNVAL=16; stardustvideo=1; im_local_unread_6692208=0; im_seqno_6692208=8; _uuid=3E3A2E4E-4776-B7C1-44FC-8DD24F3F1A1798502infoc; sid=7160u9f6; _cnt_dyn=undefined; _cnt_pm=0; _cnt_notify=0; uTZ=-480; laboratory=1-1; PVID=1; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f",
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'TE': 'Trailers'
    }
    self.bv = bv
    self.page = p
    self.bv_url = 'https://www.bilibili.com/video/'+str(bv)
    self.oid = self.get_oid()
    self.bilibili_id = str(self.oid)
    self.oid_url='https://api.bilibili.com/x/v1/dm/list.so?oid='+str(self.bilibili_id)
    self.barrage_result=self.get_page_content()
  #get oid from bv or av
  #return oid
  def get_oid(self):
    if self.page != "":
      #like https://www.bilibili.com/video/BV1zC4y1s7RW?p=2
      self.bv_url = self.bv_url+"?p="+str(self.page)
    try:
      response = requests.get(self.bv_url,headers = self.headers)
    except Exception as e:
      print("get oid fail {}".format(e))
      return 0
    else:
      if response.status_code == 200:
        response.encoding = response.apparent_encoding
        content = response.text
        oid = re.search(r"upgcxcode/\d+?/\d+?/(\d+?)/",content).group(1)
        print("oid: {}".format(oid))
        return oid
      else:
        return 0
  #get list page
  def get_page_content(self):
    try:
      time.sleep(0.5)
      response = requests.get(self.oid_url,headers=self.oid_headers)
    except Exception as e:
      print('request fail, {}'.format(e))
      return False
    else:
      #if succeed
      if response.status_code == 200:
        response.encoding = response.apparent_encoding
        with open(r'venv/static/data/bilibili.xml','wb') as f:
          f.write(response.content)
          print("get page suc")
        return True
      else:
        return False
  #parse the list page
  def get_parse_page(self):
    '''
    tag_string: store all the string in <d> tag
    '''
    if self.barrage_result:
      print(self.barrage_result)
      tag_string=[]
      with open(r'venv/static/data/bilibili.xml','r',encoding="utf-8") as xmlText:
        xml=bs(xmlText,'html.parser')
        results=xml.select("d")
        #add tags
        for i in results:
          tag_string.append(i.string)
      print('parse suc')
      return tag_string
  #count barrage
  def get_barrage_count(self):
    '''
    barrage_dic: a dic storing count barrage
    barrages: barrages in list
    '''
    barrage_dic = {}
    barrages = self.get_parse_page()
    for barrage in barrages:
      # if barrage in barrage_dic.keys():
      #   barrage_dic[barrage]+=1
      # else:
      #   barrage_dic[barrage]=1
      barrage_dic[barrage]=barrage_dic.get(barrage,0)+1
    #change to list  
    barrage_dic = list(barrage_dic.items())
    barrage_dic.sort(key=lambda x:x[1],reverse=True)
    return barrage_dic
  #make wordCloud  
  def makeWordCloud_jieba(self):
    txt = []
    #去掉感叹词
    exclude_words=['【','】',',','.','?','!','。']
    barrages=self.get_parse_page()
    for barrage in barrages:
      # for exclude_word in exclude_words:
      #   barrage="".join(barrage.split(exclude_word))
      txt.append(barrage)
    #从数组转化成一个字符串
    txt=''.join(txt)
    #切割字符串
    txt=jieba.cut(txt)
    #切割结果保存为字符串，中间用空格分离
    txt=' '.join(txt)#should be ' '(a space) but not ''(with no sapce)
    w=wc(height=700, width=1000, font_path="msyh.ttc",max_words=2000)
    w.generate(txt)
    w.to_file(r'venv/static/img/bilibili_'+self.bv + '.jpg')
  def makeWordCloud_nojieba(self):
    txt = []
    barrages=self.get_parse_page()
    for barrage in barrages:
      # for exclude_word in exclude_words:
      #   barrage="".join(barrage.split(exclude_word))
      txt.append(barrage)
    txt=' '.join(barrages)
    w=wc(height=700, width=1000, font_path="msyh.ttc",max_words=10)
    w.generate(txt)
    w.to_file(r'venv/static/img/bilibili_'+self.bv +'_nojieba' + '.jpg')

  #统计每5秒的弹幕密度
  def count_per5sec(self):
    if self.barrage_result:
      with open(r'venv/static/data/bilibili.xml','r',encoding="utf-8") as xmlText:
          xml = bs(xmlText, 'html.parser')
          find_time = re.findall('p="(.+?),.*?"',str(xml))
          #change the string to float
          find_time = list(map(float, find_time))
          #maximun, minimun and length
          max_time = max(find_time)
          min_time = min(find_time)
          len_time = len(find_time)
          list.sort(find_time)
          #time count
          time_count = {}
          step = 5
          #加2.5是为了让最后的centroid覆盖最后发送的弹幕
          time_centroid = range(0,round(max_time+2.5),step)
          for centroid in time_centroid:
            #init
            time_count[centroid] = 0
            for time in find_time:
              if centroid-step/2 <= time <= centroid+step/2:
                time_count[centroid] = time_count[centroid] + 1
          # plt.figure()
          # #change dict_keys type to list type 
          # plt.plot(list(time_count.keys()),list(time_count.values()))
          # plt.show()          
          return time_count

# b=Bilibili('BV1zC4y1s7RW')
# b.makeWordCloud_nojieba()
# b.makeWordCloud_jieba()
# barrage = b.get_barrage_count()
# top10_barrage = [[],[]]
# for i in range(10):
#   print(str(barrage[i][0])+":"+str(barrage[i][1]))
#   #tag
#   top10_barrage[0].append(barrage[i][0])
#   #number
#   top10_barrage[1].append(barrage[i][1])
# #draw bar graph
# #额... ？不是乱码,而是弹幕...不过作为表达弹幕氛围的符号,上面就不排除它了...
# plt.figure()
# plt.bar(range(len(top10_barrage[1])), top10_barrage[1],color='rgb',tick_label=top10_barrage[0])  
# plt.show()  

# b.count_per5sec()