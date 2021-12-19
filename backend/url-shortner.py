import pyshorteners
import eel

eel.init('D:/scripts/python/PyApps/URLshortner/frontend')
short = pyshorteners.Shortener()

@eel.expose
def generate_url(data):
    outputUrl = short.tinyurl.short(data)
    return outputUrl

eel.start('index.html', size=(1000,600))