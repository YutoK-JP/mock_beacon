# Bluetooth疑似ビーコン
在室記録用（現状呉高専IWスクエア用）
# ディレクトリ構成
```
├──README.md            本ファイル

├──scannerbt.py         Bluetoothデバイスのスキャンを行うモジュールスクリプト（非実行用）

├──register.py          Bluetoothアドレス(mac) - 学籍番号(id)の登録用スクリプト
├──monitor.py           スキャン＆API実行を行う常駐用スクリプト

├──settings.json        API URLとスキャン間隔を記載
├──address-id.json      登録情報管理用のjsonファイル(上記２つによって自動生成)
```

# 使い方
## 共通事項
どちらのアプローチについても、monitor.xxを起動する前にsettings.jsonのGAS_URLを記載してください。
## リリースからの利用
1．リリース画面から `mock_beacon_v1.x.x.zip` をダウンロード <br>
2．zipファイルを適当なディレクトリに展開 <br>

== 学生番号登録 ==<br>
3-1．情報を登録する際は `register.exe` を起動 <br>
3-2．コンソール内で検索もしくは端末で調べたMACアドレスと学生番号を入力 <br>
3-\*． 初回起動時には自動で `address-id.json` が作成されます。 <br>

== スキャナー ==<br>
4-1．スキャナーを起動する際は `monitor.exe` を起動 <br>
4-2． `settings.json` の情報をもとにスキャンが実行されます。<br>
4-\*．　常駐させたい場合は `monitor.exe` をスタートアップに登録してください。

## pythonスクリプトからの利用
1．レポジトリをクローンもしくはzipをダウンロード後展開<br>
2．仮想環境をアクティベート後、 `pip install -r requirements.txt` を実行

== 学生番号登録 ==<br>
2-1．情報を登録する際は `register.py` を起動 <br>
2-2．コンソール内で検索もしくは端末で調べたMACアドレスと学生番号を入力 <br>
2-\*． 初回起動時には自動で `address-id.json` が作成されます。 <br>

== スキャナー ==<br>
4-1．スキャナーを起動する際は `monitor.py` を起動 <br>
4-2． `settings.json` の情報をもとにスキャンが実行されます。<br>
4-\*．　常駐させたい場合は `monitor.exe` をスタートアップに登録してください。

# 諸注意
・本プログラムではスマホのBluetoothMACアドレスを検索にかけており、BLE(Bluetooth Low Energy)を利用していません。よって、PCの同時デバイス接続数は7台に制限されています。<br>
・スキャンに正しく反応するためには、<br>
　　1.PC-スマホ間で接続が確立している<br>
　　2.スマホ側でデバイスの検索をかけている<br>
　のどちらかが成立している必要があります。接続数の制限もあり、環境によってはスキャンが正しく動作しない場合もあるのでご了承ください。

・登録前にスマホとPCのペアリングを完了させておくことを推奨します。（スキャンを正しく動作させるため）

# その他情報
実行ファイルの作成にはnuitka、実行ファイルのアイコンにはfontawsomeのアイコンを改変したものを利用しています。