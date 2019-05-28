from bs4 import BeautifulSoup
from selenium import webdriver
import requests


def scrape(request, program):
    playlist = []
    base_url = 'https://zulu.id/program/%s/episode' % program

    # Request URL and Beautiful Parser
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_product = soup.find_all('div', class_="content-in ls-card NOTSET")
    # print(all_product)

    browser = webdriver.Chrome()
    for item in all_product:
        data = {}

        find_tag = item.find("a")
        # image = image.text.replace('\n', "").strip()
        url_video = find_tag['href']
        episode = int(find_tag['data-episode-no'])
        title = find_tag['data-label']
        # if 'https' in url_video:
        #     url_video = url_video.replace(
        #         "https://zulu.id/video/", request.base_url + "youtube/")
        # else:
        #     url_video = url_video.replace(
        #         "http://zulu.id/video/", request.base_url + "youtube/")
        data['episode'] = episode
        data['title'] = title
        data['img_url'] = item.find("img")['src']
        data['url_video'] = youtube(url_video, browser)

        playlist.append(data)
    browser.quit()
    return playlist


def youtube(link, browser):
    hasil_youtube = "http://zulu.id/video/" + link

    browser.get(link)
    soup = BeautifulSoup(browser.page_source, "lxml")
    hasil = soup.find_all('iframe')[0]['src']
    url_youtube = hasil.replace('embed', 'watch')
    result = url_youtube.split('?')

    return result[0]
