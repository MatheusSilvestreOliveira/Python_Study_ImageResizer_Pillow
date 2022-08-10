from PIL import Image
import os


def resize(folder_path, new_width=720, tag='_RESIZED', new_folder_path=None):
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f'Error: {folder_path} is not a directory')

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Get old file name.
            full_file_path = os.path.join(root, file)
            file_name, file_extension = os.path.splitext(file)

            # Set up folder for the resized file, if exists.
            new_file_root = root
            if new_folder_path is not None and os.path.isdir(new_folder_path):
                new_file_root = new_folder_path

            # Set up new file name.
            new_file = file_name + tag + file_extension
            new_file_path = os.path.join(new_file_root, new_file)

            # Prevent overwriting existing file.
            if os.path.isfile(new_file_path):
                print(f'File named {new_file_path} already exists, try a different name.')
                continue

            # Prevent duplicate resized file.
            if tag in full_file_path:
                print(f'Image {full_file_path} is already resized.')
                continue

            # Use pillow to resize
            try:
                pillow = Image.open(full_file_path)
                width, height = pillow.size
                new_height = round((new_width * height) / width)
                img_resized = pillow.resize((new_width, new_height), Image.Resampling.LANCZOS)
                img_resized.save(new_file_path, optimeze=True, quality=70)

                print()
                print(f'{full_file_path} resized successfully.')
                print(f'File path : {new_file_path}')
                img_resized.close()
                pillow.close()
            except Exception as e:
                print()
                print(f'An error occurred in {full_file_path} and cannot be resized: -> {e}')
                print()


if __name__ == '__main__':
    # Fill with the folder with images you want to resize, as the example
    img_folder_path = 'C:\Images'

    # You may fill new_width= with your preffered width, default is 720
    # tag= with your preffered tag to name the new file, default is _RESIZED
    # new_folder_path= with the path you want your new file saved in, default is the same as img_folder_path
    resize(img_folder_path)
