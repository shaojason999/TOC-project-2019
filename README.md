# TOC Project 2019

Template Code for TOC Project 2019

A Facebook messenger bot based on a finite state machine

More details in the [Slides](https://hackmd.io/p/SkpBR-Yam#/) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)

## Setup

### Prerequisite
* Python 3 (透過$python3 -V 看版本)
* Facebook Page and App (創一個粉專並且盡到FB developer做一些設定)
* HTTPS Server (看下面的ngrok)

#### Install Dependency  
事前安裝
```sh
pip3 install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

#### Secret Data

從developr頁面得到的token(xxx)要存好，不要給別人

```sh
export ACCESS_TOKEN=xxx
```

然後在需要的程式碼裡面打上這段來取得  
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

#### Run Locally
ngrok是一個可以將local端的server連到外面的辦法  
透過以下這段程式碼，可以得到https的網址，這個網址給別人，別人就可以跟local端互動
```sh
./ngrok http 5000
```

即使是要https，一樣是打http
5050為port，須跟程式碼裡設定一樣  
run(host="localhost", port=5000, debug=True, reloader=True)

#### Run the sever
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
(1)pp.py中一開始的webhook設定的token可以隨便打，跟FB developer設定一樣就好  
(2)可是utils.py中要send回去給messenger時，就需要用粉專的token(從FB developer的權杖產生取得)  
(3)資料夾中的demo只是練習(不完整)，無法跟messenger聯絡  
(4)FB developer要注意的地方
* 左邊的產品的勾勾都要是綠色
* 產品Messenger的設定的webhook要記得訂閱粉專(有時會有問題可以重新訂閱)
* 產品的Webhook記得是要選page，不是user。subscribe時的token設定看Note的(1)

