import win32com.client
import pyautogui as pg
import os

# 에스디메디칼 거래처 명
# 거래처명(에스디메디칼)
# company_names = ['씨엠지제약', '남산메디칼', '넥스팜', '뉴젠팜', '동광제약', 
#                 '마더스제약', '명문바이오', '에이치엘비제약', '삼성제약', '삼익제약',
#                 '신신제약', '쓰리에스파마', '위더스제약', '지오엠디', '제이스팜', 
#                 '한국넬슨', '한국파마', '원화약품', '에스지메디언스', '파마킹', '미래제약']

# 거래처명(에스비약품)
company_names = ['경수약품', '고려제약', '구주제약', '남산메디칼', '넥스팜', '뉴젠팜', 
                '대원제약', '동광제약', '동국제약', '창조약품', '명문바이오', '미래제약',
                '삼성제약', '삼익제약', '신신제약', '에이치엘비제약', '에이프로젠', '오스코리아',
                '위더스제약', '인베스트팜', '조아제약', '조은약품', '조인포스씨엠지', '지오엠디',
                '제이스팜', '한국넬슨', '한국코러스', '한국파마', '동흥약품주식회사']

PATH = 'Users\kwonkijun\Desktop\자동화\데이터'
excel = win32com.client.Dispatch("Excel.Application")

for company_name in company_names:    
    path = rf'C:\{PATH}\{company_name}.xls'
    # 파일이 존재 한다면 
    if(os.path.isfile(path)):
        workbook = excel.Workbooks.Open(path)

        sheet = workbook.Sheets('work')
        totalNum = 0

        try:
            for i in range(2, 5000):
                if(type(sheet.Range(f'D{i}').Value) != str):
                    totalNum = i
                    break;
        except IndexError:
            pass
        i = 3
        while i <= (totalNum - 1):
            print(i)
            if(sheet.Range(f'I{i}').Value == sheet.Range(f'I{i-1}').Value): # 이름이 같고
                if(sheet.Range(f'D{i}').Value == sheet.Range(f'D{i-1}').Value): # 날짜가 같다면
                    sheet.Range(f'K{i-1}').Value += sheet.Range(f'K{i}').Value # 수량 추가 *
                    sheet.Range(f'O{i-1}').Value += sheet.Range(f'O{i}').Value # 공급금액 추가 *
                    sheet.Range(f'P{i-1}').Value += sheet.Range(f'P{i}').Value # 세액금액 추가 *
                    sheet.Range(f'Q{i-1}').Value += sheet.Range(f'Q{i}').Value # 합계금액 추가 *
                    sheet.Rows(i).EntireRow.Delete() # 행 삭제 
                    totalNum = totalNum - 1
                else:
                    i = i + 1
            else:
                i = i + 1    
            
        workbook.SaveAs(rf'C:\{PATH}\{company_name}-data.xls')
        excel.quit()