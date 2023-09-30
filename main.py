import csv
import numpy as np
import pandas as pd
with open("npo_clnts.csv", "r", encoding='utf-8') as f:
    reader_1 = csv.reader(f)
    with open("npo_cntrbtrs.csv", "r", encoding='utf-8') as f:
        reader_2 = csv.reader(f)
        with open("npo_trnsctns.csv", "r", encoding='utf-8') as f:
            reader_3 = csv.reader(f)
            with open("inflyciy.csv", "r", encoding='utf-8') as f:
                reader_4 = csv.reader(f)

npo_clnts = pd.read_csv('npo_clnts.csv', delimiter=',')
npo_cntrbtrs = pd.read_csv('npo_cntrbtrs.csv', delimiter=',')
npo_trnsctns = pd.read_csv('npo_trnsctns.csv', delimiter=',')
inflyciy = pd.read_csv('inflyciy.csv', delimiter=',')



cl_id = str(input())
ac_id = str

cl_id_data = npo_clnts[npo_clnts.isin([cl_id]).any(axis= 1 )]
ac_id_data = npo_cntrbtrs[npo_cntrbtrs.isin([cl_id]).any(axis= 1 )]
ac_id = ac_id_data.iloc [0]['npo_accnt_id']
npo_trnsctns_data = npo_trnsctns[npo_trnsctns.isin([ac_id]).any(axis= 1 )]
with open("data1.csv",'w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow([cl_id_data])
with open("data2.csv",'w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow([ac_id_data])
    with open("data3.csv", 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([npo_trnsctns_data])

data1 = pd.read_csv('data1.csv', delimiter=',')
data2 = pd.read_csv('data2.csv', delimiter=',')
data3 = pd.read_csv('data3.csv', delimiter=',')



























