# Import Link()
from link import Link
from flask import Flask, flash
# Define XML excape characters
escapeCharacters = {
    '&': '&amp;',
    '"': '&quot;',
    "'": '&apos;',
    '<': '&lt;',
    '>': '&gt;'}

# Escape XML characters by line
def escapeUrl(url):
    for key, value in escapeCharacters.items():
        if key in url:
            url = url.replace(key, value)
        else:
            continue
    return url

# Generates sitemap.xml
def generator(uploadedFile, changefreq, priority):

    # Opens uploaded file
    userUpload = open(uploadedFile, 'r')

    # Define empty list to store URLs
    urls = []

    # Define currentLine and read in the first line
    currentLine = userUpload.readline()

    # Outer loop reads in each line
    while currentLine.endswith('\n') and len(urls) <= 50000:

        # Verifies URLs begin with http
        if currentLine.startswith('http'):

            # Calls escapeURL on each line
            currentLine = escapeUrl(currentLine)

            # Calls Link()
            currentLine = Link(currentLine[0:-1], changefreq, priority)

            # Appends escaped URL w/ XML markup to urls list
            urls.append(
                "\t<url>\n" +
                currentLine.getLoc() +
                currentLine.getLastmod() +
                currentLine.getChangeFreq() +
                currentLine.getPriority() +
                "\n\t</url>")

            # Reads in the next line
            currentLine = userUpload.readline()

        else:
            # Reads in the next line
            currentLine = userUpload.readline()

    # Creates a sitemap.xml file (overwrites if already exists)
    sitemap = open('sitemap/sitemap.xml', 'w')

    # Writes the XML file header
    sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    # Loops through urls list and writes them to sitemap.xml
    for address in urls:
        sitemap.write(address + '\n')

    # Writes the closing urlset tag
    sitemap.write("</urlset>")

    # Closes sitemap.xml
    sitemap.close()

    return
