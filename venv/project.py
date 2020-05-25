from flask import Flask
from flask import request
from flask import Response
from flask import render_template
import pymysql
import blibliBarrage as b
import json
app = Flask (__name__)

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def func(sql,m='r'):
    conn = pymysql.connect (host='127.0.0.1', port=3306, user='root', password='123456', db='networkproject', charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    try:
        cursor.execute (sql)
        if m == 'r':
            data = cursor.fetchall ()
        elif m == 'w':
            py.commit ()
            data = cursor.rowcount
    except:
        data = False
        py.rollback ()
    cursor.close()
    conn.close ()
    return data
@app.route("/")
def index():
  return render_template("test.html")

#get density of barraige
@app.route("/getdensity", methods = ['GET'])
def getDensity():
  #get the sending index
  bv = request.args['bv']
  p_num = request.args['p_num']
  #init
  bili=b.Bilibili(bv,p_num)
  content = json.dumps(bili.count_per5sec())
  resp = Response_headers(content)
  return resp

#get wordcCount and wordCloud
@app.route("/getWordCount", methods = ['GET'])
def getWordCount():
  #get the sending index
  bv = request.args['bv']
  p_num = request.args['p_num']
  bili=b.Bilibili(bv,p_num)
  #generate word cloud img
  # bili.makeWordCloud_jieba()
  #word count
  barrage = bili.get_barrage_count()
  top10_barrage = {}
  #if barrages less than 10
  if len(barrage) < 10:
    for i in barrage:
      top10_barrage[i[0]] = i[1]
  else:
    # 0~9 which contains ten word
    # should not be 10!!!!!!!!
    for i in range(9):
      top10_barrage[barrage[i][0]] = barrage[i][1]
  content = json.dumps(top10_barrage)
  resp = Response_headers(content)
  print(resp)
  return resp

@app.route("/getWordCloud", methods = ['GET'])
def getWordCloud():
  #get the sending in index
  bv = request.args['bv']
  p_num = request.args['p_num']
  bili = b.Bilibili(bv,p_num)
  wordList = bili.getWordCloud_jieba()
  #返回的词数量
  wordList = wordList[0:99]
  wordData = json.dumps(wordList)
  resp = Response_headers(wordData)
  return resp
