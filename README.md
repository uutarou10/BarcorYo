# BarcorYo
バーコードでYoします。

…とは言っていますが実際にはキーボードから入力のあったIDのユーザーに対してYoを送信しているだけです。

## 必要環境
- Python3
  - requestsが必須
  
## 準備
- バーコードリーダーリーダーを用意します。
- ユーザーIDをバーコードに変換して印刷しておきます。
- あとは起動してバーコードを読めばOK
  - バーコードリーダーの設定で読み込み後改行を出力するように設定しておかないとEnterおさないといけなくて辛い。
