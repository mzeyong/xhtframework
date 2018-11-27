from bs4 import BeautifulSoup
import requests
import logging
import time

HEADERS = {}

PROXIES = {}

def Craw(url, headers=HEADERS, proxies=PROXIES, times=0):
    try:
        if times > 0:
            logging.error("try crawing {times} times -- {url}".format(times=times, url=url))
        logging.info("crawing -- {} --".format(url))
        result = requests.get(url, headers=headers, proxies=proxies)
        return result
    except Exception as error:
        if times < 3:
            time.sleep(0.5)
            return Craw(url, times=times + 1)
        return False

def Soup(content, soup_type="html5lib"):
    return BeautifulSoup(content, soup_type)

def tag_string(tag):
    return str(tag.string)

def tag_select(tag):
    return tag.select(tag)

def tag_attr(tag,attr):
    result = []
    for ele in tag:
        if hasattr(ele,"contents"):
            result.extend(tag_attr(ele,attr))
        if hasattr(ele,"attrs"):
            if ele.attrs.get(attr):
                result.append(ele.attrs[attr])
    return result

def tag_href(tag):
    return tag["href"]

def soup_tag(soup, tag):
    result = soup.find(tag)
    return result

def soup_tag_all(soup, tag):
    result = soup.find_all(tag)
    return result

def soup_class(soup, _class):
    result = soup.find(attrs={
        "class": _class
    })
    return result

def soup_class_all(soup, _class):
    result = soup.find_all(attrs={
        "class": _class
    })
    return result

def soup_tag_class_all(soup, tag, _class):
    result = soup.find_all(tag, attrs={
        "class": _class
    })
    return result

def soup_tag_class(soup, tag, _class):
    result = soup.find(tag, attrs={
        "class": _class
    })
    return result

def soup_tag_id(soup, tag, _id):
    result = soup.find(tag, attrs={
        "id": _id
    })
    return result

def soup_tag_id_all(soup, tag, _id):
    result = soup.find_all(tag, attrs={
        "id": _id
    })
    return result
