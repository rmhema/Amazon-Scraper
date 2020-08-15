# Amazon-Scraper
#### Step #1
Create an environment for scraping using Python. You can use whichever environment manager you prefer. 
To create a conda environment, use `conda create --name scrape`. After creating the environment, activate it by typing `conda activate scrape`.

Install the requirements by using 
`pip install -r Amazon-Scraper/requirements.txt`

#### Step #2

Search in Google What is `what is my user agent`, copy the top result.
Open Amazon-Scraper/product_scraper.py with a text editor. Replace the copied result in scrape function: `your_user_agent`.

#### Step #3
Run the following commands:
1. `python Amazon-Scraper/create_search_urls.py`
You can enter the name of the product you have to scrap in Amazon.com
It will create urls upto 30(can be increased) pages which will be scraped.

2. `python Amazon-Scraper/product_scraper.py`
This will create a json file where the extracted data is present and product_urls.txt with all the urls of the Amazon Products.


#### Voila! Data  is scraped!
