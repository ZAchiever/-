from docx import Document
document = Document('storage/合同.docx')


DICT = {
    "##托运公司填写处##": "new",
    '##地址##': '',
}


def check(document):
    # tables
    for table in document.tables:
        for row in range(len(table.rows)):
            for col in range(len(table.columns)):
                for key, value in DICT.items():
                    if key in table.cell(row, col).text:
                        print(key+"->"+value)
                        table.cell(row, col).text = table.cell(
                            row, col).text.replace(key, value)

    # paragraphs
    for para in document.paragraphs:
        for i in range(len(para.runs)):
            for key, value in DICT.items():
                if key in para.runs[i].text:
                    print(key+"->"+value)
                    para.runs[i].text = para.runs[i].text.replace(key, value)

    return document


print(check(document))
document.save('word1.docx')
