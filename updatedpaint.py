#UPDATED PAINT/ORGANISED
#calvin and hobbes by Andy Liu

"""
FEATURES

buttons:
-red highlight on hover
-green highlight on click

tools:
-Pencil, only black and thin
-Line, drag and drop
-Oval, drag and drop, left click for filled,right click for unfilled
-Rectangle, see above
-Brush, variable color and size, smoothly connected
-Polygon, left click to add verticies, right click to close poly
-Spray can
-Dropper, click for the color
-Flood fill, fill an enclosed area with a color
-Hilighter, same as brush but translucent
-Eraser, erases to the choosed background
-Clear, Erase everything except choosed background

stamps:
-calvin
-moe
-hobbes
-wagon
-walking
-zombie

functions:
-undo
-redo
-(as png or jpg)
-load (png or jpg, loaded pic becomes choosed background)

music:
-play/pause music
-stop music (if you play again it restarts)

background:
-white
-rocks
-dinosaur
-tree

color choosing:
-wheel picker
-color display

text box:
-position relative to canvas
-color chosen
-button descriptors on hover
"""

"""
STATIC THINGS
only need to do once
"""

#SETUP
#=====================================================

#importing
from random import *
from math import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from pygame import *

#tkinter stuff
root = Tk()
root.withdraw()

#screen
screen = display.set_mode((1280,800))


#background
background = image.load("images/calvin-background.jpg")
screen.blit(background,(0,0))


#canvas
canvas = Rect(50,50,720,540)
draw.rect(screen,(255,255,255),canvas)
draw.rect(screen,(0,0,0),(47,47,726,546),3)        #outside border not inside

#title
titlepng = image.load("images/title.png")
screen.blit(titlepng, (885,14))

#font
font.init()
calibrifont = font.SysFont("Calibri",17)
#======================================================



#MUSIC LOAD AND VOLUME
#========================================================

init()
mixer.music.load("music/slipfunc - amid the flowers..mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.25)

#=========================================================



#Text Box rectangle
#=========================================================
textbox = (790,430,265,160)
draw.rect(screen,(255,255,255),textbox)
draw.rect(screen,0,textbox,3)


#THE COLOR WHEEL
#========================================================

#wheel
wheel = image.load("images/colorwheel.png")
wheel = transform.smoothscale(wheel,(170,170))
wheelrect = (885,240,170,170)
screen.blit(wheel,(885,240))
draw.rect(screen,(255,255,255),wheelrect,3)


#color display
coldisplay = (1075,288,75,75)
colchoosed = ((1075,288),(1075,363),(1150,288))     #a triangle on the top left corner
draw.rect(screen,(255,255,255),coldisplay)          #later will draw colchoosed with color picked

#=========================================================




#DRAWING BUTTONS AND PUTTING THEM IN LISTS
#most buttons are 75x75 with 20 px  between
#========================================================

#tool buttons pattern for button places
toolbuts = []
p = 50
for i in range(6):
    draw.rect(screen,(255,255,255),(p,610,75,75))
    draw.rect(screen,(255,255,255),(p,705,75,75))
    toolbuts.append((p,610,75,75))
    toolbuts.append((p,705,75,75))
    p+=95


#stamp buttons
stampbuts = []
q = 695                                            #similar code going down
for j in range(3):
    draw.rect(screen,(255,255,255),(q,610,75,75))
    draw.rect(screen,(255,255,255),(q,705,75,75))
    stampbuts.append((q,610,75,75))
    stampbuts.append((q,705,75,75))
    q+=95


#function buttons
funtsbuts = []
r = 50
for c in range(4):
    draw.rect(screen,(255,255,255),(790,r,75,75))
    funtsbuts.append((790,r,75,75))
    r += 95                                       #pattern goes down instead of across


#music buttons
#special places and sizes (50x50)
musicbuts = []
playbut = (984,631,50,50)
stopbut = (984,726,50,50)
musicbuts.extend((playbut,stopbut))
for place in musicbuts:
    draw.rect(screen,(255,255,255),place)



#background changing buttons

backgroundbuts = []
whitebut = (1075,430,75,75)
draw.rect(screen,(255,255,255),whitebut)
hopsbut = (1170,430,75,75)
dinobut = (1075,515,75,75)
treebut = (1170,515,75,75)
backgroundbuts.extend((whitebut,hopsbut,dinobut,treebut))
#==========================================================




#IMAGE LOADING AND PUT INTO LISTS
#==========================================================

#tool images (logos)
toolimages = []
pencilpng = image.load("images/pencil-icon.png")
linepng = image.load("images/line-icon.png")
ovalpng = image.load("images/oval-icon.png")
rectanglepng = image.load("images/rectangle-icon.png")
brushpng = image.load("images/brush-icon.png")
polypng = image.load("images/poly-icon.png")
spraypng = image.load("images/spraycan-icon.png")
droppng = image.load("images/dropper-icon.png")
fillpng = image.load("images/fill-icon.png")
hilitepng = image.load("images/hilite-icon.png")
erasepng = image.load("images/eraser-icon.png")
erallpng = image.load("images/erall-icon.png")
toolimages.extend((pencilpng,linepng,ovalpng,rectanglepng,brushpng,polypng,spraypng,droppng,fillpng,hilitepng,erasepng,erallpng))


#stamp images
stampimages = []
calvinpng = image.load("images/calvin-stamp.png")
moepng = image.load("images/moe-stamp.png")
hobbespng = image.load("images/hobbes-stamp.png")
wagonpng = image.load("images/wagon-stamp.png")
walkingpng = image.load("images/walking-stamp.png")
zombiespng = image.load("images/zombies-stamp.png")

stampimages.extend((calvinpng,moepng,hobbespng,wagonpng,walkingpng,zombiespng))


#display stamp logos
#already cropped into squares
displayimages = []
calvindisp = image.load("images/calvin-display.png")
moedisp = image.load("images/moe-display.png")
hobbesdisp = image.load("images/hobbes-display.png")
wagondisp = image.load("images/wagon-display.png")
walkingdisp = image.load("images/walking-display.png")
zombiesdisp = image.load("images/zombies-display.png")
displayimages.extend((calvindisp,moedisp,hobbesdisp,wagondisp,walkingdisp,zombiesdisp))


#function images
funtimages = []
undopng = image.load("images/undo-icon.png")
redopng = image.load("images/redo-icon.png")
savepng = image.load("images/save-icon.png")
loadpng = image.load("images/import-icon.png")
funtimages.extend((undopng,redopng,savepng,loadpng))


#music images
musicimages = []
playpng = image.load("images/play-icon.png")
stoppng = image.load("images/stop-icon.png")
musicimages.extend((playpng,stoppng))


#background imagees
#these images are already resized to 720x540 externally
backimages = []
hopspng = image.load("images/hops-canvas.png")
dinopng = image.load("images/dino-canvas.png")
treepng = image.load("images/tree-canvas.png")
backimages.extend(("filler",hopspng,dinopng,treepng))               #filler in the white background spot, makes indexes consistent
#MAKE SURE TO CHACK FOR FILLER LATER


#background display images
#cropped to squares already
backdispimages = []
hopsdisp = image.load("images/hops-display.png")
dinodisp = image.load("images/dino-display.png")
treedisp = image.load("images/tree-display.png")
backdispimages.extend((hopsdisp,dinodisp,treedisp))

#===========================================================




#RESIZE ALL IMAGES
#faster with lists
#===========================================================

#resize background display images to 75x75
for img in backdispimages:
    backdispimages[backdispimages.index(img)] = transform.smoothscale(img,(75,75))
backdispimages.insert(0,"filler spot")              #fill the zero spot with a filler, make indexes consistent between all background related list AFTER resizing images

#resize tool images to 75x75
for img in toolimages:
    toolimages[toolimages.index(img)] = transform.smoothscale(img,(75,75))

#resize display images to 75x75
for img in displayimages:
    displayimages[displayimages.index(img)] = transform.smoothscale(img,(75,75))

#resize function images to 75x75
for img in funtimages:
    funtimages[funtimages.index(img)] = transform.smoothscale(img,(75,75))

#resize music images to 50x50
for img in musicimages:
    musicimages[musicimages.index(img)] = transform.smoothscale(img,(50,50))

#=============================================================




#BLIT IMAGES INTO CORRECT SPOTS
#=========================================================

#blit tool images
p = 50
for i in range(6):                                  #same code as defining rectangles but now blitting images in their places instead
    screen.blit(toolimages[2*i],(p,610))            #2 rows of buttons :. this pattern fills every box
    screen.blit(toolimages[2*i+1],(p,705))
    p+=95

#blit display images
q = 695
for i in range(3):                                   #same code again
    screen.blit(displayimages[2*i],(q,610))
    screen.blit(displayimages[2*i+1],(q,705))
    q+=95

#blit function images
r = 50
for i in range(4):
    screen.blit(funtimages[i],(790,r))
    r += 95

#blit music images
screen.blit(musicimages[0],(984,631))
screen.blit(musicimages[1],(984,726))

#blit background display
for i in [1,2,3]:                                   #not index of zero cuz thats the filler button
    (x,y,useless1,useless2) = backgroundbuts[i]
    screen.blit(backdispimages[i],(x,y))
#===========================================================



#COLLECTION OF LISTS
#list of buttons, bools, text and names are all related by order
#in the true/false list whatever place is true is whatever thing is chosen
#using lists for all of this so the code for choosing tools can span loops and not alot of if/else
#===========================================================

#oneselect (tools + stamps) only one can be selected at once
oneselectbuts = toolbuts + stampbuts
oneselectbools = [True] + [False] * 17                              #default pencil
oneselect = ["pencil","line","oval","rectangle","brush","poly","spray","drop",
"fill","hilite","erase","erall","calvin","moe","hobbes","wagon","walking","zombies"]


#functions
funts = ["undo","redo","save","load"]
funtsbools = [False]*4


#music
music = ["play","stop"]
musicbools = [True] + [False]                       #playing music is default

#background
backgroundbools = [True] + [False]*3

#everything
everybuts = oneselectbuts + funtsbuts + musicbuts + backgroundbuts


#text for dialog boxes
#lists inside lists let me blit each item in the inner list on different "lines" using a loop
#last one is blank for when nothing needs to be printed
tooltext = [
    ["Pencil","Draw a thin, black line"],
    ["Line","Draw a straight line"],
    ["Oval","Left click for filled","Right click for unfilled"],
    ["Rectangle","Left click for filled","Right click for unfilled"],
    ["Brush","Draw with a brush effect"],
    ["Polygon","Left click to connect points","Right click to close polygon"],
    ["Spray Can","Draw with a spray can effect"],
    ["Dropper","Click to select the color"],
    ["Fill","Fill the entire canvas"],
    ["Hilighter","Draw a translucent color"],
    ["Eraser","Erase where you click"],
    ["Clear","Erase everything"],
    ["Calvin Stamp"],
    ["Moe Stamp"],
    ["Hobbes Stamp"],
    ["Calvin and Hobbes on wagon Stamp"],
    ["Calvin and Hobbes walking Stamp"],
    ["Zombie Calvin and Hobbes Stamp"],
    ["Undo","Undo your last action"],
    ["Redo","Redo your last action"],
    ["Save","Save the canvas as a PNG or JPG"],
    ["Load","Load a canvas (720x540)"],
    ["Play","Click to pause/play music"],
    ["Stop","Stop the music"],
    ["White Background"],
    ["Hopping on rocks Background"],
    ["Dinosaur Background"],
    ["Sleeping in a tree Background"],
    [" "]
    ]
#===========================================================





"""
ACTIVE PARTS
"""


#DEFAULT OPTIONS
#=========================================================

#undo/redo lists
undolist = []
redolist = []
canvascop = screen.subsurface(canvas).copy()
whitebox = canvascop                                      #for background
undolist.append(canvascop)

#color (black)
r,g,b,a = 0,0,0,0                                   #makes it easier to alter A value
color = r,g,b,a                                     #makes it easier to type

#poly points
points = []

#fill definitions
fillps = set()
fillcol = False                                     #no color

size = 4

#undo/redo perameters 
uponcanvas = False
clickoncanvas = False

choosedbackground = whitebox                     #the preselscted background, this defines the variable only at the start
#=======================================================



#START THE WHILE LOOP
#=======================================================

running = True
while running:

    #flags for different events
    click = False
    unclick = False
    left = False
    right = False
    upscroll = False
    downscroll = False

    for e in event.get():

        #event triggers
        if e.type == MOUSEBUTTONDOWN:
            click = True
            if e.button == 1:
                left = True
            if e.button == 3:
                right = True
            if e.button == 4:
                upscroll = True
            if e.button == 5:
                downscroll = True

        if e.type == MOUSEBUTTONUP:
            if e.button == 1 or e.button == 3:      #no mouse wheel plz
                unclick = True

        if e.type == QUIT:
            running = False

#========================================================



#TYPICAL MOUSE FUNCTIONS
#========================================================

    mx,my = mouse.get_pos()


    mb = mouse.get_pressed()


#=========================================================



#SIZE
#=======================================================

#size selecting:
    if upscroll and size<18: #sets max size
        size += 1
    if downscroll and size>4:#sets min size
        size -= 1

#========================================================



#CHOOSE COLOR
#========================================================

#color picking:
    if Rect(wheelrect).collidepoint((mx,my)) and (left or right):
        r,g,b,a = screen.get_at((mx,my))                #using both rgba and color so setting A value is easier
        color = r,g,b,a

#display color
    draw.polygon(screen,color,colchoosed)
    draw.rect(screen,color,coldisplay,3)

#=========================================================


#BUTTON HOVERING
#======================================================

#red if hovering else black. also keep track of the button hovering index for text box later
    hovering = -1
    for place in everybuts:
        if Rect(place).collidepoint(mx,my):
            draw.rect(screen,(255,0,0),place,3)
            ind = everybuts.index(place)
            hovering = ind
        else:
            draw.rect(screen,(0,0,0),place,3)

#=======================================================


#CLICKING BUTTONS
#THE ONLY WAY FOR A BUTTON TO TURN TRUE IS WITH A CLICK!
#====================================================

#oneselect
    for but in oneselectbuts:
        if Rect(but).collidepoint(mx,my) and (left or right):
            ind = oneselectbuts.index(but)
            oneselectbools = [False]*18
            oneselectbools[ind] = True


#function
    for but in funtsbuts:
        if Rect(but).collidepoint(mx,my) and (left or right):
            ind = funtsbuts.index(but)
            funtsbools = [False]*4
            funtsbools[ind] = True



#combining blitting the background on canvas and turning the button true
#the true is only for green highlight reasons now
            
#background
    for but in backgroundbuts:
        if Rect(but).collidepoint(mx,my):
            if left or right:
                ind = backgroundbuts.index(but)
                if ind == 0:
                    draw.rect(screen,(255,255,255),canvas)
                    choosedbackground = whitebox                #what the background is at the present moment. used later for erasing and erall purposes
                else:
                    screen.blit(backimages[ind],(50,50))
                    choosedbackground = backimages[ind]         #what the background is rn for future reference
                undolist = []
                undolist.append(choosedbackground)              #reset undolist because selecting a different background is like clearing the screen
                redolist = []
                backgroundbools = [False]*4
                backgroundbools[ind] = True


#music true and false work differently (both can be false at the same time)
#if play is true and you click than play is false
#no need for loop because its only 2 bools long
    #cases for play
    if Rect(musicbuts[0]).collidepoint(mx,my) and (left or right):     #musicbools[0] is the play button
        if musicbools[0]:                                               # if play is true and you click on it, it turns false but stopbut doesn't turn true
            musicbools[0] = False                                   #:. pause NOT stop
        else:
            musicbools[0] = True
            musicbools[1] = False

    #case for stop
    if Rect(musicbuts[1]).collidepoint(mx,my):
        if right or left:
            musicbools = [False]*2
            musicbools[1] = True                    #always turns play to false when you click on stop

#====================================================================


#WHAT DID YOU CLICK?
#=============================================================================
#every "true" button gets a green border
#drawing green comes after drawing red so its always green
    everybools = oneselectbools + funtsbools + musicbools  + backgroundbools     #every true and false at its current state
    for but in everybuts:
        if everybools[everybuts.index(but)]:
            draw.rect(screen,(0,255,0),but,3)

#=======================================================


#Text in the text box
#=======================================================

#Reset text box
    draw.rect(screen,(255,255,255),textbox)
    draw.rect(screen,0,textbox,3)


#mouse location on canvas
    mouselocation = calibrifont.render("Mouse position at "+str((mx-50,my-50)),True,(0,0,0))        #canvas starts at 50,50 so subtr 50 to get canvas position
    notoncanvas = calibrifont.render("Not on canvas",True,(0,0,0))
    if Rect(canvas).collidepoint(mx,my):                                                            #in case not on canvas
        screen.blit(mouselocation,(800,447))
    else:
        screen.blit(notoncanvas,(800,447))


#color selected
    colormessage = calibrifont.render("Color = "+str((r,g,b)),True,(0,0,0))                         # A val is useless
    screen.blit(colormessage,(800,470))

#size selected
    sizemessage = calibrifont.render("Size = "+str(size),True,((0,0,0)))
    screen.blit(sizemessage,(800,493))


#tool selected
    d = 516
    for text in tooltext[hovering]:                                                                 #lists inside lists, puts every text short on a new "line"
        toolmessage = calibrifont.render(text,True,(0,0,0))                                         #if hovering == -1 it blits the last text which is nothing
        screen.blit(toolmessage, (800,d))
        d += 23                                                                                     #17 ft and 23 space gives 5 pixels of in between


#ACTUALLY DOING MUSIC NOW
#========================================================

#play and pause with music (false = pause) (true = play)
#playbut is play and pause in one place
    if not musicbools[0]:
        mixer.music.pause()
    else:
        if not mixer.music.get_busy():
            mixer.music.play(-1)
        else:
            mixer.music.unpause()


#stop and unstop with music
    if musicbools[1]:
        mixer.music.stop()

#=======================================================




#SAVE AND LOAD
#=================================================

#save funtbools[2] is the save button
    if funtsbools[2]:
        location = asksaveasfilename()
        if location != "":          #prevents saving to nothing
            image.save(screen.subsurface(canvas),location)
        funtsbools[2] = False       #do not repeat save


#load (funtcools[3] is the load button
    if funtsbools[3]:
        location = askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")])
        if location != "":          #prevents loading from nothing
            screen.set_clip(canvas)
            loaded = image.load(location)
            loaded = transform.smoothscale(loaded,(720,540))
            choosedbackground = loaded
            screen.blit(loaded,(50,50))
        funtsbools[3] = False       #do not repeat load

#===============================================



#UNDO AND REDO IS HARD (not anymroe)
#=======================================================

    #UNDO


    #is it drawing?
    if (mb[0] == 1 or mb[2] == 1) and Rect(canvas).collidepoint(mx,my):
        clickoncanvas = True

    #add to undolist after mousebuttonup
    if clickoncanvas:
        if unclick:
            uponcanvas = True
            clickoncanvas = False
            if len(undolist) == 1: #first unclick of the undolist resets the redolist so u cant redo past a blank screen
                redolist = []
        else:
            uponcanvas = False
    else:
        uponcanvas = False


    #adding things to the undolist
    if uponcanvas:
        onthecanvas = screen.subsurface(canvas).copy()
        undolist.append(onthecanvas)

    #the actual undoing
    #blit the second last and move the last into redolist, check for length so no crashes
    if funtsbools[0]:
        if len(undolist)>1:
            screen.blit(undolist[-2],(50,50))
            redolist.append(undolist[-1])
            del undolist[-1]
        funtsbools[0] = False


    #REDO
    #blit the last and move it to undolist again
    if funtsbools[1]:
        if len(redolist)>0:
            screen.blit(redolist[-1],(50,50))
            undolist.append(redolist[-1])
            del redolist[-1]
        funtsbools[1] = False






#DRAWING STUFF!
#everything after this point has to do with drawing
#======================================================

    screen.set_clip(canvas)

    for trueorfalse in oneselectbools:
        if trueorfalse:     #if true :. it was clicked
            if mb[0] == 1:  #filled things and normal tools here

                #pencil
                if oneselect[oneselectbools.index(trueorfalse)] == "pencil":        #only one bool in list is true :. index(trueorfalse) always has the right target, this is a way to jump from related lists
                    draw.line(screen,(0,0,0),(omx,omy),(mx,my),2)                     #always black, always size of 2., drawing a line from omx,omy to mx,my makes sure theres never any holes in the line


                #line
                if oneselect[oneselectbools.index(trueorfalse)] == "line":
                    if left:                                                        #set starting point
                        startingx,startingy = mx,my
                        cop = screen.copy()
                    hyp = int(hypot(mx-startingx,my-startingy))
                    screen.blit(cop,(0,0))                                          #so the line can "move" wothout drawing on the canvas until you unclick
                    for i in range(hyp):                                            #draws a circle at every 1 interval of the hypotenuse
                        draw.circle(screen,color,(startingx+int((mx-startingx)/hyp*i),startingy+int((my-startingy)/hyp*i)),size) #similar triangles math all in one line


                #filled oval
                if oneselect[oneselectbools.index(trueorfalse)] == "oval":          #see above
                    if left:
                        startingx,startingy =mx,my
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    circrect = Rect(startingx,startingy,mx-startingx,my-startingy)
                    circrect.normalize()
                    draw.ellipse(screen,color,circrect)


                #filled rectangle
                if oneselect[oneselectbools.index(trueorfalse)] == "rectangle":     #see above
                    if left:
                        startingx,startingy =mx,my
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    draw.rect(screen,color,(startingx,startingy,mx-startingx,my-startingy))


                #brush
                if oneselect[oneselectbools.index(trueorfalse)] == "brush":
                    hyp = int(hypot(mx-omx,my-omy))
                    for i in range(hyp):
                        draw.circle(screen,color,(omx+int((mx-omx)/hyp*i),omy+int((my-omy)/hyp*i)),size) #see above (similar triangles)


                #polygon is special, so it's skipped for now


                #spraycan, 20 at a time is a good speed, pick random points
                if oneselect[oneselectbools.index(trueorfalse)] == "spray":
                    for i in range(20):
                        rand1 = randint(size*-1,size)
                        rand2 = randint(size*-1,size)
                        if hypot(rand1,rand2) <= size:
                            screen.set_at((mx+rand1,my+rand2),color)


                #dropper, selects the color you click
                if oneselect[oneselectbools.index(trueorfalse)] == "drop":
                    if Rect(canvas).collidepoint(mx,my):
                        r,g,b,a = screen.get_at((mx,my))                            #have to change both rgba and color to be consistent
                        color = r,g,b,a


                #hiliter (translucent brush)
                if oneselect[oneselectbools.index(trueorfalse)] == "hilite":
                    #what the hilite looks like
                    circscreen = Surface((size*2,size*2),SRCALPHA)
                    draw.circle(circscreen,(r,g,b,5),(size,size),size)
                    #put it on
                    hyp = int(hypot(mx-omx,my-omy))
                    for i in range(hyp):
                        screen.blit(circscreen,((omx+int((mx-omx)/hyp*i))-size,(omy+int((my-omy)/hyp*i))-size)) #the -size centers the surface(circle) to mouse




                #eraser
                if oneselect[oneselectbools.index(trueorfalse)] == "erase":

                #the variable erasing is what you need to blit on screen, different cases for erasing depending on background

                    #define erasing when it is a white background
                    if choosedbackground == whitebox:                #white square with dimensions 2sizex2size
                        erasing = Surface((size*2,size*2))
                        erasing.fill(16777215)
                    else:
                        picturesurface = Surface((1280,800))            #makes the subsurface thats the choosed background (same relativer mx and my)
                        picturesurface.blit(choosedbackground,(50,50))

                    hyp = int(hypot(mx-omx,my-omy))
                    for i in range(hyp):

                        #define erasing when not whitebackground
                        if choosedbackground != whitebox:

                            try:#try and except statements because this code sometimes crashes when you move the mouse too fast but if you skip the crashing case everything around it "fills its place" and it looks fine either way
                                erasing = picturesurface.subsurface(int(omx+int((mx-omx)/hyp*i))-size,int(omy+int((my-omy)/hyp*i))-size,size*2,size*2)      #added int() so everything works
                            except:
                                pass

                        try:
                            screen.blit(erasing,((omx+int((mx-omx)/hyp*i))-size,(omy+int((my-omy)/hyp*i))-size))
                        except:
                            pass




                #clear canvas, points list (poly), undolist (except for first) and redolist)
                if oneselect[oneselectbools.index(trueorfalse)] == "erall":
                    if choosedbackground == whitebox:
                        draw.rect(screen,16777215,canvas)
                    else:
                        screen.blit(choosedbackground,(50,50))
                    points = []
                    undolist = [undolist[0]]
                    redolist = []



            if mb[2] == 1:#unfilled shapes by rightclicking

                #unfilled ellipse
                #checked for ellipse radius greater than width
                if oneselect[oneselectbools.index(trueorfalse)] == "oval":                  #same code as filled
                    if right:
                        startingx,startingy =mx,my
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    circrect = Rect(startingx,startingy,mx-startingx,my-startingy)
                    circrect.normalize()
                    if circrect.h > 2*size and circrect.w > 2*size:
                        draw.arc(screen,color,circrect,0,360,size)
                    else:
                        draw.ellipse(screen,color,circrect)




                #unfilled rectangle
                if oneselect[oneselectbools.index(trueorfalse)] == "rectangle":             #same code as filled rect
                    if right:
                        startingx,startingy = mx,my
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    unfilled = Rect(startingx,startingy,mx-startingx,my-startingy)
                    evensize = size+size%2
                    draw.rect(screen,color,unfilled,evensize)
                    draw.rect(screen,color,(startingx-(evensize)//2+1,startingy-(evensize)//2+1,evensize,evensize))     #next 4 lines fill in the corners of the rectangle
                    draw.rect(screen,color,(startingx-(evensize)//2+1,my-(evensize)//2,evensize,evensize))              #the various +1's eliminate pygame inconsistencies
                    draw.rect(screen,color,(mx-(evensize)//2,startingy-(evensize)//2+1,evensize,evensize))              #(found by trial)
                    draw.rect(screen,color,(mx-(evensize)//2,my-(evensize)//2,evensize,evensize))



    for trueorfalse in oneselectbools:
        if trueorfalse:

            #polygon is a special tool using both clicks :. in seperate loop
            if oneselect[oneselectbools.index(trueorfalse)] == "poly":
                if Rect(canvas).collidepoint(mx,my):
                    if left:
                        points.append((mx,my))                                          #put mouse pos in list when you left click
                        cop = screen.copy()

                    #size set on first click
                    if len(points) == 0:
                        setsize = size

                    #drawing "line" from the last clicked position to current mouse position
                    if len(points)>0:
                        lastx,lasty = points[-1]
                        hyp = int(hypot(mx-lastx,my-lasty))
                        screen.blit(cop,(0,0))
                        for i in range(hyp):
                            draw.circle(screen,color,(lastx+int((mx-lastx)/hyp*i),lasty+int((my-lasty)/hyp*i)),setsize)

                    #right click to close polygon between first and last points in pointlist
                    if right:
                        points.append((mx,my))
                        if len(points) > 0:
                            end1x,end1y = points[-1]
                            end2x,end2y = points[0]
                            hyp = int(hypot(end2x-end1x,end2y-end1y))
                            for i in range(hyp):
                                draw.circle(screen,color,(end1x+int((end2x-end1x)/hyp*i),end1y+int((end2y-end1y)/hyp*i)),setsize)

                            #resetting
                            points = []

    for trueorfalse in oneselectbools: #more loop beginnings needed to take care of case where polygon is used and so nothing is true therefore fill
        #cannot exist in loop because nothing is true
        if trueorfalse:

            #fill is a special tool using a points set
            #change every adjacent color with the same color
            #initial click point and color
            if oneselect[oneselectbools.index(trueorfalse)] == "fill": #if tool is fill

                #first click
                if (left or right) and Rect(canvas).collidepoint(mx,my) and screen.get_at((mx,my)) != color:
                    fillps.add((mx,my))
                    fillcol = screen.get_at((mx,my))
                    screen.set_at((mx,my),color)

                #while loop goes through every adjacent pixel from the click and spreads out, applicable pixels only need to be put in the set once
                if fillcol != False:
                    while len(fillps)>0:
                        fx,fy = fillps.pop()
                        for adx in [-1,1]:
                            for ady in [-1,1]:
                                if screen.get_at((fx+adx,fy+ady)) == fillcol and ((fx+adx,fy+ady) not in fillps):
                                    fillps.add((fx+adx,fy+ady))
                                    screen.set_at((fx+adx,fy+ady),color)

                    #reset after loop
                    fillps = set()




#===============================================================



#STAMPS
#same code for every stamp
#==============================================================

    #a bit of debugging
    #if any function button is clicked while a stamp is selected it will blit it and do the function at the same time and cause problems
    functionclick = False
    for but in funtsbuts:
        if Rect(but).collidepoint(mx,my):
            functionclick = True

    for trueorfalse in oneselectbools:
        if trueorfalse:
            if mb[0] == 1 and not functionclick:

                #calvin stamp
                if oneselect[oneselectbools.index(trueorfalse)] == "calvin":
                    length,width = calvinpng.get_rect().size                    #gets dimensions of image
                    if left:
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    screen.blit(calvinpng,(mx-length//2,my-width//2))           #centers image to mouse


                #moe stamp
                if oneselect[oneselectbools.index(trueorfalse)] == "moe":
                    length,width = moepng.get_rect().size
                    if left:
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    screen.blit(moepng,(mx-length//2,my-width//2))

                #hobbes stamp
                if oneselect[oneselectbools.index(trueorfalse)] == "hobbes":
                    length,width = hobbespng.get_rect().size
                    if left:
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    screen.blit(hobbespng,(mx-length//2,my-width//2))

                #wagon stamp
                if oneselect[oneselectbools.index(trueorfalse)] == "wagon":
                    length,width = wagonpng.get_rect().size
                    if left:
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    screen.blit(wagonpng,(mx-length//2,my-width//2))

                #walking stamp
                if oneselect[oneselectbools.index(trueorfalse)] == "walking":
                    length,width = walkingpng.get_rect().size
                    if left:
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    screen.blit(walkingpng,(mx-length//2,my-width//2))

                #zombies stamp
                if oneselect[oneselectbools.index(trueorfalse)] == "zombies":
                    length,width = zombiespng.get_rect().size
                    if left:
                        cop = screen.copy()
                    screen.blit(cop,(0,0))
                    screen.blit(zombiespng,(mx-length//2,my-width//2))

    screen.set_clip()
    omx,omy = mx,my
#==============================================================
    display.flip()
quit()

















