from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

from openpyxl.chart import BarChart, Reference