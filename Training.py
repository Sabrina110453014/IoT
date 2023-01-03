import cv2																				# 呼叫OpenCV
import numpy as np
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # 載入人臉追蹤模型
recog = cv2.face.LBPHFaceRecognizer_create()      # 啟用訓練人臉模型方法
faces = []   																			# 儲存人臉位置大小的串列
ids = []     																			# 記錄該人臉 id 的串列
X=1

for i in range(1,21):
    img = cv2.imread(f'./EE/{X}.jpg')           	# 依序開啟每一張蔡英文的照片
#    print(f'./EE/{X}.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    face = detector.detectMultiScale(gray)        # 擷取人臉區域
    X=X+1
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄蔡英文人臉的位置和大小內像素的數值
        ids.append(1)                             # 記錄蔡英文人臉對應的 id，只能是整數，都是 1 表示蔡英文的 id 為 1
X=1
for i in range(1,21):
    img = cv2.imread(f'./Winnie/{X}.jpg')         # 依序開啟每一張習近平的照片
#    print(f'./Winnie/{X}.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    face = detector.detectMultiScale(gray)        # 擷取人臉區域
    X=X+1
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄習近平人臉的位置和大小內像素的數值
        ids.append(2)                             # 記錄習近平人臉對應的 id，只能是整數，都是 2 表示習近平的 id 為 2

print('training...')                              # 提示開始訓練
recog.train(faces,np.array(ids))                  # 開始訓練
recog.save('face.yml')                            # 訓練完成儲存為 face.yml
print('ok!')