# haxon
Python 3 tooling to retrieve data from Axon Body Cams - aka the ones cops wear. This code should work for first and second generation models

Initial tweet thread & context here https://mobile.twitter.com/unrealchill/status/1283418136738496513

##  How to retrieve data

Insert the micro SD into your PC's port / adapter. The filesystem won't be recognized (more on that later) but on OSX/Linux systems will be readable at a /dev/ location (in my case, /dev/disk2). Then run e.g.

`python3 haxon.py /dev/disk2 ~/hax/output/location`

where the first arg is the location of the SD card and the second is where you would like the data to be outputted. Haxon copies the data over using `(g)dd` and then `foremost` to reconstitute the files and write them to disk. 


## Why do this? // Implications
First and foremost, this evidence is collected on the public and therefore belongs to the public. Evidence should be democratized and made available to all who wish to view it in full integrity. By design, these devices are meant to shield and conceal evidence and footage from the public - they are built with the police perspective in mind. By creating tools for civilians to extract the data from these devices, we are rightfully reclaiming what is ours. Secondly, the nature by which we are able to extract this data reveals significant holes in the chain of custody for evidence collection. It is demonstrably simple for the police (or other security parties) to erase footage and modify the contents of the device BEFORE any review, even by the proprietary app that is usually required to retrieve footage from these devices. 

## How to get the SD card

Axon Body Cams look imposing and secure but are actually quite trivial to open. Take any thin edge (box cutter, razor blade, even house keys can work) and work it flat into the ridge corners. Turn it and you should feel the housing start to give and eventually you can pop it off into two halves: the battery and the board. The "board" half will have two circuit boards, one screwed into the housing and a smaller strip secured with orange tape. Flip the smaller board and you'll see the micro SD card with a nice orange tamper tape garnish. Peel it back (but hold on to it if you feel like making your tampering "tamper-proof" later on!) and the card is yours.

## TO DO
* Figure out what sort of filesystem / structure the SD card uses so it can be formatted and wiped correctly
* Dump Axon Body Cam 2 firmware and RE functionality 
