import os
import easygui
import datetime
from base64decode import base64decob
from base64encode import base64encob


while 1:
    r = input('编码(B）解码（P）')
    if r == 'b' or r == 'B':
        file = easygui.fileopenbox(msg = '请选择要编码的文件')
        t1 = datetime.datetime.now()
        dirname, filename = os.path.split(file)
        name = filename.split('.')[0]
        with open(file,'rb')as im:  # read out the pic's binary
            img = im.read()
            
        bases = base64encob(img)
        
        with open(name + '.txt','wb')as im:#write these str into a txt with binary
            im.write(bases)
        t2 = datetime.datetime.now()
        print('完成! 用时：',str(t2-t1))

    elif r == 'P' or r == 'p':
        file = easygui.fileopenbox(msg = '请选择要还原的文件')
        name = easygui.enterbox(msg = '请输入还原后的文件名')
        t1 = datetime.datetime.now()
        with open(file,'rb')as im:#read out these binary into bytes
            img = im.read()
        before = len(img)
        
        basee = base64decob(img)  #decode these bytes into real img bytes
        
        after = len(basee)
        with open(name,'wb')as im:#write it into a picture
            im.write(basee)
        t2 = datetime.datetime.now()
        print('还原成功！压缩比%.04f'%(after/before))
        print('用时：',str(t2-t1))
    elif r == 'Q' or r == 'q':
        break
    else:
        print('未知操作，请重新输入')

