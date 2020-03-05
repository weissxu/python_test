# 设置表格样式
import json

import xlwt as xlwt


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font

    return style


# 写Excel

def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('学生', cell_overwrite_ok=True)
    row0 = ["商品名称", "商品原价", "实际售价", "商品链接", "商品图片", "店铺名称", "类目名称", "商品简称"]
    # 写第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))

    # lines = None
    with open('/Users/siwei/Documents/crawler/src/盖得1583132200.txt', 'r') as src:
        lines = src.readlines()
        num = 1
        for line in lines:
            item_dict = json.loads(line)

            sheet1.write(num, 0, item_dict['title'])
            sheet1.write(num, 1, item_dict['origPrice'])
            sheet1.write(num, 2, item_dict['actPrice'])
            sheet1.write(num, 3, item_dict['link'])
            sheet1.write(num, 4, item_dict['photoUrl'])
            sheet1.write(num, 5, item_dict['nick'])
            sheet1.write(num, 6, item_dict['catLeafName'])
            sheet1.write(num, 7, item_dict['shortTitle'])
            num = num + 1

    f.save('test.xls')


if __name__ == '__main__':
    write_excel()
