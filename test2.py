import os
from openpyxl import load_workbook   # Module needed for loading existing workbook

os.system('copy BOM_Blank.xlsx BOM.xlsx')
wb = load_workbook(filename="BOM.xlsx")
ws = wb.active

# Save the spreadsheet
wb.save(filename="BOM.xlsx")

layers = ['induknya::Layer 02', 'Layer 04']
print(layers)
layertobom = []
for layer in layers:
    nama = layer
    cari = ':'
    index = nama.rfind(cari)
    if index >= 0:
        #slice disini
        index = index+1
        layertobom.append(nama[index:len(nama)])
    else:
        layertobom.append(nama)
print(layertobom)
