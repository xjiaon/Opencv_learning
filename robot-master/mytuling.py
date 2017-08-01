import urllib.request
#打开网页用的
import win32com.client
#发音用到的
#import json
#字符串转字典，这里用到了eval,没用到json,注释掉了
from urllib.parse import quote
#中文输入url字符用的， 当url中包含钟文时，需要转换
#http = urllib3.PoolManager()
print ("我是捷德中国智能机器人图灵大白，想聊点什么？\n")
#机器人开场白
speaker = win32com.client.Dispatch("SAPI.SpVoice")
#声音调用这个
while 1>0:
    
    myword=input('我：\n')
    #输入提示符
    #myword='你会说话不'
    url0='http://www.tuling123.com/openapi/api?key=29ccde937cd544afbd45667b4be9805e&userid=12345&info='+myword
    #图灵的网址+自己创建的myword关键词
    url=('\n%s' % quote(url0, safe='/:&?='))
    #把中文关键词转化为url能够接受的形式
    #print (url)
    #如果没有网络，或其他错误，显示没有网络
    try:
        
        fb=urllib.request.urlopen(url)
        mybytes=fb.read()
        mystr=mybytes.decode('utf8')
        feedback=eval(mystr)['text'].replace("曾先森", "捷德中国")
        #替换，把曾先森换为捷德中国
    except:
        feedback="没有网络，不跟你好啦"
    #print (feedback.replace("曾先森", "捷德"))
    print (feedback)
    #print (type(feedback))
    
    speaker.Speak(feedback)
    #说出话来
