import os

def get_filename_without_extension(abs_path):
    base_name = os.path.basename(abs_path)
    file_name, _ = os.path.splitext(base_name)
    return file_name

# 使用例
raw_file = "/path/to/your/file/example.txt"
file_name = get_filename_without_extension(raw_file)
print(file_name)