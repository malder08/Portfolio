# each month must change var month, invoiceNum, and column for times
import openpyxl
import os
from openpyxl.drawing.image import Image

os.getcwd()
os.chdir("C:\\Users\green\Python\Excel Auto\Four Star")

masterBook = openpyxl.load_workbook('FourStar Master File.xlsx')
masterSheet = masterBook['Sheet1']

invoice = openpyxl.load_workbook('Blank MLC Workbook.xlsx')
invoiceSheet = invoice['Service Invoice']

# counter (for the rows)
counter = 2

# starting invoice number
invoiceNum = 1326

# invoices to be made
invoicesToBeMade = 37

# add total number of invoices needed to be made to invoice number
invoiceCap = invoiceNum + invoicesToBeMade

while invoiceNum < invoiceCap:
    # collect all data
    month = 'September'
    address = masterSheet['A' + str(counter)].value
    times = masterSheet['D' + str(counter)].value
    rate = masterSheet['C' + str(counter)].value
    invoiceWriteNum = 'F' + str(invoiceNum)

    if times == 0:
        counter += 1
    else:
        # write invoice number
        invoiceSheet['D6'] = invoiceWriteNum

        # writing the address to the cell D9
        invoiceSheet['D9'] = address

        # write the address with other words to cell A17
        invoiceSheet['A17'] = 'Monthly Lawn Care: ' + month + ' 2018'

        # write number times to cell B17
        invoiceSheet['B17'] = times

        # write number times to cell B17
        invoiceSheet['C17'] = rate

        # insert GreenLand Logo
        logo = Image('GreenLand Small.png')
        invoiceSheet.add_image(logo, 'A1')

        # save the Workbook
        title = invoiceWriteNum + '. ' + str(address) + ' MLC.xlsx'
        invoice.save(title)

        counter += 1
        invoiceNum += 1
