# Scrape [landwatch.com](landwatch.com) listings

Landwatch does not offer a public api. Therefore it is necessary to find listings by using python to scrape the site.

Fortunately, the urls contain query parameters that allow for easier extraction of filtered data. The following query string parameters are of note:

1. ct=r
...Unsure what this does but it's necessary.
2. type=5,31
...This indicates both state and type of land listing. In this case "5,31" indicates that the state is Colorado. A value of "5,32" would search listings in the state of Connecticut. This second number can be incremented until all listings having been searched, starting at "5,25" for Alabama up until "5,83" for Wyoming. 
3. r.PSIZ=5,100
...This indicates that the parcel size range should be between 5 and 100 acres. 
4. pn=5000
...Price range lower bound is $5000
5. px=20000
...Price range upper bound is $20000

## Structure

The structure of this python cli module is based on instructions found at [Real Python](https://realpython.com/python-application-layouts/) and [Python-Guide](https://docs.python-guide.org/writing/structure/#).

