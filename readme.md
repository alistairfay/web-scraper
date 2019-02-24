# requirements

## option 1 - python
python3 with 
beautiful soup and requests

## option 2 - container
container runtime (docker) and access to docker hub

# how to run

## option 1 - python
call the script via python3

e.g.

`python3 scraper.py`

## option 2 - container

`docker run alistairfay/web-scraper:0.1`

output will be saved to site_map.txt

# reasoning

selected python as there are several libraries for crawling and parsing web content

hands on python has been on my todo list for a while and a practical challenge is a great way to pick up some skills

longer than expected was taken to get to grips with the basics of python and parsing web requests and as such no time has been spent packaging up in to a format such as a docker image.  as such the requirement to 

# todo

- multi threading
- input and validation
- error handling