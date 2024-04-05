import os
from PIL import Image
import tifffile

def collect_and_save_tiff(folder_list, output_filename="Result.tif"):
    images = []
    for folder in folder_list:
        for filename in os.listdir(folder):
            if filename.lower().endswith('.png'):
                filepath = os.path.join(folder, filename)
                try:
                    images.append(Image.open(filepath))
                except Exception:
                    print(f"Ошибка при обратботке картинки: {filepath}")

    if images:    
        tifffile.imwrite(output_filename, images, compression='lzw')
        print(f"TIFF файл сохранен как: {output_filename}")
    else:
        print("PNG картинки не были найдены в данных директориях")

folder_list = ['1388_12_Stickers 3-D_3'] 
collect_and_save_tiff(folder_list)
