from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 8번째 행의 7번 학생 데이터 삭제
# ws.delete_rows(8)

# 8번째 행의 3열 학생 데이터 삭제
ws.delete_rows(8, 3)

wb.save("sample_delete_row.xlsx")

ws.delete_cols(2) #2번째 열 (B) 삭제
wb.save("sample_delete_cols.xlsx")