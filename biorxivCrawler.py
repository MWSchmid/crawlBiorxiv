#!/usr/bin/python2.7
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def extractLinkInPage(driver):
    allLinkElements = driver.find_elements_by_class_name("highwire-cite-linked-title")
    out = [elem.get_attribute("href") for elem in allLinkElements]
    with open("myCrawlerLinks.txt", "a") as outfile:
        print >> outfile, '\n'.join(out)
    return out

def getAllLinks(driver):
    driver.get("http://biorxiv.org/content/early/recent")
    lastPageElem = driver.find_element_by_class_name("pager-last.last.odd")
    lastPageNum = int(lastPageElem.text)
    pageCounter = 0
    out = []
    while pageCounter < lastPageNum:
        curLinks = extractLinkInPage(driver)
        out.extend(curLinks)
        driver.get("http://biorxiv.org/content/early/recent?page=" + str(pageCounter))
        pageCounter += 1
        if (pageCounter % 10) == 0:
            print >> sys.stderr, pageCounter, "pages..."
            time.sleep(10)
    return out

def extractJournalFromPage(driver, link):
    driver.get(link)
    time.sleep(6)
    try:
        elem = driver.find_element_by_class_name("pub_jnl")
        out = elem.text
    except NoSuchElementException:
        out = "unpublished"
    fields = out.split(' ')
    try:
        out = ' '.join(fields[3:fields.index("doi:")])
    except ValueError:
        out = "unpublished"
    return out

myDriver = webdriver.Firefox()
myLinks = getAllLinks(myDriver) # comment if you have already a list of links
#with open("todoLinks.txt", "rb") as infile: # uncomment if you have already a list of links
#    myLinks = [line[:-1] for line in infile] # uncomment if you have already a list of links
with open("linkPublishedIn.txt.txt", "a") as outfile:
    journalCounter = {"unpublished":0}
    for curLink in myLinks:
        journal = extractJournalFromPage(myDriver, curLink)
        print >> outfile, curLink + '\t' + journal
        if journal:
            try:
                journalCounter[journal] += 1
            except KeyError:
                journalCounter[journal] = 1
        else:
            journalCounter["unpublished"] += 1
myDriver.close()

for journal, counter in journalCounter.items():
    print '\t'.join([journal, str(counter)])


