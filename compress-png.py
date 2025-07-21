# 壓縮圖片
# 此工具使用了 Pillow，請先安裝：pip install Pillow

import os
from PIL import Image

def compress_png(input_path, output_path, reduce_colors=True):
    img = Image.open(input_path)

    if reduce_colors:
        img = img.convert("P", palette=Image.ADAPTIVE)

    img.save(output_path, format="PNG", optimize=True)

    original_size = os.path.getsize(input_path) / 1024
    compressed_size = os.path.getsize(output_path) / 1024
    saved_percent = 100 * (original_size - compressed_size) / original_size

    print(f"✅ {os.path.basename(input_path)} 壓縮完成：{original_size:.1f}KB → {compressed_size:.1f}KB（↓ {saved_percent:.1f}%）")

def compress_png_folder(input_folder, output_folder, reduce_colors=True):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(input_folder) if f.lower().endswith(".png")]
    if not files:
        print("沒有找到PNG檔案")
        return

    for filename in files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        compress_png(input_path, output_path, reduce_colors)

if __name__ == "__main__":
    # 修改這裡的路徑
    input_folder = input("請輸入原始圖片資料夾路徑：")
    output_folder = input("請輸入輸出資料夾路徑：")
    
    reduce_colors = True

    compress_png_folder(input_folder, output_folder, reduce_colors)
