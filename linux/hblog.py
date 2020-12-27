import subprocess
import os
from time import sleep
while 1:
    os.system('curl http://helli5blog.ir > tmp.html')
    p = subprocess.Popen(['cat','tmp.html'], stdout=subprocess.PIPE)
    try:
        mat=p.communicate()[0].decode('utf-8').split('<h2>')[3]
    except:
        os.system('notify-send "Oops!" "It looks like that your delay is too low!"')
    f=open("last.txt",mode='a+')
    f.seek(0)
    if f.read()==mat:
        sleep(30)
        continue
    else:
        os.system('notify-send "New Post" "New Post is available in hblog!"')
        f.write(mat)
    f.close()
    print(mat)
    sleep(30)
