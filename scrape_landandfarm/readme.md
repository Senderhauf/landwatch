# Scrape [landandfarm.com](landandfarm.com) listings

Landandfarm does not offer a public api. Therefore it is necessary to find listings by using python to scrape the site.

The urls contain query parameters that allow for easier extraction of filtered data as well as well-defined routes for searching states and zip codes. 

Here is an example url:
>https://www.landandfarm.com/search/AL/35004-land-for-sale/?MinPrice=5000&MaxPrice=25000

The following query string parameters are of note:

1. MinPrice
...Minimum price
2. MaxPrice
...Maximum Price

## Structure

The structure of this python cli module is based on instructions found at [Real Python](https://realpython.com/python-application-layouts/) and [Python-Guide](https://docs.python-guide.org/writing/structure/#).

