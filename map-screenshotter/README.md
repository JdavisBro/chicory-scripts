# Map Screenshotter

These are a collection of scripts for screenshotting the chicory map!

Here's the steps that should work i think

if at any point it doesn't work, cry
in the issues section of this repo

## Step uhh 0
ok so when you play the normal game you'll have your dog there and yer paint there and yer cursor there
this is UNCOOL if you want a clear map with no doggies and no paint AND ESPECIALLY darkness
you'll need undertalemodtool... open the chicory data.win (and also backup the data.win)
search for objDog, objPaint and objBrush. SET all of their visible things to NOP and now you cna uh uhu huh h save the data.win
now you have a second data.win where doggy, paint (including darkness) and brush will be invisible (and some things (like mushrooms) won't work)!!!
however objects will be able to be painted so make sure you do not have the swim ability, so remove the "power_swim" tag from your save data or something idk you tell me is anyone reading this?
ok so now you're ready for clean screenshots

## Step 1
run get-levels.py

open get-levels.py and modify the LEVEL_DATA_PATH variable to point to your level_data file
windows: `/Program Files (x86)/Steam/steamapps/common/Chicory A Colorful Tale/PC/level_data`

something like
`python3 get-levels.py`
py instead of python3 on windows

## Step 2
AHHHHHHHHHH
you're not gonna be able to use your pc for a while, while this is happening
SET your chicory to FULLSCREEN!!!
set resolution to your screen resolution (1080p or something)
now.... run get-shots.py
wait.. until you've been on the title screen for too long

## Step 3
something has gone wrong
usually the title screen is in the wrong place
make sure the title screen is 1_2_0 and NOWHERE ELSE
if it is somewhere else uhh delete the image of where it shouldn't be and delete 1_2_0 too and run get-shots.py again

## Step 4
ok ok okok ok okkkkkkkkk
now you're ready??!?!?
go into your screenshots and run (python3 or py) `python3 _stitch.py LAYER` replace LAYER with 0, 1 or 2
it'll output as _out0 1 or 2

## Step 5
there is no step 5, you have an 11mb image
