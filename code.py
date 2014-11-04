import requests as r
from bs4 import BeautifulSoup

start_links=[]

link_2014="http://startups.co.uk/startups-100/2014/1-captify/"
#link_2013="http://startups.co.uk/startups-100/2013/1-myparceldelivery-com/"
#link_2012="http://startups.co.uk/startups-100/2012/1-shutl/"
#link_2010="http://startups.co.uk/startups-100/2010/1-huddle/"


start_links.append(link_2014)
#start_links.append(link_2013)
#start_links.append(link_2012)
#start_links.append(link_2010)

for y in start_links:

    print "***************************"
    print "********* Next Year *************"
    print "***************************"

    total=[]
    individual=[]
    current_link=y

    for i in range(1,101,1):

        page=r.get(current_link).text
        soup=BeautifulSoup(page)

        try:

            firm=soup.find_all("h1")[1].get_text()
            individual.append(firm)

        except:

            firm="Firm Name Failed"
            individual.append(firm)

        try:

            tagline=soup.find_all("h2")[1].get_text()
            individual.append(tagline)

        except:

            tagline="Tagline Failed"
            individual.append(tagline)

        try:

            website=soup.find_all("p")[1]
            website=website.a.get_text()
            individual.append(website)

        except:

            website= "Website Failed"
            individual.append(website)

        try:
            text1=soup.find_all("p")[2].get_text()
            text2=soup.find_all("p")[3].get_text()
            text=text1 +" "+ text2
            individual.append(text)

        except:

            text="Text Failed"
            individual.append(text)


        href = soup.find_all("a",text=str(i+1))

        href=href[0]["href"]



        if href[0:3] == "/st":

            current_link="http://startups.co.uk"+href

        elif href[0:3] == " /s":

            current_link="http://startups.co.uk/"+href[2:]

        elif href[0:3] == " st":

            current_link="http://startups.co.uk/"+href[1:]

        elif href[0:3] == "sta":

            current_link="http://startups.co.uk/"+href
        else:
            current_link=href

        individual.append(current_link)

        total.append(individual)



        print "************"
        print " "
        print individual[0]
        print " "
        print "TAGLINE: "+individual[1]
        print " "
        print "WEBSITE: "+individual[2]
        print " "
        print "DESCRIPTION: "+individual[3]
        print " "
        print "Next Link: " +individual[4]
        print "************"

        individual=[]

