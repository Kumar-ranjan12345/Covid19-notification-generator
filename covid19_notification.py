# pip install plyer
# pip install bs4
#pip install requests  if not installed in the system

from  plyer import notification
from bs4 import BeautifulSoup
import requests 
import time

# creating a function that will notify us 
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:/Users/Hp/Downloads/images/corona1.ico",
        timeout = 15
    )


#getting the url from web
def getData(url):
    r = requests.get(url)
    return r.text

#main function
if __name__ == "__main__":
    # while loop , if we want to get notified with a certain periodic duration
    while True:
        #notifyMe("Kumar", "Let's stop this virus together")

        # you can give the whichever site link you want .
        myhtmlData = getData("https://www.mohfw.gov.in/")

        soup = BeautifulSoup(myhtmlData, "html.parser")  #the work of beautifulsoup is to parse html data 
        #print(soup.prettify())

        # 1 is used for 2nd part of the tbody, not the first part 

        myDatastr = ""  #empty string
        # finding the table row data from the scraped data 
        for tr in soup.find_all('tbody')[0].find_all('tr'): 

            #myDatastr is the string we scraped from the website 
            myDatastr += tr.get_text()  

        myDatastr = myDatastr[1:]  #by this line of code we sliced the first line output, as ther was a space coming in the output
        itemlist = myDatastr.split("\n\n")  # itemlist is the list all data shown in the output

        # you can write your state below 
        states = ['Odisha','West Bengal', "Telangana" ]
        for item in itemlist[0:35]:  # 0 to 35 because we have data of all states and territories in first 35 entries
            datalist = item.split("\n")
            if datalist[1] in states:  
                # 1 is used because the states name in datalist is in first position
                # 0th position is the serial number
                print(datalist)
                nTitle = "Cases of Covid-19 "
                nText = f"State : {datalist[1]}\nActive : {datalist[2]}\nCured : {datalist[3]} , Deaths : {datalist[4]}\nTotal Confirmed : {datalist[5]}"
                notifyMe(nTitle, nText)
                time.sleep(5) # processing every entries after 3 each
        # in the below paranthesis we can put the time gap 
        # after that much of time the program will show you notifications
        # say the time given is 300 seconds , then this program will show you notification of the given states after that seconds 
        time.sleep(30) 