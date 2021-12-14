import os
from urllib.request import urlopen

def download_data(stock_symbol):
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'+stock_symbol+'?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'
    file_name = stock_symbol+'.csv'
    local_path = os.path.join('data', file_name)
    with urlopen(url) as file, open(local_path, 'wb') as f:
        f.write(file.read())

def get_csv_files(dir_path):
    files_list = os.listdir(dir_path)
    csv_files = []
    project_folder = os.path.abspath('')
    for file in files_list:
        if file.endswith('.csv'):
            csv_files.append(os.path.join(project_folder, 'data', file))
    return csv_files

def process_csv(file_name):
    processed_data = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        header = lines.pop(0)
        processed_data.append(header.strip().split(',') + ['Change'])
        for line in lines:
            stock_data = line.strip().split(',')
            op, cp = float(stock_data[1]), float(stock_data[4])
            pct_change = round(((cp - op)/op)*100, 2)
            stock_data.append(str(pct_change))
            processed_data.append(stock_data)
        return processed_data

def write_csv(file_name, write_data):
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'a') as f:
        for data in write_data:
            f.write(','.join(data)+'\n')

if __name__ == '__main__':
    stock_symbols = ['GOOG', 'IBM', 'MSFT']
    for stock_symbol in stock_symbols:
        download_data(stock_symbol)
    for csv_file in get_csv_files('./data'):
        write_csv(csv_file, process_csv(csv_file))

# get_csv_files('./data')

# process_csv('C:/Users/HP/PycharmProjects/PythonHomework/data/MSFT.csv')


