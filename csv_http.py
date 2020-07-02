import urllib.request
import requests
import csv
import re

"""
We have this CSV (https://raw.githubusercontent.com/akshayknarayan/alexa/master/top500.csv)
with information about the Top500 most visited sites.
We want to create a new CSV that contains the same first two columns as top500.csv,
but also contains these columns:
Number of bytes in HTTP response body
HTTP response status
Number of email addresses in HTTP response body. Use a regular expression to
match against the HTTP response body and find all emails, then count them.
"""


def main():
    get_csv()
    process_file()


def get_csv():
    url = 'https://raw.githubusercontent.com/akshayknarayan/alexa/master/top500.csv'
    urllib.request.urlretrieve(url, './top500.csv')


def parse_line(row):
        domain = row[0]
        http_url = row[1]
        req_result = requests.get(row[1])
        nbytes = len(req_result.content)
        status = req_result.status_code
        pattern = r'[\w\.-]+@[\w\.-]+[\w\.-]'
        emailfound = re.findall(pattern, str(req_result.content))
        result_line = [domain, http_url, str(nbytes), str(status), str(emailfound).strip()]
        return(result_line)


def process_file():
    with open('./top500.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for line in spamreader:
            parsed_line = parse_line(line)
            print(parsed_line[0] + ', ' + parsed_line[1] + ', ' + parsed_line[2] + ', ' + parsed_line[3] + ', ' + parsed_line[4])


if __name__ == '__main__':
    main()
