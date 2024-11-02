import os
from pdf2docx import Converter

def pdf_to_word(pdf_file,word_file):
    if not os.path.exists(pdf_file):
        print("The pdf file {pdf_filr} does not find")
        return
    try:
        # create a pdf to converter object
        converter_data = Converter(pdf_file)
        # convert to pdf to word
        converter_data.convert(word_file,start=0,end=None)

        # close the converter
        converter_data.close()
        print("Successfully converted")
    except Exception as e:
        print("error :{e}")

pdf_file_path='demo.pdf'
word_file_path='output_file.docx'

pdf_to_word(pdf_file_path,word_file_path)


        