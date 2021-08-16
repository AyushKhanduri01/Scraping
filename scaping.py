# Importing the files required for our scraping:
# selenium - allows us to connect to the browsers like Chrome, Firefox, Safari etc. The Webdriver in it specifies which browser you have to access and for that we have to first install the webdriver of the browser we want and then specifies the path of the webdriver in our program.
# BeautifulSoup - allows us to extract data from the browser and modify it. 
# time - specifies the time which we can use anywhere in our code and for many purposes.
# csv - allows us to store tabular data and database in the comma separated value on which we can work.
# requests - allows us to send HTTP requests.
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

# Storing the url in a constant called URL
URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

# Storing our Chrome Webriver in a variable called browser
browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get(URL)# The get function will open the whole browser and will wait till the whole page gets loaded

time.sleep(10)# Here we are allowing the program to take a break for 10 seconds so that the whole browser can be loaded prefectly


# We have create a scrape function using the def keyword in which we are going to scrape the data we need
def scrape():

    # We are storing the name of the headers that we have to use in the file that we will have had created in the headers variable
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    

    # There are many pages of data than a single one and for importing all the data of the all the pages we are using the for loop
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parse")# here we are getting the page source(the code which used to create the webpage which we noramlly look) of the webpage with the help of .page_source and as we have to get that coded data in the html format we are using html.parse of the BeautifulSoup to convert that data into html format through which we are going to get the specific data we need and then storing the data in the soup variable.
        
        # We are going to create in for loop in which we will get the data we need.
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):# here we have created a for loop in which we used the soup.final_all(It returns the data to specified after scanning the whole document) function to get all the data inside the ul tags whose attribute of class is equal "expolanet " we are only taking these ul tags because we don't the unneccessary data we only need the data of the given table and storing the retrieved data in ul_tag variable.
            li_tags = ul_tag.find_all("li")# here we finding all li tags inside of the data we stored in ul_tag and thn storing it in li_tags
            data = []# here we have created a data array which will store the data

            # We are creating a for loop which can create all the data if the li_tags in indexed format and store it in variables
            for index, li_tag in enumerate(li_tags):# here we are indexing the data inside the li_tags and as it has been converted into the indexed formation then storing its indexes in teh index variable the li_tags data in the li_tag variable.
                if index == 0:
                    data.append(li_tag.find_all("a")[0].contents[0])
                else:
                    