#!/usr/bin/env python3

import requests
import shelve
from bs4 import BeautifulSoup
import random
import smtplib
import shelve
import fbchat

def imgur_scrape(URL):
    """ Scrapes the IDs of images in an imgur album """
    res = requests.get(URL)
    soup_object = BeautifulSoup(res.text, 'html.parser')
    imgur_ids=soup_object.find_all("div", class_="post-image-container")
    return imgur_ids

def imgur_link_add(chosen_dictionary):
    """ Adds imgur URLs to dictionary if not already added """
    imgur_ids=imgur_scrape(imgur_album)
    for i in range(len(imgur_ids)):
        imgur_url="http://i.imgur.com/"+imgur_ids[i].get('id')+'.jpg'
        if imgur_url not in chosen_dictionary:
            chosen_dictionary[imgur_url]=0

def image_send(number_of_images):
    """ Sends images to selected friend """
    client = fbchat.Client("username", "password")
    friends = client.getUsers(friend_of_choice)
    friend = friends[0]
    selected=""
    for i in range(0,number_of_images):
        selected=random.choice(list(chosen_dictionary.keys()))
        while chosen_dictionary.get(selected)==1:
            selected=random.choice(list(chosen_dictionary.keys()))
        chosen_dictionary[selected]=1
        print(selected)
        print("\n %s" %selected)
        client.sendRemoteImage(friend.uid,message='', image=selected)

def write_log():
    """ Writes count of sent/unset images to log """
    count0=0
    count1=0
    log_file = open('%s.txt' %friend_of_choice, 'w')
    for k, v in chosen_dictionary.items():
                if v==1:
                    count0=count0+1
                else:
                    count1=count1+1
            
    log_file.write('%s %s' %(count1,count0))
    log_file.close()

people={
    1:'FRIEND 1',
    2:'FRIEND 2',
    3:'FRIEND 3',
    4:'FRIEND 4',
    5:'FRIEND 5',
}

storage_shelve = shelve.open('shelfname')

friend_1 = storage_shelve['friend_1']
friend_2 = storage_shelve['friend_2']
friend_3 = storage_shelve['friend_3']
friend_4 = storage_shelve['friend_4']
friend_5 = storage_shelve['friend_5']

dict_catalog={
    1:friend_1,
    2:friend_2,
    3:friend_3,
    4:friend_4,
    5:friend_5,
}


#User chooses which friend to send images to, how many images
pplchoice=int(input('\n FRIEND 1 - 1 \n FRIEND 2 - 2 \n FRIEND 3 - 3 \n FRIEND 4 - 4 \n FRIEND 5 - 5 \n FRIEND 6 - 6 \n FRIEND 7 - 7 \n\n '))
number_of_images=int(input('\nNumber of images:\n\n '))
friend_of_choice=people[pplchoice]
chosen_dictionary=dict_catalog[pplchoice]

#Scrapes and sends images
imgur_album="http://imgur.com/a/ZZZZZZZZZZ"
imgur_link_add(chosen_dictionary)
image_send(number_of_images)
write_log()

#Saves dictionary to shelf file
person_of_interest=str(dict_catalog[pplchoice])
storage_shelve[person_of_interest]=chosen_dictionary
storage_shelve.close()
