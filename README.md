Twitter Stock Mention Scraper

This project is a Python tool that scrapes Twitter accounts for mentions of stock symbols, without using the Twitter API. The tool takes a list of Twitter accounts, a stock ticker symbol, and a time interval as input, and outputs the number of times the stock symbol was mentioned within that interval.

Table of Contents
Introduction
Features
Requirements
Installation
Usage
Example Output
Project Structure
Contributing
License
Introduction
This tool is designed for Geek Labs' Backend Developer internship task. It scrapes Twitter accounts for stock symbol mentions and displays the count at specified intervals.

Features
Scrapes a list of Twitter accounts for stock symbol mentions.
Counts and displays the number of mentions at specified intervals.
Uses BeautifulSoup for HTML parsing.
Does not use the Twitter API.
Requirements
Python 3.x
requests library
beautifulsoup4 library
schedule library
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/TwitterStockMentionScraper.git
cd TwitterStockMentionScraper
Install the required libraries:

bash
Copy code
pip install -r requirements.txt
Usage
Open a terminal and navigate to the project directory.
Run the script:
bash
Copy code
python main.py
Enter the stock symbol to look for (e.g., TSLA) and the time interval (in minutes) for scraping sessions when prompted.
Example Output
yaml
Copy code
Enter the stock symbol to look for (e.g., TSLA): TSLA
Enter the time interval (in minutes) for another scraping session: 15
Scraping for stock symbol 'TSLA' every 15 minutes.
Account: Mr_Derivatives | Mentions: 2
Account: warrior_0719 | Mentions: 1
Account: ChartingProdigy | Mentions: 3
Account: allstarcharts | Mentions: 0
Account: yuriymatso | Mentions: 2
Account: TriggerTrades | Mentions: 1
Account: AdamMancini4 | Mentions: 1
Account: CordovaTrades | Mentions: 0
Account: Barchart | Mentions: 5
Account: RoyLMattox | Mentions: 0
'TSLA' was mentioned '15' times in the last '15' minutes.
Project Structure
css
Copy code
TwitterStockMentionScraper/
│
├── README.md
├── requirements.txt
├── main.py
├── scraper.py
├── config.py
├── tests/
│   └── test_scraper.py
└── video/
    └── demo_video.mp4
Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License.