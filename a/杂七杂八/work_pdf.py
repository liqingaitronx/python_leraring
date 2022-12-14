from win32com import client


# 转换doc为pdf
def doc2pdf(fn):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    print(word)
    # for file in files:
    doc = word.Documents.Open(fn)  # 打开word文件
    print(doc)

    doc.SaveAs("{}.pdf".format(fn[:-4]), 17)  # 另存为后缀为".pdf"的文件，其中参数17表示为pdf
    doc.Close()  # 关闭原来word文件
    word.Quit()


# 转换docx为pdf
def docx2pdf(fn):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    # for file in files:
    doc = word.Documents.Open(fn)  # 打开word文件
    doc.SaveAs("{}.pdf".format(fn[:-5]), 17)  # 另存为后缀为".pdf"的文件，其中参数17表示为pdf
    doc.Close()  # 关闭原来word文件
    word.Quit()


docx2pdf(r'C:\Users\EDY\Desktop\new_TEST\1.docx')
doc2pdf(r'C:\Users\EDY\Desktop\new_TEST\2.doc')
