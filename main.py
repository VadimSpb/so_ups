import requests
import datetime
import time
from bs4 import BeautifulSoup as BS
from pprint import pprint
from logger import create_logger

def daterange(yearsdiff):
    """
    Returns date iterator
    :param yearsdiff int: years in int
    :return: dates between current date and carrent date - yeardiff
    """
    last_date = datetime.date.today()
    first_date = last_date.replace(year=last_date.year - yearsdiff)
    delta = last_date - first_date
    for i in range(delta.days):
        yield (first_date + datetime.timedelta(days=i)).strftime("%Y-%m-%d")

def get_dom(date):
    """
    Returns DOM-object
    :param date int: parametres for date
    :return:
    """
    url = 'https://www.so-ups.ru'
    suffix = '/functioning/ups/oes-center/oes-center-indicators/oes-center-gen-consump-hour/'
    params = {'tx_mscdugraph_pi%5Bcontroller%5D': 'Graph&tx_mscdugraph_pi%5Baction%5D=fullview',
              'tx_mscdugraph_pi%5BviewDate%5D': date}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0'}

    response = requests.get(url + suffix, params=params, headers=headers)
    logger.info(f"date = {date}, response status code:{response.status_code}")
    return BS(response.text, 'html.parser')

def so_ups_parser(dom):
    block = dom.find_all('div', attrs={'class': 'big-chart'})[0]
    times = block['data-datax'].split(',')
    generated = block['data-datay'].split(',')
    spent = block['data-datay1'].split(',')
    return times, generated, spent

logger = create_logger()
year_diff = 1

# запускаем
for date in daterange(year_diff):
    times, generated, spent = so_ups_parser(get_dom(date))
    if len(times) == len(generated) == len(spent):
        logger.info(f"date = {date} was parsed.")
    else:
        logger.warning(f"incorrect lenght. len(times) ={len(times)},  len(generated) ={len(generated)}, len(spent) = {len(spent)}")

    time.sleep(1)



