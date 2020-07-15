# haxon
Tooling to retrieve data from Axon Body Cams (aka the ones cops wear)

## Features
* Read data from Axon model body cams including video

## How to get the SD card

Axon Body Cams look imposing and secure but are actually quite trivial to open. Take any thin edge (box cutter, razor blade, even house keys can work) and work it flat into the ridge corners. Turn it and you should feel the housing start to give and eventually you can pop it off into two halves: the battery and the board. The "board" half will have two circuit boards, one screwed into the housing and a smaller strip secured with orange tape. Flip the smaller board and you'll see the micro SD card with a nice orange tamper tape garnish. Peel it back (but hold on to it if you feel like making your tampering "tamper-proof" later on!) and the card is yours.

##  How to retrieve data

Insert the micro SD into your PC's port / adapter. The filesystem won't be recognized (more on that later) but on OSX/Linux systems will be readable at a /dev/ location (in my case, /dev/disk2). Then run e.g.

`python haxon.py /dev/disk2 ~/hax/output/location`

where the first arg is the location of the SD card and the second is where you would like the data to be outputted. Haxon copies the data over using `(g)dd` and then `foremost` to reconstitute the files and write them to disk. 

## TO DO
* Figure out what sort of filesystem / structure the SD card uses so it can be formatted and wiped correctly
* Dump Axon Body Cam 2 firmware and RE functionality 
