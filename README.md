# Pygames
test of pygames

## Discription
ライブラリを使ったPygamesのテスト用リポジトリ

## 環境構築
Python3.12 GUIが使えること（Pythonの公式からフルインストール）

仮想環境を準備する際は以下のコマンドで実施
```
#仮想環境作成
python3 -m venv games

#仮想環境をアクティベート
. games/bin/activate

#activateでエラーが出る場合実行権限付与
chmod 755 games/bin/activate

#仮想環境になった場合プロンプトが以下表示になる
(games) koharu-MacBook-Air %

#vsCodeで仮想環境を使用する場合はVsCode内でインタプリタからvenvを選択すること

```

pygameライブラリをインストール

```
pip install pygame

pip list

Package Version
------- -------
pip     24.2
pygame  2.6.0
```

