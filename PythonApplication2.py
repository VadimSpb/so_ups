import urllib.request
from datetime import date, timedelta
import re
import csv

addr = "https://www.so-ups.ru/functioning/ups/oes-center/oes-center-indicators/oes-center-gen-consump-hour/?tx_mscdugraph_pi%5Bcontroller%5D=Graph&tx_mscdugraph_pi%5Baction%5D=fullview&tx_mscdugraph_pi%5BviewDate%5D={}"

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2021, 9, 2)
end_date = date(2022, 9, 2)

with open('output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['date', "consume", "produce"])

    for single_date in daterange(start_date, end_date):
        iterDate = addr.format(single_date.strftime("%Y-%m-%d"))
        with urllib.request.urlopen(iterDate) as f:
            html = f.read().decode('utf-8')
            datax = re.search(r'data-datax="(.*?)"', html).group(1).split(',')
            datay = re.search(r'data-datay="(.*?)"', html).group(1).split(',')
            datay1 = re.search(r'data-datay1="(.*?)"', html).group(1).split(',')
            for i in range(0, len(datax)):
                csvwriter.writerow([datax[i], datay[i], datay1[i]])