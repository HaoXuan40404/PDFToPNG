import sys, fitz
import os
import datetime

def pyMuPDF_fitz(pdfPath, imagePath):

    print("imagePath="+imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        zoom_x = 2 #(1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):
            os.makedirs(imagePath)

        pix.writePNG(imagePath+'/'+'images_%s.png' % pg)#将图片写入指定的文件夹内

if __name__ == "__main__":
    pdfPath = './chapter1.pdf'
    imagePath = './images/chapter1/'
    pyMuPDF_fitz(pdfPath, imagePath)