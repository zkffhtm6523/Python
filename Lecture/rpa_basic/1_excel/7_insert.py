from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 행 삽입
# ws.insert_rows(8)
# 8번째 줄 위치에 5줄 행삽입
ws.insert_rows(8, 5)
wb.save("sample_insert_rows.xlsx")

ws.insert_cols(2) # B번째 열 삽입
ws.insert_cols(2, 3) # B번째 3칸 열 삽입
wb.save("sample_insert_cols.xlsx")
