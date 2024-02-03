import os


def check_is_pdf_file(file):
    if not ".pdf" in file:
        raise Exception("pdfファイル以外が含まれています")


def check_is_directory(file):
    if not os.path.isdir(file):
        raise Exception("ディレクトリ以外が含まれています")
