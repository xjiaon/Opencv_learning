import os,sys,codecs
def freefilesync_mask(item):
    #s =item
    #print (s)
    #if isinstance(item, unicode):
    #    item = item.encode('utf-8')
    #item=item.encode().decode()
    print (item)
    f=codecs.open('BatchRun.ffs_batch','r+',encoding='utf-8')
    flist=f.readlines()
    flist[40]='		<Left>//'+item+'/'+a1+'</Left>\n'
    flist[41]='		<Right>'+a2+item+'</Right>\n'
    if os.path.exists(a2+item):
        pass
    else:
        os.makedirs(a2+item)
    print ('from',flist[40],'to',flist[41])
    #print (flist)
    f=codecs.open('BatchRun.ffs_batch','w+',encoding='utf-8')
    f.writelines(flist)
    f.close()
    os.system('BatchRun.ffs_batch')
#freefilesync_mask('item1dsfsdfdsgsdg')
f=open('config.ini', 'r')
#location=f.readlines()
#print (location)
print ('**********start****************')
a1=f.readlines()[0][:-1]
f=open('config.ini', 'r')
print ('1st line is ',a1)
a2=f.readlines()[1][:-1]
print ('2nd line is ',a2)
f=open('config.ini', 'r')
for line in f.readlines()[2:]:
    item=line[:-1]
    print (item)
    freefilesync_mask(item)
print ('***********end****************')


