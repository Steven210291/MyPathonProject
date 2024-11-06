"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        }
        
        response = requests.get(url, headers=header)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': "t-stripe"})
        d = {}
        male_total = 0
        female_total = 0
        # count = 0
        for tag in tags:
            lst = tag.text.split()
            for i in range(15, 200*5+1+10, 5):
                male_total += int(lst[i].replace(',', ''))
            for i in range(17, 200 * 5 + 1 + 15, 5):
                female_total += int(lst[i].replace(',', ''))
                # print(female_total)  # 檢查總數
                # count += 1
                # print(count)
            print(f'Male Number:{male_total}')
            print(f'Female Number:{female_total}')





if __name__ == '__main__':
    main()
