import cv2
import dropbox
import time
import random
start_time=time.time()
def take_Snapshot():
    number=random.randint(0,100)
    
    videoCaptureObject = cv2.VideoCapture(0)
    
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite("new picture1.jpg",frame)
        start_time = time.time
        result=False
    return img_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadFile(img_name):
    access_token = 'sl.BBctxEwz-0NwrAG7lKJ_NTLS1AmKCAKmmt7kTJVorCf70Y5ucmh41hNeOE8cFdqG1y5vxWFmcDxfb2yrRblgv2YiJzLf9BmOrzqw_2Z4ZR9CJqq3Ry6ZsANlaSqUvesW7NYZwlE'
    file=img_name
    fileFrom  = file
    file_to = "/image/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(fileFrom,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.file.WriteMode.overWrite)
        print("file uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_Snapshot()
            uploadFile(name) 
main()  