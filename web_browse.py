#!/usr/bin/env python

import requests

class bcolors:
    PAGE = '\033[96m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
def main():
    pages = [ "http://www.google.com",
            "http://www.msn.com",
            "http://www.yahoo.com",
            "http://www.reddit.com",
            "http://www.youtube.com",
            "http://www.wikipedia.org",
            "http://www.amazon.com",
            "http://www.twitter.com",
            "http://www.facebook.com",
            "http://www.instagram.com",
            "http://www.linkedin.com",
            "http://www.netflix.com",
            "http://www.imgur.com",
            "http://www.ebay.com",
            "http://www.playboy.com",
            "http://www.microsoft.com",
            "http://www.stackoverflow.com",
            "http://www.twitch.tv",
            "http://www.blogspot.com",
            "http://www.apple.com",
            "http://www.cnn.com",
            "http://www.imdb.com",
            "http://www.github.com",
            "http://www.office.com",
            "http://www.pinterest.com",
            "http://www.paypal.com",
            "http://www.adobe.com",
            "http://www.dropbox.com",
            "http://www.whatsapp.com",
            "http://www.disney.com",
            "http://www.accuweather.com",
            "http://www.eicar.org/download/eicar.com",
            "http://www.espn.com",
            "http://www.packetpushers.net",
            "https://www.gmail.com",
            "http://darksky.net",
            "http://github.com/Microsoft/azure-docs",
            "http://live.paloaltonetworks.com/t5/Management-Articles/How-to-upgrade-a-High-Availability-HA-pair/ta-p/57081",
            "http://wiki.ubuntu.com/JonathanFerguson/Quagga",
            "http://www.woodridgebaseball.org",
            "http://www.cnet.com/how-to/marvel-cinematic-universe-timeline-avengers",
            "http://napalm.readthedocs.io/en/latest/index.html",
            "http://scotch.io/tutorials/how-to-create-a-vagrant-base-box-from-an-existing-one",
            "http://www.wireshark.org/tools/oui-lookup.html",
            "http://lg.he.net",
            "http://www.bangbus.com",
            "https://www.ssllabs.com",
            "https://www.porntube.com",
            "http://ase.arubanetworks.com"
    ]

    loop = cycle(r"-\|/")

    try:
        while True:
            for page in pages:
                response = requests.get(page)
                msg = "Browsing " + bcolors.PAGE + page + bcolors.ENDC + " and received HTTP response code: " + bcolors.WARNING + str(response.status_code) + bcolors.ENDC
                print(msg)
    except KeyboardInterrupt:
        pass

if __name__== "__main__":
    main()