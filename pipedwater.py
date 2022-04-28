import codecs
import json
with open('pipedwater.json', 'r', encoding='utf-8') as j:
        getdata = json.load(j)
from ftplib import FTP

#อ้างอิงค์จากการบ้าน
def downloadFile():
    filename = 'pipedwater.json '
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    
    localfile.close()
#อ้างอิงค์จากการบ้าน   
def uploadFile():
    filename = 'pipedwater.txt'
    ftp.storbinary('STOR ' + filename,  open(filename, 'rb'))
    filename1 = 'pipedwater.json'
    ftp.storbinary('STOR ' + filename1,  open(filename1, 'rb'))

try:
    #///////////////////////////////////////////
    ftp = FTP("158.108.97.18")
    ftp.login(user="ST03603423",passwd="03603423")
    
    num = 0 #จำนวนปี
    Psum = 0 #คะแนนทั้งหมด
    #ปริมาณน้ำที่ผลิตได้
    score = []  
    score0 = []
    
    #ปริมาณน้ำจำหน่าย
    supply=[]
    supply0=[]
    
    #กำไรจากการจำหย่ายน้ำ 
    total=[]
    total0=[]
    
    # %การผลิตในแต่ละปี
    percentage=[]
    percentage0=[]
   
    
   #จำนวนผู้ใช้น้ำ
    users=[]
    users0=[]
    try:
        for i in getdata:
            Psum=int(i["p1"])+int(i["p2"])
            
            num+=1
            
            score.append(int(i["p1"]))
            score.append(int(i["year"])) 
            score0.append(score)
            
            
            supply.append(int(i["p2"]))
            supply.append(int(i["year"])) 
            supply0.append(supply)
            
            
            Psum=int(i["p8"])-int(i["p7"])
            total.append(Psum)
            total.append(int(i["year"])) 
            total0.append(total)
            
            percentage.append(int(i["p3"]))
            percentage.append(int(i["year"])) 
            percentage0.append(percentage)
            
            
            users.append(int(i["p4"]))
            users.append(int(i["year"])) 
            users0.append(users)
            
            users =[]
            total = []
            percentage = []
            supply = []
            score = []
       # print(score)
        print(score0)
       # print(i)
        #print(i["p1"])  # เข้าถึงข้อมูลใน dict ของคีย์ nameง
    except TypeError:
        print("object is not iterable")
    p1max=max(score0)
    p1min=min(score0)


    p2max=max(supply0)
    p2min=min(supply0)
    
    psummax=max(total0)
    psummin=min(total0)
    
    p3max=max(percentage0)
    p3min=min(percentage0)
    
    p4max=max(percentage0)
    p4min=min(percentage0)
    
    try:       
         report = codecs.open("pipedwater.txt",'w',"utf-8")
         report.write("ข้อมูลน้ำประปาของประเทศ " "\n")
         report.write("ปีที่มีการผลิตน้ำประปามากสุด " + str(p1max[1])+"  เป็นจำนวน  " + str(p1max[0])+ " ล้าน ลบ.ม.""\n")
         report.write("ปีที่มีการผลิตน้ำประปาน้อยสุด " + str(p1min[1])+"  เป็นจำนวน  " + str(p1min[0])+ " ล้าน ลบ.ม.""\n")
         
         report.write("ปีที่มีปริมาณจำหน่ายประปามากสุด " + str(p2max[1])+"  เป็นจำนวน  " + str(p2max[0])+ " ล้าน ลบ.ม.""\n")
         report.write("ปีที่มีปริมาณจำหน่ายน้ำประปาน้อยสุด " + str(p2min[1])+"  เป็นจำนวน  " + str(p2min[0])+ " ล้าน ลบ.ม.""\n")
        
         report.write("ปีที่มีกำไรจากการจำหน่ายน้ำประปามากสุด " + str(psummax[1])+"  เป็นจำนวน  " + str(psummax[0])+ " ล้านบาท""\n")
         report.write("ปีที่มีกำไรจากการจำหน่ายน้ำ น้ำประปาน้อยสุด " + str(psummin[1])+"  เป็นจำนวน  " + str(psummin[0])+ " ล้านบาท""\n")
        
        
         report.write("ปีที่มี % การใช้น้ำประปามากสุด " + str(p3max[1])+"  เป็นจำนวน  " + str(p3max[0])+ " %""\n")
         report.write("ปีที่มี % การใช้น้ำประปาน้อยสุด " + str(p3min[1])+"  เป็นจำนวน  " + str(p3min[0])+ " %""\n")
       
         report.write("ปีที่มี จำนวนผู้ใช้น้ำมากสุด " + str(p4max[1])+"  เป็นจำนวน  " + str(p4max[0])+ " คน""\n")
         report.write("ปีที่มี จำนวนผู้ใช้น้ำน้อยสุด " + str(p4min[1])+"  เป็นจำนวน  " + str(p4min[0])+ " คน""\n")
         report.write("ปีที่มี จำนวนผู้ใช้น้ำน้อยสุด " + str(p4min[1])+"  เป็นจำนวน  " + str(p4min[0])+ " คน""\n")
         report.write("แหล่งที่มา ข้อมูล สถิติ <https://teams.microsoft.com/l/message/19:lT2V7MKsLhwjWe-AwqXyftj03nNzHqCDy7uSeWLxvt81@thread.tacv2/1647260208162?tenantId=8c1832ea-a96d-413e-bf7d-9fe4d608e00b&amp;groupId=a87aebe1-02a6-4d76-aea7-4b3b371bba0f&amp;parentMessageId=1647250170655&amp;teamName=2021-2 03600390 COOP Prep. 800 Mon 16.30-19.30&amp;channelName=General&amp;createdTime=1647260208162> ""\n")
         report.close()
    
    
    
    except :
       print("can not write") 
    try:
        #สร้างโฟเดอร์ใน winscp
        ftp.cwd('6230300460')  #เข้าไปในโฟเดอร์
    except:
        ftp.cwd('6230300460')
    try:
        uploadFile()
    except:
        print('file not found')
        
except TimeoutError:
    print('timeouterror')
except ConnectionRefusedError:
    print('server no response')
