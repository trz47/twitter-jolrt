# twitter-jolrt

Twitterで利用路線のみのジョルダンライブツイートをRTするプログラム

Python 3.6.6 で動作確認

## 使い方

### Gitを使って設置し、仮想環境を作成して動作させる手順

まず、[こちら](https://apps.twitter.com/)よりアプリ作成しキーを取得

configディレクトリ内の二つの設定ファイルを編集

1. アプリ作成した際に取得したキーをkey.json.sampleに入力し、ファイル名をkey.jsonに変更
1. 監視したい路線名をlines.json.sampleに入力し、ファイル名をlines.jsonに変更

Python仮想環境を以下のコマンドで作成（詳しくは[ここ](https://docs.python.jp/3/library/venv.html)とか[ここ](https://docs.python.jp/3/tutorial/venv.html)とかを参照）

```bash
python3 -m venv venv    # 仮想環境作成
source venv/bin/activate    # 仮想環境に入る
pip install -r requirements.txt # 必要なパッケージをインストール
deactivate  # 仮想環境から抜ける
```

以上で、設置と仮想環境構築は完了

以下のコマンドで実行できる。

```bash
venv/bin/python main.py
```

これをcronなどに登録しておいて自動実行できるようにすればい。