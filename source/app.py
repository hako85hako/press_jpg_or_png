from glob import glob
from io import BytesIO
from PIL import Image

import os


def app():

    # JPEG形式とPNG形式の画像ファイルを用意
    target_jpg_file_names = glob(f'target/*.jpg')
    target_png_file_names = glob(f'target/*.png')

    # コンフィグ
    COMPRESS_QUALITY = 30 # 圧縮のクオリティ

    #############################
    #     JPEG形式の圧縮処理     #
    #############################
    # ファイル名を取得
    for target_file_name in target_jpg_file_names:
        file_name = os.path.splitext(os.path.basename(target_file_name))[0]
        with open(target_file_name, 'rb') as inputfile:
            # バイナリモードファイルをPILイメージで取得
            im = Image.open(inputfile)
            # JPEG形式の圧縮を実行
            im_io = BytesIO()
            im.save(im_io, 'JPEG', quality = COMPRESS_QUALITY)
        with open('result/' + file_name + '-min.jpg', mode='wb') as outputfile:
            # 出力ファイル(result/*.jpg)に書き込み
            outputfile.write(im_io.getvalue())

    #############################
    #     PNG形式の圧縮処理      #
    #############################
    # ファイル名を取得
    for target_png_file_name in target_png_file_names:
        file_name = os.path.splitext(os.path.basename(target_png_file_name))[0]
        with open(target_png_file_name, 'rb') as inputfile:
            # バイナリモードファイルをPILイメージで取得
            im = Image.open(inputfile)
            # JPEG形式に変換して、圧縮を実行
            im = im.convert('RGB')
            im_io = BytesIO()
            im.save(im_io, 'JPEG', quality = COMPRESS_QUALITY)
        with open('result/' + file_name + '-min.jpg', mode='wb') as outputfile:
            # 出力ファイル(result/*.png)に書き込み
            outputfile.write(im_io.getvalue())



if __name__=="__main__":
    app()