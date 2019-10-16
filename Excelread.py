import xlrd 
    #Open and read an Excel file
row=0
col=0 
k=int(0)
ch=str("Mukundan")
book = xlrd.open_workbook("/Users/mukundanramesh/Downloads/Financial Sample.xlsx")
 
    # print number of sheets
#print book.nsheets
 
    # print sheet names
#print("\n")
#print book.sheet_names()
 
    # get the first worksheet
#print("\n")
first_sheet = book.sheet_by_index(0)
second_sheet=book.sheet_by_index(1)
 
    # read a row
#print("\n")
#print first_sheet.row_values(1)
 
    # read a cell
print("\n")
for row in range(5):
    #print ('ROW: %d' % (row))
    for col in range(2):
        #print ('COL: %d' % (col))
        cell = second_sheet.cell(row,col)
        cell1 = str(cell.value)
        #print(cell1)
        if cell1 == ch:
            k=col+1
            print("\n")
            cell2=first_sheet.cell(row,k)
            print ('ROW: %d' % (row))
            #print("\n")
            print ('COL: %d' % (col))
            #print("\n")
            print (cell.value)
            print (cell2.value)
        
        
 
    # read a row slice
#print first_sheet.row_slice(rowx=0,start_colx=0,end_colx=2)