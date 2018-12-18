# TOC Project 2019

## 使用教學
### 每次使用須執行:
1. $./ngrook http 5000  (ngrook需去官網下載，放在同資料夾下)
2. $python3 app.py
3. 到FB developer的產品的webhook，選擇"page"的subscribe。webhook的網址從1.取得，token打123(app.py裡的設定)
4. 開始用粉專傳訊息 (由管理員傳才會有回應)(權限問題)

### clone下來後的僅須一次:
1. 環境安裝
```sh
pip3 install -r requirements.txt
```
2. 取得粉專token(xxx)(從developer取得)，存在本機端(若重新產生token，則需要再打一次)
```sh
export ACCESS_TOKEN=xxx
```
然後在需要的程式碼裡面打上這段來取得  
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")


### 環境需求
* Python 3 (透過$python3 -V 看版本)
* Facebook Page and App (創一個粉專並且盡到FB developer做一些設定)
* HTTPS Server (看下面的ngrok)

### ngrok介紹
ngrok是一個可以將local端的server連到外面的辦法  
透過以下這段程式碼，可以得到https的網址，這個網址給別人，別人就可以跟local端互動
```sh
./ngrok http 5000
```

即使是要https，一樣是打http
5000為port，須跟程式碼裡設定一樣  
run(host="localhost", port=5000, debug=True, reloader=True)

### 主程式碼介紹
app.py做以下幾件事  
(1)一開始的webhook設定  
(2)接收request  
(3)呼叫fsm.py做處理  
(3)從fsm.py呼叫utils.py回傳訊息給messenger user  
```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Note
1. app.py中一開始的webhook設定的token可以隨便打，跟FB developer設定一樣就好  
2. 可是utils.py中要send回去給messenger時，就需要用粉專的token(從FB developer的權杖產生取得)  
3. 資料夾中的demo只是練習(不完整)，無法跟messenger聯絡  
4. FB developer要注意的地方  
(1)左邊的產品的勾勾都要是綠色  
(2)產品Messenger的設定的webhook要記得訂閱粉專(有時會有問題可以重新訂閱)  
(3)產品的Webhook記得是要選page，不是user。subscribe時的token設定看Note的(1)  

  
## 作業介紹&FAQ
More details in the [Slides](https://hackmd.io/p/SkpBR-Yam#/) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)
