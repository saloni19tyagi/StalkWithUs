from bs4 import BeautifulSoup
import requests

def recentactivity():

    user = "vandita_1081"   #codeforces handle
    URL = 'https://codeforces.com/submissions/{}'.format(user)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('tr')

    # Format
    # Problem name               Problem Link               Submission Time            Submitted Code

    for tr in results:
        if len(tr.find_all('td')) > 3:
            print("".join(tr.find_all('td')[3].a.text.split()))
            print("https://codeforces.com{}".format(tr.find_all('td')[3].a['href']))
            print(tr.find_all('td')[1].text.strip("\n"))
            print("https://codeforces.com/contest/1395/submission/{}".format(tr.find_all('td')[0].a.text))


recentactivity() 