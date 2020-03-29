from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_req = 'https://www.amazon.in/s?k=mobile+under+20000&ref=nb_sb_noss_2'

uClient = uReq(my_req)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,'html.parser')

containers = page_soup.find_all("div", {"class":"sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"})

container = containers[0]

filename = "mobiles under 20000"
f = open(filename,"w")
header = "Product,Price,Rating(out of 5),Prime Delivery by\n"
f.write(header)

for container in containers :
    product_name = container.div.img["alt"]

    price_container = container.findAll("span",{"class":"a-offscreen"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("span",{"class":"a-icon-alt"})
    rating = rating_container[0].text.strip()

   # delivery_container = container.find_all("span", {"class":"a-text-bold"})
    #deliver_by = delivery_container[0].text.strip()

    print("Product : " + product_name )
    print("Price : " + price )
    print("Rating(out of 5) : " + rating )
    #print("Prime Delivery by : " + deliver_by )



