# change invoiceNum and invoicesToBeMade
import win32com.client
import openpyxl
import os

os.getcwd()
os.chdir("C:\\Users\green\Python\Excel Auto\Four Star")

masterBook = openpyxl.load_workbook('FourStar Master File.xlsx')
masterSheet = masterBook['Sheet1']

invoiceNum = 1326
invoicesToBeMade = 37
invoiceCap = invoiceNum + invoicesToBeMade
counter = 2

while invoiceNum < invoiceCap:
    # get address
    address = masterSheet['A' + str(counter)].value

    # save the workbook as pdf
    o = win32com.client.Dispatch("Excel.Application")

    o.Visible = False

    invoiceTitle = 'F' + str(invoiceNum) + '. ' + address + ' MLC'
    path = 'C:\\users\green\Python\Excel Auto\Four Star\\'
    wb_path = path + invoiceTitle + '.xlsx'

    wb = o.Workbooks.Open(wb_path)

    ws_index_list = [1]

    pathToPdf = path + invoiceTitle + ' .pdf'

    wb.WorkSheets(ws_index_list).Select()

    wb.ActiveSheet.ExportAsFixedFormat(0, pathToPdf)

    invoiceNum += 1
    counter += 1
