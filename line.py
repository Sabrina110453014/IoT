def linemes(mes):

    import requests

#Line群組代號
    token = 'Uxn4DHUd6amLr5pJpUgE5B0GUnX7c3ouk3btaHdTrCw'

# 要發送的訊息
    message = 'IOT專題' + mes

# HTTP 標頭參數與資料
    headers = { "Authorization": "Bearer " + token }
    data = { 'message': message }

# 以 requests 發送 POST 請求
    requests.post("https://notify-api.line.me/api/notify",
        headers = headers, data = data)

def linephoto(file, mes):

    import requests

#Line群組代號
    token = 'Uxn4DHUd6amLr5pJpUgE5B0GUnX7c3ouk3btaHdTrCw'

# 要發送的訊息
    message = 'IOT專題' + mes

# HTTP 標頭參數與資料
    headers = { "Authorization": "Bearer " + token }
    data = { 'message': message }

# 要傳送的圖片檔案/home/pi/
    image = open(file, 'rb')
    files = { 'imageFile': image }

# 以 requests 發送 POST 請求
    requests.post("https://notify-api.line.me/api/notify",
        headers = headers, data = data, files = files)
    
