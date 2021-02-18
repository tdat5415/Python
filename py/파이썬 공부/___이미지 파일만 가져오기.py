files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
picture =[i for i in files if i.find('.png') != -1 or i.find('jpg') != -1]
print(picture)
