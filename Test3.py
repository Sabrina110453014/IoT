from gpiozero import MotionSensor, LED	#GPIO
from time import sleep
from datetime import datetime						#計算時間用
from Training2a import faceidentify			#呼叫人臉識別程式
from line import linephoto							#呼叫發送Line訊息程式
import pygame														#播放音樂使用
import cv2															#OpenCV

led = LED(23)	#LED腳位pin 23
led.off()
pir = MotionSensor(24) #物體移動偵測pin 24
Mia="0"
sleep(10)

while True:
    if pir.motion_detected:							#看是否有物體移動
        led.on()												#led亮燈
        now = datetime.now()
        t1 = now.strftime("%Y-%m-%d, %H:%M:%S")
        print(t1 , "Someone moved!")
        
        cap = cv2.VideoCapture(0)				#OpenCV開啟相機
        ret, frame = cap.read()					#讀取相機資料

        for i in range(10):
            sleep(1)
            cv2.imwrite('test'+str(i)+'.jpg', frame) # 儲存10張圖片,每張間隔1秒
            
#        then = datetime.now()
#        duration_in_s = 0

#        fourcc = cv2.VideoWriter_fourcc(*'XVID')
#        out = cv2.VideoWriter('output.avi', fourcc, 120, (640,480))
#        ret, frame = cap.read()		# 讀取影格
        
#        while duration_in_s < 10:
#            out.write(frame)
#            now = datetime.now()
#            duration = now - then
#            duration_in_s = duration.total_seconds()

        cap.release()										#抓完照片,釋放鏡頭
#        out.release()
        cv2.destroyAllWindows()
        
        print("faceidentify")						#進入人臉識別
        a='unknow'
        sleep(2)      
        a=faceidentify()								#人臉識別主程式faceidentify
        print(a)       									#會回傳return EE=蔡英文 / Winnie=習近平 
        sleep(2)
        
        if a=='EE':
            mes="蔡總統來了"
            file="Music/2.mp3"
        
        if a=='Winnie':
            mes="飛彈來了快找掩護!!"
            file="Music/1.mp3"
        
        if a=='Mia':
            mes="是平民老百姓"
            file="Music/3.mp3"
    
        linephoto('test9.jpg' , t1 +' '+ mes)		#發送line通知 & 第10張的照片
        pygame.mixer.init(frequency=44100)			#使用pygame播放聲音,設定取樣數
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.load(file)						#設定檔案名稱,加載檔案
        pygame.mixer.music.play()								#開始撥方音樂
        sleep(10)
        pygame.mixer.music.stop()								#10秒後關閉音樂
        sleep(5)

else:							#沒有物體被偵測到移動
        sleep(2)
        led.off()
        a="nothing"
        
    
    
    
