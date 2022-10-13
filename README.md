# Multicore-WebScraping-VideoGames
A multiprocessing Web Scraper that will help for research of some games for the Nintendo Switch, PlayStation 4 and PlayStation 5

In this case we use various libraries from webscrape to multiprocessing, these are helpful because of the efficiency and simpleness.

We use the libraries Beautiful Soup, Urllib.request, Json and Multiprocess.Process

# Web Scrape with Python
First for the metacritic page, it's needed to lower the cases because of how the link is scripted, then put the console in a separated string to use as a headline. We also used json because of the properties of the Metacritic's HTML.

For the Amazon website we need to create a dictionary of URL to use for every string in oreder to function, then we extract not only the normal price but the sale price as well.

Finally for the Nintendo One, because of the TEC server we couldn't scrap the original page, howewer, we can use Eshop prices, a website which main purpose is to search for all the prices all arround the eshop of the world

# The HTML Page
We use the language HTML to create a pseudo website that can show all the game's info, in that page we used a Compucell-type website

![photo_5060210145094642226_y](https://user-images.githubusercontent.com/114549612/195651403-efa61a1d-e864-4ddd-ad69-2e4af2a4bb15.jpg)

In the page we add the following data:

- Title of the game
- Image of the cover
- The Amazon Price
- The Nintendo Eshop Prices
- The Metacritic Score


In the end it's going to look like this

![photo_5064567780258458191_y](https://user-images.githubusercontent.com/114549612/195658855-73056636-0d43-4a0f-8eb1-5c87b9d090b9.jpg)
