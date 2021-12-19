from tqdm import tqdm
import re
import pandas as pd
import numpy as np
import requests
import bs4
search_item = [('men'  , 'shoes' , 30),
               ('kid' , 'shoes', 20 ),
               ('women' , 'tshirt', 20),
               ('men' , 'tshirt' , 20),
               ('kid' , 'tshirt' , 20),
               ('women', 'glasses' , 20),
               ('men' , 'sleeper' , 20),
               ('women' , 'sleeper' , 20),
               ('kid' , 'glasses', 20),
               ('men', 'shirt' , 20),
               ('women' , 'shirt' , 20),
               ('men' , 'glasses' , 30),
               ('women' , 'shoes' ,30),
               ('men'  , 'lower' , 20),
               ('women' , 'lower' , 20),
               ('kids' , 'lower' , 10),
               ('men' , 'watch' , 20),
               ('women' ,'watch' , 20),
               ('men', 'sandal' , 20),
               ('women' , 'sandal' ,20),
               ('kid' , 'sandal' , 20),]
# pat_brand = re.compile(r'[\b]?[A-Z]{3,}\b')
pat = re.compile(r'[0-9,]+')
data = {
        'Brand': [],
        'Title': [],
        'Product Type': [],
        'Who': [],
        'Price': [],
        'MRP': [],
        'Savings': [],
        'Discount %': [],
        'Rating' : [],
        'Total Ratings Given': [],
        'Total Reviews Given': [],
    }
def scrap_details(url,who, product_type , pages):
    for i in range(1, pages):
        res = requests.get(url,params={'page':i })
#         print(url)
    
    
        if res.status_code == 200:
            content = res.content
            soup = bs4.BeautifulSoup(content,'html.parser')
            for item in soup.find_all('div', class_="_1kLt05"):
                brand_name = item.find('div', attrs = {'class':"_1W9f5C"})
                if brand_name:

                    title = brand_name.text[2:]
#                     brand_name = match = re.search(pat_brand  ,title )
                    brand_name = title.split()[0]
                else:
                    continue
                

                discount = item.find('div' ,attrs = {'class':"_3Ay6Sb"} )
                if discount:
                    discount = discount.span.text
                    discount = round(float(discount.split()[0].replace('%', '')),2)
                else:
                    discount = 0

                price = item.find('div' ,attrs = {'class':"_30jeq3 UMT9wN"} )
                if price:
                    price = price.text
                    price = int(price[1:].replace(',', ''))

                if price:
                    MRP = round((price * 100)/(100 - discount) , 2)
                    
                saving = int(MRP - price)
                
                rating = item.find('div' , attrs = {'class' : '_3LWZlK' })
                if rating :
                    rating = float(rating.text)
                else:
                    rating = np.nan
                    # Total No. of  Ratings  and Reviwes given to Product
                no_of_rat_rev = item.find('span' , attrs = {'class':"_34hpFu"})
                if no_of_rat_rev:
                    
                    ls = re.findall(pat , no_of_rat_rev.text)
                    if ls:
                        no_of_ratings = int(ls[0].replace(',', ''))
                        no_of_reviews =int(ls[1].replace(',', ''))

                    # Appending Alll the Values into 'data' dict
                data['Brand'].append(brand_name)
                data['MRP'].append(MRP)
                data['Who'].append(who)
                data['Product Type'].append(product_type)
                data['Title'].append(title)
                data['Savings'].append(saving)
                data['Discount %'].append(discount)
                data['Price'].append(price)
                data['Total Ratings Given'].append(no_of_ratings)
                data['Total Reviews Given'].append(no_of_reviews)
                data['Rating'].append(rating)
    
#Driver Code 
if __name__ = '__main__':
    for who , product_type , pages in tqdm(search_item):
        url = f'https://www.flipkart.com/search?q={who}+sport+{product_type}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    #     print(url)
        scrap_details(url , who , product_type , pages )
    else:
        print('Data Scraped Successfully!!')
