# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

# TODO: NewsStory


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

    def is_phrase_in(self, story):
        pass

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        """
        The constructor
        """
        self.phrase = phrase.lower().split(' ')

    def is_phrase_in(self, text):
        text = text.lower()
        text_list = []
        word = []
        for i in text:
            if i == ' ' or i in string.punctuation:
                if word:
                    text_list.append("".join(word))
                word = []
                continue
            else:
                word.append(i)
        if word:
            text_list.append("".join(word))
        i = 0
        while i < len(text_list):
            j = 0
            temp = i
            while j < len(self.phrase) and i < len(text_list) and text_list[i] == self.phrase[j]:
                i, j = i + 1, j + 1
            if j == len(self.phrase):
                return True
            i = temp + 1
        return False


# TODO: PhraseTrigger

# Problem 3
class TitleTrigger(PhraseTrigger):
    def is_phrase_in(self, story):
        return PhraseTrigger.is_phrase_in(self, story.get_title())

    def evaluate(self, story):
        return self.is_phrase_in(story)


# TODO: TitleTrigger

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def is_phrase_in(self, story):
        return PhraseTrigger.is_phrase_in(self, story.get_description())

    def evaluate(self, story):
        return self.is_phrase_in(story)
# TODO: DescriptionTrigger

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, time_now):
        self.datetime = datetime.strptime(time_now, "%d %b %Y %H:%M:%S")

# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, time):
        if time.get_pubdate() < self.datetime:
            return True
        else:
            return False

class AfterTrigger(TimeTrigger):
    def evaluate(self, time):
        if time.get_pubdate() > self.datetime:
            return True
        else:
            return False
# TODO: BeforeTrigger and AfterTrigger


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.value = trigger.evaluate

    def evaluate(self, story):
        return not self.value(story)
# TODO: NotTrigger

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, triggera, triggerb):
        self.functiona = triggera.evaluate
        self.functionb = triggerb.evaluate

    def evaluate(self, story):
        return self.functiona(story) and self.functionb(story)
# TODO: AndTrigger

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, triggera, triggerb):
        self.functiona = triggera.evaluate
        self.functionb = triggerb.evaluate

    def evaluate(self, story):
        return self.functiona(story) or self.functionb(story)
# TODO: OrTrigger


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    filter_sto = []
    for i in stories:
        for j in triggerlist:
            if j.evaluate(i) and i not in filter_sto:
                filter_sto.append(i)
    stories = filter_sto
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    trigger_list = []
    dic = {}
    for i in lines:
        words = i.split(',')
        if words[0] == 'ADD':
            for j in words[1:]:
                trigger_list.append(dic[j])
        else:
            if words[1] == 'DESCRIPTION':
                dic[words[0]] = DescriptionTrigger(words[2])
            elif words[1] == 'TITLE':
                dic[words[0]] = TitleTrigger(words[2])
            elif words[1] == 'BEFORE':
                dic[words[0]] = BeforeTrigger(words[2])
            elif words[1] == 'AFTER':
                dic[words[0]] = AfterTrigger(words[2])
            elif words[1] == 'NOT':
                dic[words[0]] = NotTrigger(words[2])
            elif words[1] == 'AND':
                dic[words[0]] = AndTrigger(dic[words[2]], dic[words[3]])
            elif words[1] == 'OR':
                dic[words[0]] = OrTrigger(dic[words[2]], dic[words[3]])




    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!
    return trigger_list


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("https://news.baidu.com/"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

