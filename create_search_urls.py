f = open('search_urls.txt', 'w+')

search_input = input("Enter the product you want to search! ")

product_query = search_input.replace(" ", "+")

url = 'https://www.amazon.com/s?k=' + str(product_query) + '&ref=nb_sb_noss_2'
f.write(url)
f.write('\n')

for i in range(2, 31):
    url = 'https://www.amazon.com/s?k='+ str(product_query) + '&page=' + str(
        i) + '&qid=1594555641&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()
