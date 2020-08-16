from selectorlib import Extractor
import requests
import json

e = Extractor.from_yaml_file('search_results.yml')


def scrape(url):
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'your_user_agent',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    r = requests.get(url, headers=headers)
    # This is to check if the Amazon page is blocked :
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print(
                "Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (
                url, r.status_code))
        return None
    # Pass the HTML of the page and create
    return e.extract(r.text)


with open("search_urls.txt", 'r') as urllist, open('search_output.json', 'w') as outfile:
    f = open('product_urls.txt', 'w')
    for url in urllist.read().splitlines():
        data = scrape(url)

        if data:
            try:
                for product in data['products']:
                    product['url'] = 'https://www.amazon.com' + product['url']
                    f.write(product['url'])
                    f.write('\n')

                    json.dump(product, outfile)
                    outfile.write(", \n")

            except:
                continue
    f.close()
