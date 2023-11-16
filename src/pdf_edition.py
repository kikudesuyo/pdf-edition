import pypdf
from util import generate_path
from natsort import natsorted
import glob
import os

def split_pdf_file(raw_file):
  if not ".pdf" in raw_file:
    raise Exception("pdfファイル以外が含まれています")
  src_pdf = pypdf.PdfReader(raw_file)
  base_name = os.path.basename(raw_file)
  file_name, _ = os.path.splitext(base_name)
  if not os.path.exists(generate_path(f"/output/split/{file_name}")):
    os.mkdir(generate_path(f"/output/split/{file_name}"))
  for pdf_page, page in enumerate(src_pdf.pages):
    #コメントアウトの処理はpdf内に書かれているページ数を取
    # data = src_pdf.pages[pdf_page]
    # text = data.extract_text()
    # splited_file_name = text.split("\n")[0]
    splited_file_name = pdf_page+1
    dst_pdf = pypdf.PdfWriter()
    dst_pdf.add_page(page)
    dst_pdf.write(generate_path(f"/output/split/{file_name}/{splited_file_name}.pdf"))

def split_all_pdf_file():
  pdf_files = natsorted(glob.glob(generate_path("/pdf/*.pdf")))
  for pdf_file in pdf_files:
    split_pdf_file(pdf_file)

def combine_files(splited_files_directroy):
  dst_pdf = pypdf.PdfWriter()
  splited_files = natsorted(glob.glob(generate_path(f"/output/split/{splited_files_directroy}/*.pdf")))
  for splited_file in splited_files:
    if not ".pdf" in splited_file:
      raise Exception("pdfファイル以外が含まれています")
    dst_pdf.append(splited_file)
  combined_file_name = splited_files_directroy
  dst_pdf.write(generate_path(f"/output/combine/{combined_file_name}.pdf")) 

def combine_all_files():
  splited_files_directories = natsorted(os.listdir(generate_path("/output/split")))
  #should modify
  #そもそも.gitkeepがsplited_files_directoriesに含まれないようにする
  if ".gitkeep" in splited_files_directories:
    splited_files_directories.remove(".gitkeep")
  for splited_files_directroy in splited_files_directories:
    if not os.path.isdir(generate_path(f"/output/split/{splited_files_directroy}")):
      raise Exception("ディレクトリ以外が含まれています")
    combine_files(splited_files_directroy)
