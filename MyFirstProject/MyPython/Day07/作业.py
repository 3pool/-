import xlrd
import xlwt

myBook = xlrd.open_workbook('公司1-2月数据.xls')
sheet1 = myBook.sheets()[0]
sheet2 = myBook.sheets()[1]
rows1 = sheet1.nrows
rows2 = sheet2.nrows
list_orderid = []

for row1 in range(1,rows1):
    list_orderid.append(sheet1.cell(row1,0).value)

for row2 in range(1,rows2):
    list_orderid.append(str(int(sheet2.cell(row2,0).value)))

newBook = xlwt.Workbook()
newBook = xlwt.Workbook()
newSheet = newBook.add_sheet('订单号码')
newSheet.write(0,0,'订单号码')

for iRow in range(len(list_orderid)):
    newSheet.write(iRow+1,0,list_orderid[iRow])
newBook.save('订单.xls')

