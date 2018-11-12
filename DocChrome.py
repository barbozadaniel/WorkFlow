def add_to_doc(text_string):    
    from docx import Document
    from docx.shared import Inches

    document = Document()
    p = document.add_paragraph(text_string)
    document.save('Word-SunHacks.docx')


def open_chrome(link):
    import string
    import webbrowser as wb
    link = link.lower();
    chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    wb.get(chromedir).open(link)
