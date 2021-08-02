import requests
from bs4 import BeautifulSoup as bs
import time

#html = requests.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={locations}+%EB%82%A0%EC%94%A8")
#soup = bs(html.content, 'html.parser')

def current_location(locations):

    html = requests.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={locations}+%EB%82%A0%EC%94%A8")
    soup = bs(html.content, 'html.parser')
    data1 = soup.find('div', {'class': 'weather_box'})
    find_address = data1.find('span', {'class':'btn_select'}).text
    return find_address
def current_weather(locations):
    html = requests.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={locations}+%EB%82%A0%EC%94%A8")
    soup = bs(html.content, 'html.parser')
    data1 = soup.find('div', {'class': 'weather_box'})
    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
    return find_currenttemp
def current_fdust(locations):
    html = requests.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={locations}+%EB%82%A0%EC%94%A8")
    soup = bs(html.content, 'html.parser')
    data1 = soup.find('div', {'class': 'weather_box'})
    data2 = data1.findAll('dd')
    find_dust = data2[0].find('span', {'class':'num'}).text
    return find_dust
def current_ufdust(locations):
    html = requests.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={locations}+%EB%82%A0%EC%94%A8")
    soup = bs(html.content, 'html.parser')
    data1 = soup.find('div', {'class': 'weather_box'})
    data2 = data1.findAll('dd')
    find_ultra_dust = data2[1].find('span', {'class':'num'}).text
    return find_ultra_dust
def current_ozoneindex(locations):
    html = requests.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={locations}+%EB%82%A0%EC%94%A8")
    soup = bs(html.content, 'html.parser')
    data1 = soup.find('div', {'class': 'weather_box'})
    data2 = data1.findAll('dd')
    find_ozone = data2[2].find('span', {'class':'num'}).text
    return find_ozone