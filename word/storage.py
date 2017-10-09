import easygui as g
import xlrd,os
def switch(choice):
    if choice=='入库':
        print ('入库')
    if choice=='出库':
        print ('出库')
    if choice=='新增':
        print ('新增')
        data = xlrd.open_workbook('storage.xls')
        table = data.sheet_by_name('data')
        nrows = table.nrows
        #ncols = table.ncols
        #nrows代表行数
        
        data='NC'+str(nrows+5010001001)
        
        
        st = g.enterbox("请输入物品描述：\n")

        ccbox = g.ccbox(data+": "+st,title="新增",choices=('确定','取消'))
        if ccbox==True:
            print ('y')
        print (ccbox)
    if choice=='库存':
        print ('库存')
        os.system('storage.xls')
        
    return 'end'
#import image
title='捷德备件管理系统'
msg='请问要执行哪类操作？'
ok_button='你确定？'
image='python.png'
#g.msgbox(msg,title)
choices=['入库','出库','新增','库存']
#choice=g.choicebox(msg,title,choices)
#g.msgbox(choice,title,ok_button,image)
#g.ccbox(msg,choices=('y','n'))
choice=g.buttonbox(msg,title,choices)
#g.indexbox(msg,title,choices)
switch(choice)


