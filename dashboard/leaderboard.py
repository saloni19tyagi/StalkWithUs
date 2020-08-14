from bs4 import BeautifulSoup
import requests
# from models leaderboard
from dashboard.models import leaderboard

def createLeaderBoard():

    URL = 'https://codeforces.com/ratings'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('table')
    results = results.tbody.find_all('tr')

    for tr in results:
        if len(tr.find_all('td'))>2:
            name = tr.find_all('td')[1].text
            rating = tr.find_all('td')[2].text
            # link = ("https://codeforces.com"+tr.find_all('td')[1].a['href'])
            # print(name)
            # print(rating)
            # print()
            lead = leaderboard.objects.filter(username = name)
            if not lead.exists():
                leader = leaderboard(username=name, rating=rating)
                leader.save()

            print()

createLeaderBoard()