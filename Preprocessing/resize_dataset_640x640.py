import os
import shutil
from PIL import Image
from pathlib import Path

input_dir = Path(r"C:/test/datasets/resize")
output_dir = Path(r"C:/test/processed_640x640")

# Создаем выходную папку, если её нет
output_dir.mkdir(exist_ok=True)

# Поддерживаемые форматы изображений
image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}

processed_count = 0


for file_path in input_dir.iterdir():
    if file_path.is_file() and file_path.suffix.lower() in image_extensions:
        try:
            with Image.open(file_path) as img:
                # Проверяем размер
                if img.size != (640, 640):
                    img = img.resize((640, 640), Image.Resampling.LANCZOS)

                output_path = output_dir / f"{processed_count+1:05d}.jpg"
                img.save(output_path, 'JPEG', quality=95, optimize=True)
                processed_count += 1
        except Exception as e:
            print(f"Ошибка при обработке {file_path.name}: {str(e)}")

print(f"Обработано файлов: {processed_count}")
print(f"Файлы сохранены в: {output_dir}")