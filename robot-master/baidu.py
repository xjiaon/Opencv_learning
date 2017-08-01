# 引入Speech SDK
from aip import AipSpeech
import json
import recorder
import os,sys
import turing
print ('hello01')
isOk=recorder.recorder()
print ('hello02')
# 定义常量
APP_ID = '9424816'
print ('hello03')
API_KEY = 'qaCMG6wQ0WVejR1IpXoS1ABB'
print ('hello04')
SECRET_KEY = '4c36038b7b31ab119b9a56ed88f70229'
print ('hello05')
# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
print ('hello06')

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        print ('hello07')
        print (fp)
        return fp.read()
# 识别本地文件
print ('hello08')
os.system('output.wav')
try:
    #print ('hellllll')
    result = aipSpeech.asr(get_file_content('output.wav'), 'wav', 8000, {'lan': 'zh'})
    
except Exception as err:
    print ("error")
    result={'err_no': 3301, 'sn': '864541891991501574763', 'err_msg': 'recognition error.'}
print ("done")
#result = aipSpeech.asr(get_file_content('output.wav'), 'wav', 8000, {
#    'lan': 'zh',
#})
print (result)
#json_result = json.dumps(result)
#print ('hello10',json_result)
#strtestObj = json.loads(json_result)
print ('hello11')
#print (result)
#print strtestObj
#lists = strtestObj["result"]
#print ("识别结果：".decode('utf-8').encode('gbk'),lists[0] )
#print (result,lists[0])
ask='hello'
ans=turing.turing('12345',"你好呀")
print (ans)

