# はんなりPython / Dash Hands On 20200319

### ハンズオン用リポジトリ

```
$ git clone https://github.com/hannari-python/dash_hands_on.git
$ cd dash_hands_on
$ python -m venv venv
$ pip install -r requirements.txt
もしくは
$ pip install dash dash_daq plotly pandas 
```

#### ファイルの実行

```
$ python first.py
```

``http://127.0.0.1:8050/`` にアクセスすると、アプリケーションが見れます。



## 方法その2 Dockerを使う方法

[Docker](https://www.docker.com/get-started)ページからインストーラーを使ってインストールしてください。  
他にもインストール方法があるので各自の環境に合わせてインストールしてください。  
`docker` コマンドが使える状態にしてください。


Dockerイメージを作成します。

```
$ docker build -t dash-handson .
```

Dockerコンテナを起動します。

```
$ docker run --rm -it -v $(pwd):/work -P -p 8050:8050 dash-handson python first.py
```

ブラウザでアクセスするとDashのページが表示されます。
[http://127.0.0.1:8050/](http://127.0.0.1:8050/)


