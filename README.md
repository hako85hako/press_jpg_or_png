# press_jpg_or_png
targetファイル内に入れたjpgとpngを圧縮します。

## Dependency
python 3.7.4
Docker version 20.10.10

## Setup
Docker環境必須です。
exe化してませんので、コマンド叩いてください<br>
手順は以下 "Usage" です

## Usage
    
    \#git clone
    git clone https://github.com/hako85hako/press_jpg_or_png.git
    
    \#フォルダが作成される
    \#圧縮したい画像ファイルをtargetに格納
    
    \#docker
    #コンテナをビルド
    docker compose up -d --build
    
    \#コンテナに接続
    docker compose exec python3 bash

    \#フォルダ移動
    cd source
    
    \#実行
    python app.py

## License

## Authors
sakai

## References
url:https://create-it-myself.com/know-how/compress-png-and-jpeg-images-in-python/
