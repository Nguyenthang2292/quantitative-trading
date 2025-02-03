import requests
from bs4 import BeautifulSoup
import yfinance as yf
import csv
import os

# Hàm crawl danh sách các công ty từ Wikipedia
def crawl_sp500_companies():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'constituents'})
        
        if table:
            tbody = table.find('tbody')
            if tbody:
                rows = tbody.find_all('tr')
                companies = []
                
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    cell_data = [cell.get_text(strip=True) for cell in cells]
                    
                    # Lấy symbol (cột đầu tiên) và tên công ty (cột thứ hai)
                    if len(cell_data) > 1:  # Bỏ qua hàng tiêu đề nếu cần
                        symbol = cell_data[0]
                        name = cell_data[1]
                        companies.append((symbol, name))
                
                return companies
            else:
                print("Không tìm thấy thẻ <tbody> trong bảng.")
        else:
            print("Không tìm thấy bảng có id='constituents'.")
    else:
        print(f'Không thể truy cập trang web. Mã lỗi: {response.status_code}')
    
    return []

# Hàm tải dữ liệu từ yfinance và lưu vào file CSV
def download_stock_data(symbol, start_date, end_date):
    try:
        # Tải dữ liệu từ yfinance
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        
        if not stock_data.empty:
            # Tạo thư mục nếu chưa tồn tại
            if not os.path.exists('stock_data'):
                os.makedirs('stock_data')
            
            # Lưu dữ liệu vào file CSV
            file_path = f'stock_data/{symbol}.csv'
            stock_data.to_csv(file_path)
            print(f'Dữ liệu của {symbol} đã được lưu vào {file_path}')
        else:
            print(f'Không có dữ liệu cho {symbol} trong khoảng thời gian này.')
    except Exception as e:
        print(f'Lỗi khi tải dữ liệu cho {symbol}: {e}')

# Hàm main
def main():
    # Crawl danh sách các công ty từ Wikipedia
    companies = crawl_sp500_companies()
    
    if not companies:
        print("Không tìm thấy danh sách công ty. Kết thúc chương trình.")
        return
    
    # Thời gian bắt đầu và kết thúc
    start_date = '2018-01-01'
    end_date = '2022-12-31'
    
    # Tải dữ liệu cho từng công ty
    for symbol, name in companies:
        print(f'Đang tải dữ liệu cho {name} ({symbol})...')
        download_stock_data(symbol, start_date, end_date)

# Điểm khởi đầu của chương trình
if __name__ == '__main__':
    main()