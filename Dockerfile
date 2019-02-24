FROM python:3

ADD scraper.py /

RUN pip3 install beautifulsoup4 requests

CMD [ "python3", "./scraper.py" ]