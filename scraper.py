import requests
from bs4 import BeautifulSoup
import re
import schedule
import time

# Function to fetch HTML content of a Twitter user's profile page.
def fetch_tweets(username):
    url = f"https://twitter.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve tweets for {username}")
        return ""


# Function to parse tweets from HTML content.
def parse_tweets(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tweets = soup.find_all('div', {'data-testid': 'tweet'})
    return [tweet.get_text() for tweet in tweets]


# Function to count the number of mentions of a stock symbol in a list of tweets.
def count_stock_mentions(tweets, stock_symbol):
    pattern = re.compile(rf'\${stock_symbol}')
    count = sum(1 for tweet in tweets if pattern.search(tweet))
    return count


# Function to continuously scrape Twitter accounts for mentions of a stock symbol at a given interval.
def scrape_twitter_accounts(usernames, stock_symbol, interval):
    print(f"Scraping for stock symbol '{stock_symbol}' every {interval} minutes.")
    while True:
        total_mentions = 0
        for username in usernames:
            html_content = fetch_tweets(username)
            if html_content:
                tweets = parse_tweets(html_content)
                mentions = count_stock_mentions(tweets, stock_symbol)
                total_mentions += mentions
                print(f"Account: {username} | Mentions: {mentions}")
        print(f"'{stock_symbol}' was mentioned '{total_mentions}' times in the last '{interval}' minutes.")
        time.sleep(interval * 60)

if __name__ == "__main__":
    usernames = [
        "Mr_Derivatives", 
        "warrior_0719",
        "ChartingProdigy",
        "allstarcharts",
        "yuriymatso",
        "TriggerTrades",
        "AdamMancini4",
        "CordovaTrades",
        "Barchart",
        "RoyLMattox"
    ]
    stock_symbol = input("Enter the stock symbol to look for (e.g., TSLA): ").strip()
    interval = int(input("Enter the time interval (in minutes) for another scraping session: ").strip())

    schedule.every(interval).minutes.do(scrape_twitter_accounts, usernames, stock_symbol, interval)

    while True:
        schedule.run_pending()
        time.sleep(1)
