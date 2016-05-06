# Created by Daniel Wright (c16612)

import xlsxwriter

def entry():
    global fh
    global fname
    fname = raw_input('Name of text file you wish to convert (include .txt): ')
    fh = open(fname)

def outfile():
    global output
    global workbook
    global worksheet
    output = raw_input('Name of output Excel file (include .xlsx): ')
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

def parse():
    global row
    global col
    global i
    global dataflag
    global passcount
    global failcount

    for lines in fh:
        col = 0
        line = lines.replace("\t", " ")
        words = line.split()

        # Extract desired data, only excutes if words is NOT blank
        #if words:
            #print words

        for elements in words:
            if elements == "PASS" or elements == "P":
                passcount = passcount + 1
            if elements == "FAIL" or elements == "F":
                failcount = failcount + 1

            # Eliminate empty rows in text file that leads to empty lists
            if i < len(elements):
                #if elements[0].isdigit() or elements.startswith('-') is True:
                #    elements = float(elements)
                worksheet.write(row, col, elements)
                col = col + 1

        if len(words) < 1:
            continue
        row = row + 1


    prompt = raw_input("Type any key and press enter to convert another file. Press Enter to exit. ")
    if prompt:
        entry()
        parse()

# Initialize variables
row = 0
i = 0
dataflag = 0
passcount = 0
failcount = 0
device = []
measure = []

entry()
outfile()
parse()

workbook.close()

testpoints = passcount + failcount

print "COMPLETE"
print "Total test points: ", testpoints
print "Test result pass: ", passcount
print "Test result fail: ", failcount
