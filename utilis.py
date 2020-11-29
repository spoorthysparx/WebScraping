import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    """takes the url of the webpage and gets the contents of the page
    param url"""
    html=requests.get(url)
    return html.content

def parse_html_using_tag(html_content,tag):
    """gets all the paragraph contents from the page
    param html_content:contents of the page,tag:paragraphs"""
    soup=BeautifulSoup(html_content,"html.parser")
    data=[para.text for para in soup.find_all(tag)]
    return data