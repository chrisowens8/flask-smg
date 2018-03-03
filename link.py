import datetime

class Link:
    def __init__(self,
        loc,
        changefreq,
        priority,
        lastmod = "\n\t\t<lastmod>" + str(datetime.date.today()) + "</lastmod>",
        ):
        self.__loc = loc
        self.__lastmod = lastmod
        self.__changefreq = changefreq
        self.__priority = priority

    def getLoc(self):
        return "\t\t<loc>" + self.__loc + "</loc>"

    def getLastmod(self):
        return self.__lastmod

    def getChangeFreq(self):
        return "\n\t\t<changefreq>" + self.__changefreq + "</changefreq>"

    def getPriority(self):
        return "\n\t\t<priority>" + str(self.__priority) + "</priority>"

    def setLoc(self, loc):
        self.__url = loc

    def setLastmod(self, lastmod):
        self.__lastmod = lastmod

    def setChangeFreq(self, changefreq):
        self.__changefreq = changefreq

    def setPriority(self, priority):
        self.__priority = priority
