import glob
import os

import pypdf
from natsort import natsorted

from helper.file_relation import check_is_directory, check_is_pdf_file
from util import generate_path


class PdfSplitter:
    def __init__(self, original_file):
        check_is_pdf_file(original_file)
        self.src_pdf = pypdf.PdfReader(original_file)
        base_name = os.path.basename(original_file)
        self.file_name, _ = os.path.splitext(base_name)
        if not os.path.exists(generate_path(f"/output/split/{self.file_name}")):
            os.mkdir(generate_path(f"/output/split/{self.file_name}"))

    def get_desiginated_page(self, page_number):
        page = self.src_pdf.pages[page_number]
        dst_pdf = pypdf.PdfWriter()
        dst_pdf.add_page(page)
        dst_pdf.write(
            generate_path(f"/output/split/{self.file_name}/{page_number}.pdf")
        )

    def split_pdf_file(self):
        for pdfpage, _ in enumerate(self.src_pdf.pages):
            self.get_desiginated_page(pdfpage)


class PdfCombiner:
    def __init__(self, abs_combined_dir):
        self.file_name = os.path.basename(abs_combined_dir)
        self.dst_pdf = pypdf.PdfWriter()
        self.splited_files = natsorted(glob.glob(f"{abs_combined_dir}/*.pdf"))
        for splited_file in self.splited_files:
            check_is_pdf_file(splited_file)
            self.dst_pdf.append(splited_file)

    def combine_files(self):
        self.dst_pdf.write(generate_path(f"/output/combine/{self.file_name}.pdf"))


def split_all_pdf_file():
    pdf_files = natsorted(glob.glob(generate_path("/pdf/*.pdf")))
    for pdf_file in pdf_files:
        instance = PdfSplitter(pdf_file)
        instance.split_pdf_file()


def combine_all_files():
    split_dir_element = natsorted(os.listdir(generate_path("/output/split")))
    if ".gitkeep" in split_dir_element:
        split_dir_element.remove(".gitkeep")
    for splited_files_directroy in split_dir_element:
        abs_combined_dir = generate_path(f"/output/split/{splited_files_directroy}")
        check_is_directory(abs_combined_dir)
        instance = PdfCombiner(abs_combined_dir)
        instance.combine_files()
