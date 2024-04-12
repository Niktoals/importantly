from PIL import Image
from PIL.ExifTags import TAGS
import argparse

def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i", "--image", dest="image", help="Image to check")
    options=parser.parse_args()
    return options

# Функция для удаления метаданных из указанного изображения.
def clear_all_metadata(img_name):
    # Открываем файл изображения.
    img = Image.open(img_name)

    # Читаем данные изображения, исключая метаданные.
    data_i = list(img.getdata())
    data_t=img.getexif()

    if len(data_t)!=0:
        print('It have metas')
        for tag_id in data_t:
            tag=TAGS.get(tag_id, tag_id)
            data=data_t.get(tag_id)
            if isinstance(data, bytes):
                data=data.decode()
            print(f'{tag:20}: {data}')    
        # Создаем новое изображение с тем же режимом и размером, но без метаданных.
        img_without_metadata = Image.new(img.mode, img.size)
        img_without_metadata.putdata(data_i)

        # Сохраняем новое изображение поверх исходного файла, удаляя метаданные.
        img_without_metadata.save(img_name)

        print(f"Метаданные успешно удалены из '{img_name}'.")

    else:
        print("Can't find metas")

if __name__ == "__main__":
    options=get_args()
    scan_result=clear_all_metadata(options.image)