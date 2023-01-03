def faceidentify():

    import cv2																								#呼叫OpenCV
    from datetime import datetime

    recognizer = cv2.face.LBPHFaceRecognizer_create()         # 啟用訓練人臉模型方法
    recognizer.read('face.yml')                               # 讀取人臉模型檔
#   cascade_path = "haarcascade_frontalface_default.xml"  		# 載入人臉追蹤模型
#   face_cascade = cv2.CascadeClassifier(cascade_path)        # 啟用人臉追蹤
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    then = datetime.now()		#
    duration_in_s=0.0			#

    cap = cv2.VideoCapture(0)                                 # 開啟攝影機
    if not cap.isOpened():																		# 判斷相機是否有啟動
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()																	# 讀取相機資料
        if not ret:
            print("Cannot receive frame")
            break
#    img = cv2.resize(img,(540,300))              						# 縮小尺寸，加快辨識效率
        img = cv2.resize(img,(640,480))              					# 縮小尺寸，加快辨識效率
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  					# 轉換成黑白
#    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  		# 追蹤人臉 ( 目的在於標記出外框 )
        faces = faceCascade.detectMultiScale(
            gray,																							# 灰階
            scaleFactor=1.1,																	# 倍率參數 
            minNeighbors=10,																	# 數字越大月準確
            minSize=(20, 20)																	# 最小可識別的區域
        )
    
    # 建立姓名和 id 的對照表
        name = {
            '1':'EE',																					# 蔡英文
            '2':'Winnie',																			# 習近平
#        '3':'Mia'
        }
    # 依序判斷每張臉屬於哪個 id
        text = 'unknow'																								# 初始宣告
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)            # 標記出人臉外框
            idnum,confidence = recognizer.predict(gray[y:y+h,x:x+w])  # 取出 id 號碼以及信心指數 confidence
            print(idnum , confidence)
            if confidence < 75:
                text = name[str(idnum)]                               # 如果信心指數小於 75，取得對應的idnum還有名字
#                return text																					# 回傳名子
            else:
                text = 'Mia'                                          # 不然名字就是 ???
#                return text
        # 在人臉外框旁加上名字
            cv2.putText(img, text, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)	

        cv2.imshow('Mia', img)																# 畫面上顯示相機及時影片+人臉識別結果
    
        now = datetime.now()																	# 定義現在時間,計算秒數使用
        duration = now - then
        duration_in_s = duration.total_seconds()
    
        if duration_in_s > 10:																# 識別超過10秒後，停止識別程式，回傳text
            cap.release()
            cv2.destroyAllWindows()
            return text
            break
    
        if cv2.waitKey(5) == ord('q'):												# 手動按鍵盤上的q即可跳出迴圈，回傳text
            cap.release()
            cv2.destroyAllWindows()
            return text
            break    																					# 按下 q 鍵停止
    cap.release()
    cv2.destroyAllWindows()