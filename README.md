# SimpleMemo

勉強会用Flaskウェブアプリ。

## 必須プログラム、ライブラリ
* Python3
* Flask
* Sqlite3

OSはCent OS7を想定。

## インストール

### 必要なOSパッケージをインストール
```
yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel
```
### pyenvのインストール
```
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

.bashrcに設定を書き込む

```
$ echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ source ~/.bashrc
$ pyenv -v
```

### Pythonをコンパイル
```
$ pyenv install 3.6.1
```

SimpleMemoディレクトリにcdして実行するPythonのバージョンを指定する。

```
$ cd simple-memo
$ pyenv local 3.6.1
```

### Pythonライブラリインストール
```
$ pip install flask sqlite3
```
## 実行
```
$ python app.py
```

ブラウザでhttp://localhost:3000にアクセスする。
