import requests 
import re
n = input("What do you want for web scraping?")
youtube_search_url = "http://www.youtube.com/results?search_query=" # The youtube URL to the search query
youtube_video_url = "http://www.youtube.com/watch?v=" # The basic youtube URL
r = requests.get(url=youtube_video_url)
def search(query):
    r = requests.get(youtube_search_url + query.replace(" ","+"))
    ids = re.findall(r"watch\?v=(\S{11})\"", r.text) # Check this line
    url = youtube_video_url + ids[0]
    print(url)
search(n)

