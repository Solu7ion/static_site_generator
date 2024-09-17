import os
import shutil
from textnode import *

def copy_static_files(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.makedirs(dest_dir, exist_ok=True)

    # Рекурсивно скопируем все файлы и поддиректории
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        # Если это файл, копируем его
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} -> {dest_path}")
        # Если это директория, рекурсивно копируем её содержимое
        elif os.path.isdir(source_path):
            copy_static_files(source_path, dest_path)

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.def")
    print(node)

    source_directory = "static"
    destination_directory = "public"
    copy_static_files(source_directory, destination_directory)

if __name__ == "__main__":
    main()
