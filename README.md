# pdf-edition
For spliting or combining PDF files.


仮想環境を有効化
```source
.env/bin/activate
```

# installation
```pip 
install -r requirements.txt
```


# Usage
If you want to split several pdf files, put them directly under `/pdf`.
Execute `python split_pdf.py`.
Split files are generated under `/output/split/your_pdf_file/`.


If you want to combine several pdf files, make direcotry under `/split` (you can combine others files respectively.)
(The name of the directory becomes the generated file name.)
put combined files under `/split/your_combined_file_name/`.
Execute `python combine_pdf.py`
Combined files are generated under `/output/combine/`
