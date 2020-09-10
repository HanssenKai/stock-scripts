# pip install BeautifulSoup - > for parse the html and find all url hrf with ".pdf" final
from PyPDF2 import PdfFileReader
import io


def main():
    fd = open("AA200504.pdf", "rb")    
    pdf = PdfFileReader(fd)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    txt = f"""
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """
    # Here the metadata of your pdf
    print(txt)
    # numpage for the number page
    numpage=8
    page = pdf.getPage(numpage)
    page_content = page.extractText()
            
    print(page_content)
    fd.close()

if __name__ == "__main__":
    main()