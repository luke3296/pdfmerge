import os.path
import PyPDF4
import getopt, sys
output_name = ''
pdf_list = []

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "ho:"

# Long options
long_options = ["Help", "Output"]

try:
# Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
# checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--Help"):
            print("usage: pdfmerge -o output_name pdf1 pdf2 ...")
            print("usage: pdfmerge pdf1 pdf2 ...")
        elif currentArgument in ("-o", "--Output"):
            output_name = currentValue
except getopt.error as err:
        print (str(err))


if output_name != '':
    idx = argumentList.index("-o")
    pdf_list = argumentList[idx+2:]
else:
    pdf_list = argumentList
    output_name = 'merged.pdf'

print(pdf_list)

merger = PyPDF4.PdfFileMerger(strict=False)

for file in pdf_list:
    currentDir = os.getcwd() + "\\"
    file_exists = os.path.exists(file)
    if file_exists:
        merger.append(fileobj=open(file, 'rb'))

merger.write(fileobj=open(output_name, 'wb'))
merger.close()