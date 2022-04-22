import cv2
import dropbox
import time
import random

starttime=time.time()
def takesnapshot():
    randomnumber=random.randint(0,100)
    imagetaken=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=imagetaken.read()
        imagename="image"+str(randomnumber)+".png"
        cv2.imwrite("imagename",frame)
        result=False
        print("IMAGE CAPTURED") 

#takesnapshot()

def uploadfile(imagename):
    accesstoken="sl.BGPBRZBbCyaF9CQPx4NBGX0wsZGaUZgl3-uyNEJC7GQ2JbfqYQKmimrE-zrDWRqHTNytA1FbRbdWGoldeiRCIXaXtGcfarmFv9WN-5HAn1hKi9e3x49Fi8lSknphHQzYhlSUS-pAijmj"
    filefrom=imagename
    fileto="/newfolder/"+(imagename)
    dbx=dropbox.Dropbox(accesstoken)

    with open(filefrom,"rb") as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("FILES UPLOADED") 
     


def main():
    while(True):
        if(time.time()-starttime>=5):
            name= takesnapshot()
            uploadfile(name)


main()        

