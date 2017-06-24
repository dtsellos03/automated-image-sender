import requests
import random
import fbchat
import shelve
from bs4 import BeautifulSoup
import pickle

image_gallery = 'http://imgur.com/a/your_gallery_here'
fb_username = 'your_username'
fb_password = 'your_password'


class Person(object):
    """Represents a person to send images to."""

    def __init__(self, full_name):
        self.full_name = full_name
        self.gallery = {}

    def img_update(self):
        res = requests.get(image_gallery)
        exampleSoup = BeautifulSoup(res.text, 'html.parser')
        letters = exampleSoup.find_all("div", class_="post-image-container")
        body = letters[0].get('id')
        for i in range(len(letters)):
            image_link = "http://i.imgur.com/" + letters[i].get('id') + '.jpg'
            # count=count+1
            if image_link not in self.gallery:
                self.gallery[image_link] = 0

    def random_image(self, nmbchoice):
        client = fbchat.Client(fb_username, fb_password)
        friends = client.getUsers(self.full_name)
        friend = friends[0]
        for i in range(0, nmbchoice):
            selected = random.choice(list((self.gallery).keys()))
            while (self.gallery).get(selected) == 1:
                selected = random.choice(list((self.gallery).keys()))
            (self.gallery)[selected] = 1
            print(selected)
            client.sendRemoteImage(friend.uid, message='', image=selected)

    def writeToLog(self):
        unset, sent = 0, 0
        for k, v in (self.gallery).items():
            if v == 1:
                unsent += 1
            else:
                sent += 1
        with open('%s 2.txt' % self.full_name, 'w') as logFile:
            logFile.write('%s %s' % (sent, unsent))


def createPerson(nameInput):
    temp_person = Person(nameInput)
    return temp_person


def save_to_pickle():
    global People
    file_name = "image_sender_storage"
    fileObject = open(file_name, 'wb')
    pickle.dump(People, fileObject)
    fileObject.close()


def load_from_pickle():
    global People
    file_name = "image_sender_storage"
    fileObject = open(file_name, 'rb')
    People = pickle.load(fileObject)
    fileObject.close()


try:
    load_from_pickle()
    print(People)
except NameError:
    People = {}

nameInput = input("Enter full name")
numberInput = int(input("Number of images"))

if nameInput in People:
    People[nameInput].img_update()
    People[nameInput].random_image(numberInput)
    People[nameInput].writeToLog()
else:
    People[nameInput] = createPerson(nameInput)
    People[nameInput].img_update()
    People[nameInput].random_image(numberInput)
    People[nameInput].img_update()
    People[nameInput].writeToLog()

print(People)
save_to_pickle()

