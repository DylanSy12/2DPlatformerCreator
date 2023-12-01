
from cmu_graphics import *
import decimal
app.sizeMulti = 2
app.height = 400*app.sizeMulti
app.width = 400*app.sizeMulti
app.centery = app.height/2
app.centerx = app.width/2
# app.pixelSize=4.0404040404040404040404040404*app.sizeMulti
app.pixelSize=app.width/99
class Portal:
    def __init__(self,left,top):
        self.shape=Rect(left,top,5*app.pixelSize,7*app.pixelSize,fill='purple')
        self.shape.transported=False
        self.shape.block='p'
        p=0
        for i in portalList:
            if len(i)==0 or len(i)==1:
                if p==0:
                    p+=1
                else:
                    portalList.remove(i)
        app.portals=len(portalList)-1
        p=0
        for i in portalList:
            if p>app.portals:
                portalList.remove(i)
            p+=1
        self.shape.portalIndex=app.portals
        if len(portalList[app.portals])==0:
            self.shape.pair=1
        elif len(portalList[app.portals])==1:
            self.shape.pair=0
        portalList[app.portals].append(self.shape)
        portalListSelf.append(self)
        if len(portalList[app.portals])==2:
            portalList.append([])
            app.portals+=1
    def teleport(self):
        xDis=int(distance(character.centerX,0,portalList[self.shape.portalIndex][self.shape.pair].centerX,0)/app.pixelSize)
        yDis=int(distance(0,character.centerY,0,portalList[self.shape.portalIndex][self.shape.pair].centerY)/app.pixelSize)
        x=0
        y=0
        while x<xDis:
            if character.centerX<portalList[self.shape.portalIndex][self.shape.pair].centerX:
                moveRight(collisionArray,roomGroup,graphicGroup)
                app.moveH+=1
            elif character.centerX>portalList[self.shape.portalIndex][self.shape.pair].centerX:
                moveLeft(collisionArray,roomGroup,graphicGroup)
                app.moveH-=1
            x+=1
        while y<yDis:
            if character.centerY<portalList[self.shape.portalIndex][self.shape.pair].centerY:
                moveDown(collisionArray,roomGroup,graphicGroup)
                app.moveV+=1
            elif character.centerY>portalList[self.shape.portalIndex][self.shape.pair].centerY:
                moveUp(collisionArray,roomGroup,graphicGroup)
                app.moveV-=1
            y+=1
        portalList[self.shape.portalIndex][self.shape.pair].transported=True
class Ladder:
    def __init__(self,left,top):
        self.shape=Rect(left,top,app.pixelSize,app.pixelSize,fill='sandybrown')
        self.shape.block='l'
        ladderList.append(self.shape)
class Torch:
    def __init__(self,centerX,centerY,radius):
        self.shape=Line(centerX,centerY-app.pixelSize,centerX,centerY+app.pixelSize,lineWidth=app.pixelSize,fill='brown')
        self.shape.block='t'
        # self.light=Circle(self.shape.x1,self.shape.y1,radius,fill='white',opacity=15)
        # self.light1=Circle(self.shape.x1,self.shape.y1,radius,fill=gradient('white','white','ivory','ivory','ivory','floralwhite','floralwhite','floralwhite','lightgray','dimgray','black'),opacity=5)
        # self.light2=Circle(self.shape.x1,self.shape.y1,radius,fill=gradient('white','white','ivory','ivory','ivory','floralwhite','floralwhite','floralwhite','lightgray','dimgray','black'),opacity=5)
        # self.light3=Circle(self.shape.x1,self.shape.y1,radius,fill=gradient('white','white','ivory','ivory','ivory','floralwhite','floralwhite','floralwhite','lightgray','dimgray','black'),opacity=5)
        # self.light4=Circle(self.shape.x1,self.shape.y1,radius,fill=gradient('white','white','ivory','ivory','ivory','floralwhite','floralwhite','floralwhite','lightgray','dimgray','black'),opacity=5)
        # self.light5=Circle(self.shape.x1,self.shape.y1,radius,fill=gradient('white','white','ivory','ivory','ivory','floralwhite','floralwhite','floralwhite','lightgray','dimgray','black'),opacity=5)
        self.lightList=[]
        for i in range(5):
            self.lightList.append(Circle(self.shape.x1,self.shape.y1,radius,fill=gradient('white','white','ivory','ivory','ivory','floralwhite','floralwhite','floralwhite','lightgray'),opacity=5,visible=False))
        # torchGroup.add(self.shape)
        torchList.append(self)
collisionArray=[]
editArray=[]
portalList=[[]]
portalListSelf=[]
ladderList=[]
torchList=[]
shapeBlockList=[]
#shapes
app.background='white'
levelBorderA=Polygon((0-(app.pixelSize*50)),(0-(app.pixelSize*50)),(app.width+(app.pixelSize*50)),(0-(app.pixelSize*50)),(app.width+(app.pixelSize*50)),(app.height+(app.pixelSize*50)),(0-(app.pixelSize*50)),(app.height+(app.pixelSize*50)),(0-(app.pixelSize*50)),(0-(app.pixelSize*50)),(0-(app.pixelSize*100)),(0-(app.pixelSize*100)),(0-(app.pixelSize*100)),(app.height+(app.pixelSize*100)),(app.width+(app.pixelSize*100)),(app.height+(app.pixelSize*100)),(app.width+(app.pixelSize*100)),(0-(app.pixelSize*100)),(0-(app.pixelSize*100)),(0-(app.pixelSize*100)))
spawnPoint=Rect(app.centerx-(1.5*app.pixelSize),app.centery-(2.5*app.pixelSize),3*app.pixelSize,5*app.pixelSize,fill='blue')
roomGroup=Group(levelBorderA,spawnPoint)
# Rect(0,0,400,400,opacity=50)
undoneGroup=Group()
undoneGroup.visible=False
undoArrays=[]
levelList=[
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]]
inventory={"Torch":0}
character=Line(app.centerx,(app.centery-2.5*app.pixelSize),app.centerx,(app.centery+2.5*app.pixelSize),fill='red',lineWidth=(3*app.pixelSize))
shapeBorderA=Polygon(fill=None)
for i in levelBorderA.pointList:
    shapeBorderA.addPoint(rounded(i[0]),rounded(i[1]))
graphicGroup=Group(shapeBorderA)
app.lightRadius=35*app.sizeMulti
app.darkLevel=0
darkGroup=Group()
for i in range(5):
    darkGroup.add(Rect(0,0,app.width,app.height,opacity=app.darkLevel))
darkGroup.opacity=app.darkLevel
torchGroup=Group()
torchGroup.add(Polygon())
for i in levelBorderA.pointList:
    torchGroup.children[0].addPoint(i[0],i[1])
# t=Torch(200,100,75)
portalSign=Rect(-100*app.sizeMulti,-100*app.sizeMulti,5*app.pixelSize,7*app.pixelSize,fill='purple',opacity=50,visible=False)
#color buttons
app.graphicsColor=rgb(0,0,0)
app.r=0
app.g=0
app.b=0
red=Rect(5*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(255,0,0),border='black',borderWidth=2*app.sizeMulti)
darkred=Rect(5*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(139,0,0),border='black',borderWidth=2*app.sizeMulti)
orange=Rect(35*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(255,170,0),border='black',borderWidth=2*app.sizeMulti)
darkorange=Rect(35*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(240,100,0),border='black',borderWidth=2*app.sizeMulti)
yellow=Rect(65*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(255,255,0),border='black',borderWidth=2*app.sizeMulti)
gold=Rect(65*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(255,215,0),border='black',borderWidth=2*app.sizeMulti)
green=Rect(95*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(0,128,0),border='black',borderWidth=2*app.sizeMulti)
darkgreen=Rect(95*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(0,100,0),border='black',borderWidth=2*app.sizeMulti)
blue=Rect(125*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(0,0,255),border='black',borderWidth=2*app.sizeMulti)
darkblue=Rect(125*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(0,0,139),border='black',borderWidth=2*app.sizeMulti)
purple=Rect(155*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(128,0,128),border='black',borderWidth=2*app.sizeMulti)
indigo=Rect(155*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(75,0,130),border='black',borderWidth=2*app.sizeMulti)
pink=Rect(185*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(255,192,203),border='black',borderWidth=2*app.sizeMulti)
deeppink=Rect(185*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(255,20,147),border='black',borderWidth=2*app.sizeMulti)
sandybrown=Rect(215*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(244,164,96),border='black',borderWidth=2*app.sizeMulti)
saddlebrown=Rect(215*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(139,69,19),border='black',borderWidth=2*app.sizeMulti)
silver=Rect(245*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(192,192,192),border='black',borderWidth=2*app.sizeMulti)
dimgray=Rect(245*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(105,105,105),border='black',borderWidth=2*app.sizeMulti)
white=Rect(275*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(255,255,255),border='black',borderWidth=2*app.sizeMulti)
black=Rect(275*app.sizeMulti,350*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=rgb(0,0,0),border='dimgray',borderWidth=2*app.sizeMulti)
custom=Rect(305*app.sizeMulti,375*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill=gradient('red','orange','yellow','green','blue','purple',start='left-bottom'),border='black',borderWidth=2*app.sizeMulti)
current=Rect(5*app.sizeMulti,310*app.sizeMulti,35*app.sizeMulti,35*app.sizeMulti,fill=app.graphicsColor,border='black',borderWidth=2*app.sizeMulti)
colorGroup=Group(red,darkred,orange,darkorange,yellow,gold,green,darkgreen,blue,darkblue,purple,indigo,pink,deeppink,sandybrown,saddlebrown,silver,dimgray,white,black,custom,current)
colorGroup.visible=False
colorRGBDict={
    red:[255,0,0],darkred:[139,0,0],orange:[255,170,0],darkorange:[240,100,0],yellow:[255,255,0],
    gold:[255,215,0],green:[0,128,0],darkgreen:[0,100,0],blue:[0,0,255],darkblue:[0,0,139],
    purple:[128,0,128],indigo:[75,0,130],pink:[255,192,203],deeppink:[255,20,147],sandybrown:[244,164,96],
    saddlebrown:[139,69,19],silver:[192,192,192],dimgray:[105,105,105],white:[255,255,255],black:[0,0,0]
}
h1=Rect(5*app.sizeMulti,5*app.sizeMulti,45*app.sizeMulti,30*app.sizeMulti,fill='dodgerBlue',border='steelBlue',borderWidth=3*app.sizeMulti)
h2=Rect(20*app.sizeMulti,14*app.sizeMulti,16*app.sizeMulti,15*app.sizeMulti,fill=None,border='black',borderWidth=2*app.sizeMulti)
h3=Line(15*app.sizeMulti,20*app.sizeMulti,27*app.sizeMulti,9*app.sizeMulti,lineWidth=2*app.sizeMulti)
h4=Line(41*app.sizeMulti,20*app.sizeMulti,27*app.sizeMulti,9*app.sizeMulti,lineWidth=2*app.sizeMulti)
h5=Polygon(15*app.sizeMulti,20*app.sizeMulti,27*app.sizeMulti,9*app.sizeMulti,41*app.sizeMulti,20*app.sizeMulti,36*app.sizeMulti,20*app.sizeMulti,36*app.sizeMulti,29*app.sizeMulti,20*app.sizeMulti,29*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,15*app.sizeMulti,20*app.sizeMulti)
h6=Rect(25.5*app.sizeMulti,23*app.sizeMulti,5*app.sizeMulti,7*app.sizeMulti,fill='dodgerblue')
e1=Rect(70*app.sizeMulti,5*app.sizeMulti,30*app.sizeMulti,30*app.sizeMulti,fill='dodgerBlue',border='gold',borderWidth=2*app.sizeMulti)
e2=Rect(80*app.sizeMulti,7.5*app.sizeMulti,10*app.sizeMulti,20*app.sizeMulti,rotateAngle=45,fill='gold')
e3=Polygon(81.5*app.sizeMulti,29*app.sizeMulti,73*app.sizeMulti,28.5*app.sizeMulti,74.7*app.sizeMulti,21.5*app.sizeMulti)
e4=Rect(78*app.sizeMulti,18*app.sizeMulti,5*app.sizeMulti,10*app.sizeMulti,rotateAngle=140,fill='yellow')
play=Rect(355*app.sizeMulti,365*app.sizeMulti,40*app.sizeMulti,30*app.sizeMulti,fill='red',border='darkred',borderWidth=2*app.sizeMulti)
play2=RegularPolygon(375*app.sizeMulti,380*app.sizeMulti,12*app.sizeMulti,3,rotateAngle=90,fill='white',border='gray',borderWidth=2*app.sizeMulti)
play3=Arc(375*app.sizeMulti,380*app.sizeMulti,24*app.sizeMulti,24*app.sizeMulti,110*app.sizeMulti,320,border=None,fill=None)
play4=Circle(375*app.sizeMulti,380*app.sizeMulti,10*app.sizeMulti,fill=None)
play5=RegularPolygon(385*app.sizeMulti,385*app.sizeMulti,4*app.sizeMulti,3,fill=None,rotateAngle=30)
tempGraphicsButton=Rect(120*app.sizeMulti,5*app.sizeMulti,30*app.sizeMulti,30*app.sizeMulti,fill='dodgerBlue',border='black',borderWidth=2*app.sizeMulti)
tempGraphicsButtonLine=Line(132.5*app.sizeMulti,10*app.sizeMulti,125*app.sizeMulti,20*app.sizeMulti,lineWidth=2*app.sizeMulti)
tempGraphicsButtonCircle=Circle(140*app.sizeMulti,15*app.sizeMulti,5*app.sizeMulti)
tempGraphicsButtonRect=Rect(128.75*app.sizeMulti,22.5*app.sizeMulti,12.5*app.sizeMulti,7.5*app.sizeMulti)
room1=Rect(5*app.sizeMulti,45*app.sizeMulti,30*app.sizeMulti,30*app.sizeMulti,fill='paleturquoise',border='darkred',borderWidth=2*app.sizeMulti)
room2=Rect(15*app.sizeMulti,55*app.sizeMulti,10*app.sizeMulti,10*app.sizeMulti,fill=None,border='black',borderWidth=1*app.sizeMulti)
room3=Line(10*app.sizeMulti,55*app.sizeMulti,30*app.sizeMulti,55*app.sizeMulti,lineWidth=2*app.sizeMulti)
room4=Line(10*app.sizeMulti,65*app.sizeMulti,30*app.sizeMulti,65*app.sizeMulti,lineWidth=2*app.sizeMulti)
room5=Line(15*app.sizeMulti,50*app.sizeMulti,15*app.sizeMulti,70*app.sizeMulti,lineWidth=2*app.sizeMulti)
room6=Line(25*app.sizeMulti,50*app.sizeMulti,25*app.sizeMulti,70*app.sizeMulti,lineWidth=2*app.sizeMulti)
ll=Rect(170*app.sizeMulti,5*app.sizeMulti,30*app.sizeMulti,30*app.sizeMulti,fill='gray',border='steelblue',borderWidth=2*app.sizeMulti)
ll1=Circle(188*app.sizeMulti,20*app.sizeMulti,10*app.sizeMulti,fill='white')
ll2=Oval(193*app.sizeMulti,20*app.sizeMulti,12*app.sizeMulti,20*app.sizeMulti,fill='gray')
buttonGroupAll=Group(
    h1,h2,h3,h4,h5,h6,e1,e2,e3,e4,
    play,play2,play3,play4,play5,
    tempGraphicsButton,tempGraphicsButtonLine,tempGraphicsButtonCircle,tempGraphicsButtonRect,
    room1,room2,room3,room4,room5,room6,ll,ll1,ll2)
cg1=Rect(370*app.sizeMulti,335*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='skyblue',border='steelblue',borderWidth=2*app.sizeMulti)
cg2=Oval(380*app.sizeMulti,355*app.sizeMulti,8*app.sizeMulti,4*app.sizeMulti,fill='navy')
cg3=Rect(380*app.sizeMulti,339*app.sizeMulti,10*app.sizeMulti,7*app.sizeMulti,fill='blue')
cg4=Line(380*app.sizeMulti,355*app.sizeMulti,380*app.sizeMulti,339*app.sizeMulti,fill='gray',lineWidth=2*app.sizeMulti)
ch1=Rect(370*app.sizeMulti,300*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='peru',border='gold',borderWidth=2*app.sizeMulti)
ch2=Line(375*app.sizeMulti,320*app.sizeMulti,390*app.sizeMulti,305*app.sizeMulti,lineWidth=2*app.sizeMulti)
ch3=Rect(383*app.sizeMulti,301*app.sizeMulti,7*app.sizeMulti,16*app.sizeMulti,rotateAngle=-45)
ca1=Rect(370*app.sizeMulti,265*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='gainsboro',border='dimGray',borderWidth=2*app.sizeMulti)
ca2=Star(382*app.sizeMulti,277*app.sizeMulti,10*app.sizeMulti,7,fill='red',border='yellow',borderWidth=1.5*app.sizeMulti)
cd1=Rect(370*app.sizeMulti,230*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='seagreen',border='navy',borderWidth=2*app.sizeMulti)
cd2=Rect(377*app.sizeMulti,233*app.sizeMulti,12*app.sizeMulti,20*app.sizeMulti,fill='deeppink',border='pink',rotateAngle=45,borderWidth=2*app.sizeMulti)
cr1=Rect(370*app.sizeMulti,195*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='black',border='crimson',borderWidth=2*app.sizeMulti)
cr2=Oval(383*app.sizeMulti,207.5*app.sizeMulti,12*app.sizeMulti,20*app.sizeMulti,fill='purple')
cr3=Oval(383*app.sizeMulti,207.5*app.sizeMulti,9*app.sizeMulti,16*app.sizeMulti,fill='navy')
cr4=Oval(383*app.sizeMulti,207.5*app.sizeMulti,6*app.sizeMulti,10*app.sizeMulti,fill='darkOrchid')
lc=Rect(370*app.sizeMulti,160*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='gray',border='deepPink',borderWidth=2*app.sizeMulti)
lc1=Line(377*app.sizeMulti,167*app.sizeMulti,377*app.sizeMulti,182*app.sizeMulti,lineWidth=2*app.sizeMulti)
lc2=Line(389*app.sizeMulti,167*app.sizeMulti,389*app.sizeMulti,182*app.sizeMulti,lineWidth=2*app.sizeMulti)
lc3=Line(377*app.sizeMulti,172*app.sizeMulti,389*app.sizeMulti,172*app.sizeMulti,lineWidth=2*app.sizeMulti)
lc4=Line(377*app.sizeMulti,178*app.sizeMulti,389*app.sizeMulti,178*app.sizeMulti,lineWidth=2*app.sizeMulti)
rp=Rect(370*app.sizeMulti,90*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='blue',border='gray',borderWidth=2*app.sizeMulti)
rp1=Line(390*app.sizeMulti,96*app.sizeMulti,382*app.sizeMulti,108*app.sizeMulti,fill='green',lineWidth=3*app.sizeMulti)
rp2=Line(382*app.sizeMulti,108*app.sizeMulti,375*app.sizeMulti,104*app.sizeMulti,fill='green',lineWidth=4*app.sizeMulti)
tb=Rect(370*app.sizeMulti,125*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='dimGray',border='purple',borderWidth=2*app.sizeMulti)
tb1=Line(382.5*app.sizeMulti,132.5*app.sizeMulti,382.5*app.sizeMulti,145*app.sizeMulti,fill='saddlebrown',lineWidth=2*app.sizeMulti)
tb2=Circle(382.5*app.sizeMulti,132.5*app.sizeMulti,5*app.sizeMulti,fill=gradient('orange','yellow'),opacity=50)
buttonGroupEditor=Group(cg1,cg2,cg3,cg4,ch1,ch2,ch3,ca1,ca2,cd1,cd2,cr1,cr2,cr3,cr4,lc,lc1,lc2,lc3,lc4,rp,rp1,rp2,tb,tb1,tb2)
# buttonGroupEditor.visible=False
# hitboxToggle
tempCircleButton=Rect(370*app.sizeMulti,335*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='white',border='black',borderWidth=2*app.sizeMulti)
tempCircleButtonCircle=Circle(382.5*app.sizeMulti,347.5*app.sizeMulti,7.5*app.sizeMulti,fill='black')
tempRectButton=Rect(370*app.sizeMulti,300*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='white',border='black',borderWidth=2*app.sizeMulti)
tempRectButtonRect=Rect(375*app.sizeMulti,305*app.sizeMulti,15*app.sizeMulti,15*app.sizeMulti,fill='black')
tempLineButton=Rect(370*app.sizeMulti,265*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='white',border='gold',borderWidth=2*app.sizeMulti)
tempLineButtonLine=Line(375*app.sizeMulti,270*app.sizeMulti,390*app.sizeMulti,285*app.sizeMulti,fill='black',lineWidth=2*app.sizeMulti)
buttonGroupGraphics=Group(tempCircleButton,tempCircleButtonCircle,tempRectButton,tempRectButtonRect,tempLineButton,tempLineButtonLine)
buttonGroupGraphics.visible=False
menuBack=Rect(25*app.sizeMulti,25*app.sizeMulti,350*app.sizeMulti,350*app.sizeMulti,border='darkred',fill='paleturquoise',borderWidth=2*app.sizeMulti)
room00=Rect(140*app.sizeMulti,140*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='black',fill='paleturquoise',borderWidth=1*app.sizeMulti)
room01=Rect(180*app.sizeMulti,140*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='black',fill='paleturquoise',borderWidth=1*app.sizeMulti)
room02=Rect(220*app.sizeMulti,140*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='black',fill='paleturquoise',borderWidth=1*app.sizeMulti)
room10=Rect(140*app.sizeMulti,180*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='black',fill='paleturquoise',borderWidth=1*app.sizeMulti)
room11=Rect(180*app.sizeMulti,180*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='black',fill='dodgerblue',borderWidth=1*app.sizeMulti)
room12=Rect(220*app.sizeMulti,180*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='black',fill='paleturquoise',borderWidth=1*app.sizeMulti)
room20=Rect(140*app.sizeMulti,220*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='black',fill='paleturquoise',borderWidth=1*app.sizeMulti)
room21=Rect(180*app.sizeMulti,220*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='black',fill='paleturquoise',borderWidth=1*app.sizeMulti)
room22=Rect(220*app.sizeMulti,220*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='black',fill='paleturquoise',borderWidth=1*app.sizeMulti)
gridBorder=Rect(140*app.sizeMulti,140*app.sizeMulti,120*app.sizeMulti,120*app.sizeMulti,border='black',fill=None,borderWidth=1*app.sizeMulti)
selected=Rect(180*app.sizeMulti,180*app.sizeMulti,40*app.sizeMulti,40*app.sizeMulti,border='gold',fill=None,borderWidth=2*app.sizeMulti)
exitBox=Rect(350*app.sizeMulti,30*app.sizeMulti,20*app.sizeMulti,20*app.sizeMulti,fill='paleTurquoise',border='darkred',borderWidth=2*app.sizeMulti)
exit=Star(360*app.sizeMulti,40*app.sizeMulti,10*app.sizeMulti,4,fill='darkred',rotateAngle=45,roundness=25)
gridGroup=Group(menuBack,room00,room01,room02,room10,room11,room12,room20,room21,room22,gridBorder,selected,exitBox,exit)
gridGroup.visible=False
app.score=0
score=Label(app.score,380*app.sizeMulti,30*app.sizeMulti,fill='blue')
scoreLabel=Label("Score: ",350*app.sizeMulti,30*app.sizeMulti,fill='blue')
# pauseButton=Rect(370*app.sizeMulti,335*app.sizeMulti,25*app.sizeMulti,25*app.sizeMulti,fill='red',border='darkred',borderWidth=2*app.sizeMulti)
# pauseButton2=Line(374.5*app.sizeMulti,347.5*app.sizeMulti,390.5*app.sizeMulti,347.5*app.sizeMulti,fill='white',dashes=True,lineWidth=15*app.sizeMulti)
# pauseButton3=RegularPolygon(380*app.sizeMulti,347.5*app.sizeMulti,10*app.sizeMulti,3*app.sizeMulti,fill='white',border='gray',rotateAngle=90,borderWidth=2*app.sizeMulti)
buttonGroupRunning=Group(score,scoreLabel)
buttonGroupRunning.visible=False
backGround=Rect(0,0,400*app.sizeMulti,400*app.sizeMulti,fill=gradient('darkOrchid','slateBlue','slateBlue','steelblue','steelblue','steelblue'))
a=Label('Play',200*app.sizeMulti,280*app.sizeMulti,fill=gradient('white','azure','aliceBlue',start='left'),size=20*app.sizeMulti,font='orbitron')
b=Label('Settings',200*app.sizeMulti,320*app.sizeMulti,fill=gradient('white','azure','aliceBlue',start='left'),size=20*app.sizeMulti,font='orbitron')
c=Label('Instuctions',200*app.sizeMulti,360*app.sizeMulti,fill=gradient('white','azure','aliceBlue',start='left'),size=20*app.sizeMulti,font='orbitron')
a1=Label('>Play<',200*app.sizeMulti,280*app.sizeMulti,fill=gradient('white','azure','aliceBlue',start='left'),size=20*app.sizeMulti,font='orbitron',visible=False)
b1=Label('>Settings<',200*app.sizeMulti,320*app.sizeMulti,fill=gradient('white','azure','aliceBlue',start='left'),size=20*app.sizeMulti,font='orbitron',visible=False)
c1=Label('>Instuctions<',200*app.sizeMulti,360*app.sizeMulti,fill=gradient('white','azure','aliceBlue',start='left'),size=20*app.sizeMulti,font='orbitron',visible=False)
title=Label('The Unnamed Platformer',200*app.sizeMulti,150*app.sizeMulti,size=25*app.sizeMulti,font='orbitron',bold=True,italic=True)
homeGroup=Group(backGround,a,b,c,a1,b1,c1,title)

backGround2=Rect(0,0,400*app.sizeMulti,400*app.sizeMulti,fill=gradient('slategray','gray','slategray',start='left'))
lon=Line(200*app.sizeMulti,0,200*app.sizeMulti,400*app.sizeMulti,lineWidth=2*app.sizeMulti)
lon1=Label('New Game',100*app.sizeMulti,50*app.sizeMulti,font='orbitron',size=20*app.sizeMulti,fill='silver')
lon2=Label('Load File',300*app.sizeMulti,50*app.sizeMulti,font='orbitron',size=20*app.sizeMulti,fill='silver')
lon3=Rect(50*app.sizeMulti,150*app.sizeMulti,100*app.sizeMulti,150*app.sizeMulti,fill='white',border='silver',borderWidth=2*app.sizeMulti)
lon4=Rect(250*app.sizeMulti,150*app.sizeMulti,100*app.sizeMulti,150*app.sizeMulti,fill='white',border='silver',borderWidth=2*app.sizeMulti)
lon5=Line(300*app.sizeMulti,100*app.sizeMulti,300*app.sizeMulti,220*app.sizeMulti,arrowStart=True,lineWidth=10*app.sizeMulti,dashes=True,fill='forestGreen')
playScreenGroup=Group(backGround2,lon,lon1,lon2,lon3,lon4,lon5)
playScreenGroup.visible=False
loadScreen=Rect(0,0,400*app.sizeMulti,400*app.sizeMulti,fill='gray')
LoadingOutLine=Rect(120*app.sizeMulti,190*app.sizeMulti,160*app.sizeMulti,20*app.sizeMulti,fill=None,border='black',borderWidth=2*app.sizeMulti)
LoadingInLine=Line(123*app.sizeMulti,200*app.sizeMulti,130*app.sizeMulti,200*app.sizeMulti,lineWidth=15*app.sizeMulti,fill='red')
Instructions1=Label('N: New Level',200*app.sizeMulti,240*app.sizeMulti,fill='blue',size=12*app.sizeMulti)
Instructions2=Label('S: Show Save Code|L: Insert Save Code',200*app.sizeMulti,260*app.sizeMulti,fill='blue',size=12*app.sizeMulti)
Instructions4=Label('Shift+Z: Undo|Shift+Y: Redo|Arrow Keys: Move/Pan',200*app.sizeMulti,300*app.sizeMulti,fill='blue',size=12*app.sizeMulti)
Instructions5=Label('Click and Drag to Create Collision While in Editor Mode',200*app.sizeMulti,320*app.sizeMulti,fill='blue',size=12*app.sizeMulti)
Instructions6=Label('Click and Drag to Create Graphics While in Graphics Mode',200*app.sizeMulti,340*app.sizeMulti,fill='blue',size=12*app.sizeMulti)
loadingGroup=Group(
    loadScreen,LoadingOutLine,LoadingInLine,
    Instructions1,Instructions2,Instructions4,Instructions5,Instructions6)
buttonList=[buttonGroupAll,buttonGroupEditor,buttonGroupRunning,buttonGroupGraphics,colorGroup,gridGroup]
# loading=Arc(200*app.sizeMulti,200*app.sizeMulti,50*app.sizeMulti,50*app.sizeMulti,1*app.sizeMulti,1*app.sizeMulti,opacity=50,fill=None,border='blue',borderWidth=2*app.sizeMulti)
# cover=Circle(200*app.sizeMulti,200*app.sizeMulti,20*app.sizeMulti,fill='white')
# app properties
app.airTime=0
app.cheat=False
app.wallJump=False
app.dash=True
app.dashing=False
app.dashTime=0
app.jumpTime=0
app.jumpMax=13
app.falling=True
# direction: True=Right; False=Left
app.direction=True
app.dashCooldown=20
app.onWall=False
app.down=False
app.gamePause=False
app.drop=True
app.stepsPerSecond=40
app.shapex1=0
app.shapey1=0
app.shapex2=0
app.shapey2=0
app.horizontalMove=0
app.verticalMove=0
app.blockType='1'
app.shapeType='Line'
app.mode='editor'
app.creating=False
app.modeChanged=False
app.mousePressed=False
app.hitboxes=True
app.gridFalse=False
app.roomX=1
app.roomY=1
app.choosingRoom=False
app.start=True
app.portals=0
app.onLadder=False
app.moveH=0
app.moveV=0
Label('Ver 1.1.3',360*app.sizeMulti,10*app.sizeMulti,size=15*app.sizeMulti,fill='blue')
# encode/decode save code
def makeFourDigits(string,number):
    if len(number)==1:
        string+="000"+number
    elif len(number)==2:
        string+="00"+number
    elif len(number)==3:
        string+="0"+number
    else:
        string+=number
    return string
def makeThreeDigits(string,number):
    if len(number)==1:
        string+="00"+number
    elif len(number)==2:
        string+="0"+number
    else:
        string+=number
    return string
def compress(string):
    index=0
    compressed=""
    while index!=len(string):
        count=1
        while (index<len(string)-1) and (string[index]==string[index+1]):
            count+=1
            index+=1
        compressed+=str(string[index])
        compressed=makeFourDigits(compressed,str(count))
        index+=1
    return compressed
def unCompress(string):
    unCompressed=""
    index=0
    while index<len(string):
        i=0
        n=""
        n+=string[index+1]+string[index+2]+string[index+3]+string[index+4]
        while i<int(n):
            unCompressed+=string[index]
            i+=1
        index+=5
    return unCompressed
def loadShapes(string,levelGroup,levelBorder):
    roomGroup.add(spawnPoint)
    index=0
    while index<len(string):
        levelBorderA.centerX=app.centerx
        levelBorderA.centerY=app.centery
        # change so that shape is made based on middle
        left=""
        left+=string[index]+string[index+1]+string[index+2]+string[index+3]
        top=""
        top+=string[index+4]+string[index+5]+string[index+6]+string[index+7]
        width=""
        width+=string[index+8]+string[index+9]+string[index+10]+string[index+11]
        height=""
        height+=string[index+12]+string[index+13]+string[index+14]+string[index+15]
        if string[index+16]=="1":
            roomGroup.add(Rect(levelBorderA.left+((int(left)*app.pixelSize)),levelBorderA.top+(int(top)*app.pixelSize),int(width)*app.pixelSize,int(height)*app.pixelSize))
            roomGroup.children[len(roomGroup.children)-1].block='1'
        elif string[index+16]=="0":
            roomGroup.add(Rect(levelBorderA.left+((int(left)*app.pixelSize)),levelBorderA.top+(int(top)*app.pixelSize),int(width)*app.pixelSize,int(height)*app.pixelSize,fill='white'))
            roomGroup.children[len(roomGroup.children)-1].block='0'
        elif string[index+16]=="2":
            roomGroup.add(Rect(levelBorderA.left+((int(left)*app.pixelSize)),levelBorderA.top+(int(top)*app.pixelSize),int(width)*app.pixelSize,int(height)*app.pixelSize,fill='orange'))
            roomGroup.children[len(roomGroup.children)-1].block='2'
        elif string[index+16]=="3":
            roomGroup.add(Rect(levelBorderA.left+((int(left)*app.pixelSize)),levelBorderA.top+(int(top)*app.pixelSize),int(width)*app.pixelSize,int(height)*app.pixelSize,fill='yellow'))
            roomGroup.children[len(roomGroup.children)-1].block='3'
        elif string[index+16]=="p":
            roomGroup.add(Portal(levelBorderA.left+((int(left)*app.pixelSize)),levelBorderA.top+(int(top)*app.pixelSize)).shape)
        elif string[index+16]=="l":
            roomGroup.add(Ladder(levelBorderA.left+((int(left)*app.pixelSize)),levelBorderA.top+(int(top)*app.pixelSize)).shape)
        elif string[index+16]=="s":
            spawnPoint.top=levelBorderA.top+(int(top)*app.pixelSize)
            spawnPoint.left=levelBorderA.left+(int(left)*app.pixelSize)
        index+=17
def saveShapes(levelGroup,levelBorder):
    string="."
    left=""
    top=""
    width=""
    height=""
    left+=str(rounded(distance(levelBorderA.left,0,spawnPoint.left,0)/app.pixelSize))
    top+=str(rounded(distance(0,levelBorderA.top,0,spawnPoint.top)/app.pixelSize))
    width+=str(rounded(spawnPoint.width/app.pixelSize))
    height+=str(rounded(spawnPoint.height/app.pixelSize))
    string=makeFourDigits(string,left)
    string=makeFourDigits(string,top)
    string=makeFourDigits(string,width)
    string=makeFourDigits(string,height)
    string+="s"
    for i in roomGroup:
        if i!=levelBorderA and i!=spawnPoint:
            levelBorderA.centerX=app.centerx
            levelBorderA.centerY=app.centery
            # change so that shape is made based on middle
            left=""
            top=""
            width=""
            height=""
            left+=str(rounded(distance(levelBorderA.left,0,i.left,0)/app.pixelSize))
            top+=str(rounded(distance(0,levelBorderA.top,0,i.top)/app.pixelSize))
            width+=str(rounded(i.width/app.pixelSize))
            height+=str(rounded(i.height/app.pixelSize))
            string=makeFourDigits(string,left)
            string=makeFourDigits(string,top)
            string=makeFourDigits(string,width)
            string=makeFourDigits(string,height)
            if i.block=='0':
                string+="0"
            elif i.block=='1':
                string+="1"
            elif i.block=='2':
                string+="2"
            elif i.block=='3':
                string+="3"
            elif i.block=='p':
                string+="p"
            elif i.block=='l':
                string+="l"
    return string
def saveGraphics(graphicsGroup,shapeBorder):
    string="."
    for i in graphicsGroup:
        if i!=shapeBorder:
            if i.type=='Rect':
                string+='R'
                left=str(rounded(distance(shapeBorder.left,0,i.left,0)))
                top=str(rounded(distance(0,shapeBorder.top,0,i.top)))
                width=str(rounded(i.width))
                height+=str(rounded(i.height))
                string=makeFourDigits(string,left)
                string=makeFourDigits(string,top)
                string=makeFourDigits(string,width)
                string=makeFourDigits(string,height)
            elif i.type=='Circle':
                string+='C'
                centerX=str(rounded(distance(graphicsBorder.left,0,i.centerX,0)))
                centerY=str(rounded(distance(0,graphicsBorder.top,0,i.centerY)))
                radius=str(rounded(i.radius))
                string=makeFourDigits(string,centerX)
                string=makeFourDigits(string,centerY)
                string=makeFourDigits(string,radius)
            elif i.type=='Line':
                string+='L'
                x1=str(rounded(distance(shapeBorder.left,0,i.x1,0)))
                y1=str(rounded(distance(0,shapeBorder.top,0,i.y1)))
                x2=str(rounded(distance(shapeBorder.left,0,i.x2,0)))
                y2=str(rounded(distance(0,shapeBorder.top,0,i.y2)))
                string=makeFourDigits(string,x1)
                string=makeFourDigits(string,y1)
                string=makeFourDigits(string,x2)
                string=makeFourDigits(string,y2)
            color=[str(i.r),str(i.g),str(i.b)]
            for a in color:
                string=makeThreeDigits(string,a)
            color.clear()
    return string
def loadGraphics(string,graphicsGroup,graphicsBorder):
    index=0
    while index<len(string):
        if string[index]=='R':
            left=graphicsBorder.left+int(string[index+1]+string[index+2]+string[index+3]+string[index+4])
            top=graphicsBorder.top+int(string[index+5]+string[index+6]+string[index+7]+string[index+8])
            width=int(string[index+9]+string[index+10]+string[index+11]+string[index+12])
            height=int(string[index+13]+string[index+14]+string[index+15]+string[index+16])
            r=int(string[index+17]+string[index+18]+string[index+19])
            g=int(string[index+20]+string[index+21]+string[index+22])
            b=int(string[index+23]+string[index+24]+string[index+25])
            graphicsGroup.add(Rect(left,top,width,height,fill=rgb(r,g,b)))
            graphicsGroup.children[len(graphicsGroup.children)-1].type='Rect'
            graphicsGroup.children[len(graphicsGroup.children)-1].r=r
            graphicsGroup.children[len(graphicsGroup.children)-1].g=g
            graphicsGroup.children[len(graphicsGroup.children)-1].b=b
            index+=26
        elif string[index]=='C':
            centerX=graphicsBorder.left+int(string[index+1]+string[index+2]+string[index+3]+string[index+4])
            centerY=graphicsBorder.top+int(string[index+5]+string[index+6]+string[index+7]+string[index+8])
            radius=int(string[index+9]+string[index+10]+string[index+11]+string[index+12])
            r=int(string[index+13]+string[index+14]+string[index+15])
            g=int(string[index+16]+string[index+17]+string[index+18])
            b=int(string[index+19]+string[index+20]+string[index+21])
            graphicsGroup.add(Circle(centerX,centerY,radius,fill=rgb(r,g,b)))
            graphicsGroup.children[len(graphicsGroup.children)-1].type='Circle'
            graphicsGroup.children[len(graphicsGroup.children)-1].r=r
            graphicsGroup.children[len(graphicsGroup.children)-1].g=g
            graphicsGroup.children[len(graphicsGroup.children)-1].b=b
            index+=22
        elif string[index]=='L':
            x1=graphicsBorder.left+int(string[index+1]+string[index+2]+string[index+3]+string[index+4])
            y1=graphicsBorder.top+int(string[index+5]+string[index+6]+string[index+7]+string[index+8])
            x2=graphicsBorder.left+int(string[index+9]+string[index+10]+string[index+11]+string[index+12])
            y2=graphicsBorder.top+int(string[index+13]+string[index+14]+string[index+15]+string[index+16])
            r=int(string[index+17]+string[index+18]+string[index+19])
            g=int(string[index+20]+string[index+21]+string[index+22])
            b=int(string[index+23]+string[index+24]+string[index+25])
            graphicsGroup.add(Line(x1,y1,x2,y2,fill=rgb(r,g,b)))
            graphicsGroup.children[len(graphicsGroup.children)-1].type='Line'
            graphicsGroup.children[len(graphicsGroup.children)-1].r=r
            graphicsGroup.children[len(graphicsGroup.children)-1].g=g
            graphicsGroup.children[len(graphicsGroup.children)-1].b=b
            index+=26
# level creation
def loadFile(array,original,levelGroup,levelBorder,graphicsGroup,shapeBorder,code):
    app.gamePause=True
    loadingGroup.visible=True
    LoadingInLine.x2=130*app.sizeMulti
    # clears everything
    roomGroup.clear()
    original.clear()
    array.clear()
    graphicsGroup.clear()
    # adds levelborder, recenters
    roomGroup.visible=True
    roomGroup.add(levelBorderA)
    graphicsGroup.visible=True
    graphicsGroup.add(shapeBorder)
    # takes in a code
    codeList=code.split(".")
    code2=codeList[0].strip("'").strip("[").strip("]")
    levelCode=unCompress(code2[6:])
    if len(codeList)>1:
        shapeCode=codeList[1].strip("'").strip("[").strip("]")
    if len(codeList)>2:
        graphicsCode=codeList[2].strip("'").strip("[").strip("]")
    width=int(code2[:3])-100
    height=int(code2[3:6])-100
    x1=0-(app.pixelSize*((width-99)/2))
    x2=app.width+(app.pixelSize*((width-99)/2))
    x3=0-(app.pixelSize*((width-99)/2))-(50*app.pixelSize)
    x4=app.width+(app.pixelSize*((width-99)/2))+(50*app.pixelSize)
    y1=0-(app.pixelSize*((height-99)/2))
    y2=app.height+(app.pixelSize*((height-99)/2))
    y3=0-(app.pixelSize*((height-99)/2))-(50*app.pixelSize)
    y4=app.height+(app.pixelSize*((height-99)/2))+(50*app.pixelSize)
    levelBorderA.pointList=[[x1,y1],[x2,y1],[x2,y2],[x1,y2],[x1,y1],[x3,y3],[x3,y4],[x4,y4],[x4,y3],[x3,y3]]
    graphicsGroup.children[0].pointList=[[rounded(x1),rounded(y1)],[rounded(x2),rounded(y1)],[rounded(x2),rounded(y2)],[rounded(x1),rounded(y2)],[rounded(x1),rounded(y1)],[rounded(x3),rounded(y3)],[rounded(x3),rounded(y4)],[rounded(x4),rounded(y4)],[rounded(x4),rounded(y3)],[rounded(x3),rounded(y3)]]
    loadShapes(shapeCode,roomGroup,levelBorderA)
    loadGraphics(graphicsCode,graphicsGroup,shapeBorder)
    l=int(code2[3:6])
    a=0
    while a<l:
        array.append([])
        original.append([])
        a+=1
    a=0
    for i in levelCode:
        if i!='8':
            array[a].append(i)
            original[a].append(i)
        else:
            a+=1
def exportSave(array,original,levelGroup,levelBorder,graphicsGroup,shapeBorder):
    # prints code to copy
    loadingGroup.visible=True
    LoadingInLine.x2=130*app.sizeMulti
    app.mode='editor'
    roomGroup.centerX=app.centerx
    roomGroup.centerY=app.centery
    graphicsGroup.centerX=app.centerx
    graphicsGroup.centerY=app.centery
    saveCode=""
    # adds all elements from the "original" array to a string, with a '8' to seperate the rows
    for row in original:
        for i in row:
            saveCode+=i
        saveCode+='8'
    a=""
    a=makeThreeDigits(a,str(len(original)))
    a=makeThreeDigits(a,str(len(original[0])))
    
    c=compress(saveCode)
    s=saveShapes(roomGroup,levelBorderA)
    g=saveGraphics(graphicsGroup,shapeBorder)
    acsg=a+c+s+g
    if app.choosingRoom==False:
        app.getTextInput(acsg)
    else:
        return acsg
def runLevel(array,original,levelGroup,graphicsGroup):
    app.gamePause=True
    loadingGroup.visible=True
    LoadingInLine.x2=130*app.sizeMulti
    app.mode='running'
    # recentering
    roomGroup.centerX=app.centerx
    roomGroup.centerY=app.centery
    character.centerX=app.centerx
    character.centerY=app.centery
    graphicsGroup.centerX=app.centerx
    graphicsGroup.centerY=app.centery
    arrayCopy(array,original)
    xDis=int(distance(character.centerX,0,spawnPoint.centerX,0)/app.pixelSize)
    yDis=int(distance(0,character.centerY,0,spawnPoint.centerY)/app.pixelSize)
    x=0
    y=0
    while x<xDis:
        if character.centerX<spawnPoint.centerX:
            moveRight(array,roomGroup,graphicsGroup)
            app.moveH+=1
        elif character.centerX>spawnPoint.centerX:
            moveLeft(array,roomGroup,graphicsGroup)
            app.moveH-=1
        x+=1
    while y<yDis:
        if character.centerY<spawnPoint.centerY:
            moveDown(array,roomGroup,graphicsGroup)
            app.moveV+=1
        elif character.centerY>spawnPoint.centerY:
            moveUp(array,roomGroup,graphicsGroup)
            app.moveV-=1
        y+=1
def newLevel(array,original,levelGroup,levelBorder,graphicsGroup,shapeBorder,width,height):
    # clears, recenters
    array.clear()
    original.clear()
    roomGroup.clear()
    levelBorderA.centerX=app.centerx
    levelBorderA.centerY=app.centery
    levelBorderA.visible=True
    roomGroup.add(levelBorderA)
    roomGroup.add(spawnPoint)
    roomGroup.add(Rect(levelBorderA.left+app.pixelSize,levelBorderA.top+app.pixelSize,app.pixelSize,app.pixelSize))
    roomGroup.children[len(roomGroup.children)-1].block='1'
    roomGroup.centerX=app.centerx
    roomGroup.centerY=app.centery
    graphicsGroup.centerX=app.centerx
    graphicsGroup.centerY=app.centery
    graphicsGroup.clear()
    graphicsGroup.add(shapeBorder)
    graphicsGroup.add(Line(shapeBorder.left+1*app.sizeMulti,shapeBorder.top+1*app.sizeMulti,shapeBorder.left+2*app.sizeMulti,shapeBorder.top+2*app.sizeMulti,fill=rgb(0,0,0)))
    graphicsGroup.children[len(graphicsGroup.children)-1].type='Line'
    graphicsGroup.children[len(graphicsGroup.children)-1].r=0
    graphicsGroup.children[len(graphicsGroup.children)-1].g=0
    graphicsGroup.children[len(graphicsGroup.children)-1].b=0
    app.gamePause=True
    loadingGroup.visible=True
    LoadingInLine.x2=130*app.sizeMulti
    app.mode='editor'
    # constructs blank arrays
    a=0
    while a<100+height:
        array.append([])
        a+=1
    a=0
    while a<50:
        b=0
        while b<100+width:
            array[a].append('1')
            b+=1
        a+=1
    while a<height+50:
        b=0
        while b<50:
            array[a].append('1')
            b+=1
        while b<width+50:
            array[a].append('0')
            b+=1
        while b<width+100:
            array[a].append('1')
            b+=1
        a+=1
    while a<height+100:
        b=0
        while b<width+100:
            array[a].append('1')
            b+=1
        a+=1
    a=0
    while a<height+100:
        original.append([])
        a+=1
    a=0
    while a<50:
        b=0
        while b<width+100:
            original[a].append('1')
            b+=1
        a+=1
    while a<height+50:
        b=0
        while b<50:
            original[a].append('1')
            b+=1
        while b<width+50:
            original[a].append('0')
            b+=1
        while b<width+100:
            original[a].append('1')
            b+=1
        a+=1
    while a<height+100:
        b=0
        while b<width+100:
            original[a].append('1')
            b+=1
        a+=1
def shapeSet(original,levelGroup,levelBorder):
    if app.mode=='editor':
        if shapeBlockList[len(shapeBlockList)-1]!='p' and shapeBlockList[len(shapeBlockList)-1]!='t' and shapeBlockList[len(shapeBlockList)-1]!='s':
            roomGroup.children[len(roomGroup.children)-1].left=roomGroup.children[0].left+(rounded(distance(roomGroup.children[0].left,0,roomGroup.children[len(roomGroup.children)-1].left,0)/app.pixelSize)*app.pixelSize)
            roomGroup.children[len(roomGroup.children)-1].right=roomGroup.children[0].left+(rounded(distance(roomGroup.children[0].left,0,roomGroup.children[len(roomGroup.children)-1].right,0)/app.pixelSize)*app.pixelSize)
            roomGroup.children[len(roomGroup.children)-1].top=roomGroup.children[0].top+(rounded(distance(0,roomGroup.children[0].top,0,roomGroup.children[len(roomGroup.children)-1].top)/app.pixelSize)*app.pixelSize)
            roomGroup.children[len(roomGroup.children)-1].bottom=roomGroup.children[0].top+(rounded(distance(0,roomGroup.children[0].top,0,roomGroup.children[len(roomGroup.children)-1].bottom)/app.pixelSize)*app.pixelSize)
        elif shapeBlockList[len(shapeBlockList)-1]=='p':
            roomGroup.children[len(roomGroup.children)-1].left=roomGroup.children[0].left+(rounded(distance(roomGroup.children[0].left,0,roomGroup.children[len(roomGroup.children)-1].left,0)/app.pixelSize)*app.pixelSize)
            roomGroup.children[len(roomGroup.children)-1].width=5*app.pixelSize
            roomGroup.children[len(roomGroup.children)-1].right=roomGroup.children[0].left+(rounded(distance(roomGroup.children[0].left,0,roomGroup.children[len(roomGroup.children)-1].right,0)/app.pixelSize)*app.pixelSize)
            roomGroup.children[len(roomGroup.children)-1].top=roomGroup.children[0].top+(rounded(distance(0,roomGroup.children[0].top,0,roomGroup.children[len(roomGroup.children)-1].top)/app.pixelSize)*app.pixelSize)
            roomGroup.children[len(roomGroup.children)-1].height=7*app.pixelSize
            roomGroup.children[len(roomGroup.children)-1].bottom=roomGroup.children[0].top+(rounded(distance(0,roomGroup.children[0].top,0,roomGroup.children[len(roomGroup.children)-1].bottom)/app.pixelSize)*app.pixelSize)
        elif shapeBlockList[len(shapeBlockList)-1]=='t':
            torchGroup.children[len(torchGroup.children)-1].centerX=torchGroup.children[0].left+(rounded(distance(0,torchGroup.children[0].left,0,torchGroup.children[len(torchGroup.children)-1].centerX)/app.pixelSize)*app.pixelSize)
            torchGroup.children[len(torchGroup.children)-1].centerY=torchGroup.children[0].top+(rounded(distance(0,torchGroup.children[0].top,0,torchGroup.children[len(torchGroup.children)-1].centerY)/app.pixelSize)*app.pixelSize)
            t=len(torchGroup)-1
            for i in torchList[len(torchList)-1].lightList:
                i.centerX=torchGroup.children[t].x1
                i.centerY=torchGroup.children[t].y1
                i.visible=True
                torchGroup.add(i)
        character.left=roomGroup.children[0].left+(rounded(distance(roomGroup.children[0].left,0,character.left,0)/app.pixelSize)*app.pixelSize)
        character.right=roomGroup.children[0].left+(rounded(distance(roomGroup.children[0].left,0,character.right,0)/app.pixelSize)*app.pixelSize)
        character.top=roomGroup.children[0].top+(rounded(distance(0,roomGroup.children[0].top,0,character.top)/app.pixelSize)*app.pixelSize)
        character.bottom=roomGroup.children[0].top+(rounded(distance(0,roomGroup.children[0].top,0,character.bottom)/app.pixelSize)*app.pixelSize)
        # checks to make sure shape is in valid position
        if roomGroup.children[len(roomGroup.children)-1].containsShape(character)==False:
            if app.blockType!='0' and app.blockType!='t':
                if character.left<=roomGroup.children[len(roomGroup.children)-1].left<character.right and roomGroup.children[len(roomGroup.children)-1].hitsShape(character):
                    if (not (roomGroup.children[len(roomGroup.children)-1].top<character.top and roomGroup.children[len(roomGroup.children)-1].bottom<=character.top)) and (not (roomGroup.children[len(roomGroup.children)-1].top>=character.bottom and roomGroup.children[len(roomGroup.children)-1].bottom>character.bottom)):
                        for i in portalList:
                            if roomGroup.children[len(roomGroup.children)-1] in i:
                                i.remove(roomGroup.children[len(roomGroup.children)-1])
                        if roomGroup.children[len(roomGroup.children)-1] in portalListSelf:
                            portalListSelf.remove(roomGroup.children[len(roomGroup.children)-1])
                        roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
                        return
                elif character.left<roomGroup.children[len(roomGroup.children)-1].right<=character.right and roomGroup.children[len(roomGroup.children)-1].hitsShape(character):
                    if (not (roomGroup.children[len(roomGroup.children)-1].top<character.top and roomGroup.children[len(roomGroup.children)-1].bottom<=character.top)) and (not (roomGroup.children[len(roomGroup.children)-1].top>=character.bottom and roomGroup.children[len(roomGroup.children)-1].bottom>character.bottom)):
                        for i in portalList:
                            if roomGroup.children[len(roomGroup.children)-1] in i:
                                i.remove(roomGroup.children[len(roomGroup.children)-1])
                        if roomGroup.children[len(roomGroup.children)-1] in portalListSelf:
                            portalListSelf.remove(roomGroup.children[len(roomGroup.children)-1])
                        roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
                        return
                elif character.top<=roomGroup.children[len(roomGroup.children)-1].top<character.bottom and roomGroup.children[len(roomGroup.children)-1].hitsShape(character):
                    if (not (roomGroup.children[len(roomGroup.children)-1].left<character.left and roomGroup.children[len(roomGroup.children)-1].left<=character.right)) and (not (roomGroup.children[len(roomGroup.children)-1].left>=character.right and roomGroup.children[len(roomGroup.children)-1].right>character.right)):
                        for i in portalList:
                            if roomGroup.children[len(roomGroup.children)-1] in i:
                                i.remove(roomGroup.children[len(roomGroup.children)-1])
                        if roomGroup.children[len(roomGroup.children)-1] in portalListSelf:
                            portalListSelf.remove(roomGroup.children[len(roomGroup.children)-1])
                        roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
                        return
                elif character.top<roomGroup.children[len(roomGroup.children)-1].bottom<=character.bottom and roomGroup.children[len(roomGroup.children)-1].hitsShape(character):
                    if (not (roomGroup.children[len(roomGroup.children)-1].left<character.left and roomGroup.children[len(roomGroup.children)-1].left<=character.right)) and (not (roomGroup.children[len(roomGroup.children)-1].left>=character.right and roomGroup.children[len(roomGroup.children)-1].right>character.right)):
                        for i in portalList:
                            if roomGroup.children[len(roomGroup.children)-1] in i:
                                i.remove(roomGroup.children[len(roomGroup.children)-1])
                        if roomGroup.children[len(roomGroup.children)-1] in portalListSelf:
                            portalListSelf.remove(roomGroup.children[len(roomGroup.children)-1])
                        roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
                        return
            if (app.blockType!='1' and app.blockType!='t'):
                if (((roomGroup.children[len(roomGroup.children)-1].top<roomGroup.pointList[0][1] or roomGroup.children[len(roomGroup.children)-1].bottom<roomGroup.pointList[0][1]) and (roomGroup.children[len(roomGroup.children)-1].top>=levelBorderA.pointList[5][1] or roomGroup.children[len(roomGroup.children)-1].bottom>=levelBorderA.pointList[5][1]))):
                    for i in portalList:
                        if roomGroup.children[len(roomGroup.children)-1] in i:
                            i.remove(roomGroup.children[len(roomGroup.children)-1])
                    if roomGroup.children[len(roomGroup.children)-1] in portalListSelf:
                        portalListSelf.remove(roomGroup.children[len(roomGroup.children)-1])
                    roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
                    return
                elif (((roomGroup.children[len(roomGroup.children)-1].left<levelBorderA.pointList[0][0] or roomGroup.children[len(roomGroup.children)-1].right<levelBorderA.pointList[0][0]) and (roomGroup.children[len(roomGroup.children)-1].left>=levelBorderA.pointList[5][0] or roomGroup.children[len(roomGroup.children)-1].right>=levelBorderA.pointList[5][0]))):
                    for i in portalList:
                        if roomGroup.children[len(roomGroup.children)-1] in i:
                            i.remove(roomGroup.children[len(roomGroup.children)-1])
                    if roomGroup.children[len(roomGroup.children)-1] in portalListSelf:
                        portalListSelf.remove(roomGroup.children[len(roomGroup.children)-1])
                    roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
                    return
                elif (((roomGroup.children[len(roomGroup.children)-1].left>levelBorderA.pointList[2][0] or roomGroup.children[len(roomGroup.children)-1].right>levelBorderA.pointList[2][0]) and (roomGroup.children[len(roomGroup.children)-1].left<=levelBorderA.pointList[7][0] or roomGroup.children[len(roomGroup.children)-1].right<=levelBorderA.pointList[7][0]))):
                    for i in portalList:
                        if roomGroup.children[len(roomGroup.children)-1] in i:
                            i.remove(roomGroup.children[len(roomGroup.children)-1])
                    if roomGroup.children[len(roomGroup.children)-1] in portalListSelf:
                        portalListSelf.remove(roomGroup.children[len(roomGroup.children)-1])
                    roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
                    return
                elif (((roomGroup.children[len(roomGroup.children)-1].top>levelBorderA.pointList[2][1] or roomGroup.children[len(roomGroup.children)-1].bottom>levelBorderA.pointList[2][1]) and (roomGroup.children[len(roomGroup.children)-1].top<=levelBorderA.pointList[7][1] or roomGroup.children[len(roomGroup.children)-1].bottom<=levelBorderA.pointList[7][1]))):
                    for i in portalList:
                        if roomGroup.children[len(roomGroup.children)-1] in i:
                            i.remove(roomGroup.children[len(roomGroup.children)-1])
                    if roomGroup.children[len(roomGroup.children)-1] in portalListSelf:
                        portalListSelf.remove(roomGroup.children[len(roomGroup.children)-1])
                    roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
                    return
            if shapeBlockList[len(shapeBlockList)-1]!='p' and shapeBlockList[len(shapeBlockList)-1]!='t':
                for i in portalListSelf:
                    if roomGroup.children[len(roomGroup.children)-1].hitsShape(i.shape):
                        if i.shape.visible==True:
                            roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
                            return
            # sets collision
            if shapeBlockList[len(shapeBlockList)-1]!='t': #and shapeBlockList[len(shapeBlockList)-1]!='s':
                a=False
                undoArrays.append([])
                if shapeBlockList[len(shapeBlockList)-1]!='s':
                    app.minX=rounded(distance(0,roomGroup.left,0,roomGroup.children[len(roomGroup.children)-1].left)/app.pixelSize)
                    app.maxX=rounded(distance(0,roomGroup.left,0,roomGroup.children[len(roomGroup.children)-1].right)/app.pixelSize)
                    app.minY=rounded(distance(0,roomGroup.top,0,roomGroup.children[len(roomGroup.children)-1].top)/app.pixelSize)
                    app.maxY=rounded(distance(0,roomGroup.top,0,roomGroup.children[len(roomGroup.children)-1].bottom)/app.pixelSize)
                else:
                    app.minX=rounded(distance(0,roomGroup.left,0,spawnPoint.left)/app.pixelSize)
                    app.maxX=rounded(distance(0,roomGroup.left,0,spawnPoint.right)/app.pixelSize)
                    app.minY=rounded(distance(0,roomGroup.top,0,spawnPoint.top)/app.pixelSize)
                    app.maxY=rounded(distance(0,roomGroup.top,0,spawnPoint.bottom)/app.pixelSize)
                app.minYSave=app.minY
                while app.minX<app.maxX:
                    undoArrays[len(undoArrays)-1].append([])
                    app.minY=app.minYSave
                    while app.minY<app.maxY:
                        undoArrays[len(undoArrays)-1][len(undoArrays[len(undoArrays)-1])-1].append(original[app.minY][app.minX])
                        if original[app.minY][app.minX]!="0" and shapeBlockList[len(shapeBlockList)-1]=="p":
                            a=True
                        if original[app.minY][app.minX]=="s":
                            a=True
                        original[app.minY][app.minX]=app.blockType
                        app.minY+=1
                    app.minX+=1
                if shapeBlockList[len(shapeBlockList)-1]!='s':
                    roomGroup.children[len(roomGroup.children)-1].levelX=roomGroup.centerX
                    roomGroup.children[len(roomGroup.children)-1].levelY=roomGroup.centerY
                    roomGroup.children[len(roomGroup.children)-1].roomX=app.roomX
                    roomGroup.children[len(roomGroup.children)-1].roomY=app.roomY
                else:
                    spawnPoint.levelX=roomGroup.centerX
                    spawnPoint.levelY=roomGroup.centerY
                    spawnPoint.roomX=app.roomX
                    spawnPoint.roomY=app.roomY
                if a==True:
                    undo(collisionArray,original,roomGroup,undoneGroup,graphicGroup)
                    return
            else:
                pass
        else:
            for i in portalList:
                if roomGroup.children[len(roomGroup.children)-1] in i:
                    i.remove(roomGroup.children[len(roomGroup.children)-1])
            if roomGroup.children[len(roomGroup.children)-1] in portalListSelf:
                portalListSelf.remove(roomGroup.children[len(roomGroup.children)-1])
            roomGroup.remove(roomGroup.children[len(roomGroup.children)-1])
    p=0
    for i in portalList:
        if len(i)==0 or len(i)==1:
            if p==0:
                p+=1
            else:
                portalList.remove(i)
    app.portals=len(portalList)-1
    p=0
    for i in portalList:
        if p>app.portals:
            portalList.remove(i)
        p+=1
def shapeDrag(levelGroup,x,y,graphicsGroup):
    app.creating=True
    # making shape's dimensions 
    if app.mode=='editor':
        if shapeBlockList[len(shapeBlockList)-1]=='p':
            app.shapex1=(rounded(distance(levelBorderA.left,0,x,0)/app.pixelSize)*app.pixelSize)
            app.shapey1=(rounded(distance(0,levelBorderA.top,0,y)/app.pixelSize)*app.pixelSize)
            if x>levelBorderA.left+app.shapex1:
                app.shapex1+=(app.pixelSize/2)
            elif x<levelBorderA.left+app.shapex1:
                app.shapex1-=(app.pixelSize/2)
            if y>levelBorderA.top+app.shapey1:
                app.shapey1+=(app.pixelSize/2)
            elif y<levelBorderA.top+app.shapey1:
                app.shapey1-=(app.pixelSize/2)
            roomGroup.children[len(roomGroup.children)-1].centerX=levelBorderA.left+app.shapex1
            roomGroup.children[len(roomGroup.children)-1].centerY=levelBorderA.top+app.shapey1
            portalSign.centerX=levelBorderA.left+app.shapex1
            portalSign.centerY=levelBorderA.top+app.shapey1
        elif shapeBlockList[len(shapeBlockList)-1]=='s':
            app.shapex1=(rounded(distance(levelBorderA.left,0,x,0)/app.pixelSize)*app.pixelSize)
            app.shapey1=(rounded(distance(0,levelBorderA.top,0,y)/app.pixelSize)*app.pixelSize)
            print(app.shapex1)
            print(app.shapey1)
            print(rounded(distance(levelBorderA.left,0,x,0)/app.pixelSize))
            print(rounded(distance(0,levelBorderA.top,0,y)/app.pixelSize))
            if x>levelBorderA.left+app.shapex1:
                app.shapex1-=(app.pixelSize/2)
            elif x<levelBorderA.left+app.shapex1:
                app.shapex1+=(app.pixelSize/2)
            if y>levelBorderA.top+app.shapey1:
                app.shapey1-=(app.pixelSize/2)
            elif y<levelBorderA.top+app.shapey1:
                app.shapey1+=(app.pixelSize/2)
            spawnPoint.centerX=levelBorderA.left+app.shapex1
            spawnPoint.centerY=levelBorderA.top+app.shapey1
        elif shapeBlockList[len(shapeBlockList)-1]=='t':
            app.shapex1=(rounded(distance(torchGroup.children[0].left,0,x,0)/app.pixelSize)*app.pixelSize)
            app.shapey1=(rounded(distance(0,torchGroup.children[0].top,0,y)/app.pixelSize)*app.pixelSize)
            if x>torchGroup.children[0].left+app.shapex1:
                app.shapex1+=(app.pixelSize/2)
            elif x<torchGroup.children[0].left+app.shapex1:
                app.shapex1-=(app.pixelSize/2)
            if y>torchGroup.children[0].top+app.shapey1:
                app.shapey1+=(app.pixelSize/2)
            elif y<torchGroup.children[0].top+app.shapey1:
                app.shapey1-=(app.pixelSize/2)
            torchGroup.children[len(torchGroup.children)-1].centerX=torchGroup.children[0].left+app.shapex1
            torchGroup.children[len(torchGroup.children)-1].centerY=torchGroup.children[0].top+app.shapey1
        else:
            app.shapex2=(rounded(distance(levelBorderA.left,0,x,0)/app.pixelSize)*app.pixelSize)
            app.shapey2=(rounded(distance(0,levelBorderA.top,0,y)/app.pixelSize)*app.pixelSize)
            if app.shapex1<app.shapex2:
                roomGroup.children[len(roomGroup.children)-1].left=levelBorderA.left+app.shapex1
            elif app.shapex1>app.shapex2:
                roomGroup.children[len(roomGroup.children)-1].left=levelBorderA.left+app.shapex2
            else:
                roomGroup.children[len(roomGroup.children)-1].left=levelBorderA.left+app.shapex1
                app.shapex2+=app.pixelSize
            if app.shapey1<app.shapey2:
                roomGroup.children[len(roomGroup.children)-1].top=levelBorderA.top+app.shapey1
            elif app.shapey1>app.shapey2:
                roomGroup.children[len(roomGroup.children)-1].top=levelBorderA.top+app.shapey2
            else:
                roomGroup.children[len(roomGroup.children)-1].top=levelBorderA.top+app.shapey1
                app.shapey2+=app.pixelSize
            roomGroup.children[len(roomGroup.children)-1].width=(rounded(distance(app.shapex1,0,app.shapex2,0)/app.pixelSize)*app.pixelSize)
            roomGroup.children[len(roomGroup.children)-1].height=(rounded(distance(0,app.shapey1,0,app.shapey2)/app.pixelSize)*app.pixelSize)
            roomGroup.children[len(roomGroup.children)-1].levelX=roomGroup.centerX
            roomGroup.children[len(roomGroup.children)-1].levelY=roomGroup.centerY
    elif app.mode=='graphics':
        if graphicsGroup.children[len(graphicsGroup.children)-1].type=='Rect':
            app.graphicsx2=rounded(x)
            app.graphicsy2=rounded(y)
            if 0<(x-app.graphicsx1):
                graphicsGroup.children[len(graphicsGroup.children)-1].left=app.graphicsx1
                graphicsGroup.children[len(graphicsGroup.children)-1].width=app.graphicsx2-app.graphicsx1
            elif 0>(x-app.graphicsx1):
                graphicsGroup.children[len(graphicsGroup.children)-1].left=app.graphicsx2
                graphicsGroup.children[len(graphicsGroup.children)-1].width=app.graphicsx1-app.graphicsx2
            if 0<(y-app.graphicsy1):
                graphicsGroup.children[len(graphicsGroup.children)-1].top=app.graphicsy1
                graphicsGroup.children[len(graphicsGroup.children)-1].height=app.graphicsy2-app.graphicsy1
            elif 0>(y-app.graphicsy1):
                graphicsGroup.children[len(graphicsGroup.children)-1].top=app.graphicsy2
                graphicsGroup.children[len(graphicsGroup.children)-1].height=app.graphicsy1-app.graphicsy2
        elif graphicsGroup.children[len(graphicsGroup.children)-1].type=='Circle':
            app.graphicsx2=rounded(graphicsGroup.children[0].left)+rounded(distance(graphicsGroup.children[0].left,0,x,0))
            app.graphicsy2=rounded(graphicsGroup.children[0].top)+rounded(distance(0,graphicsGroup.children[0].top,0,y))
            graphicsGroup.children[len(graphicsGroup.children)-1].radius=distance(app.graphicsx1,app.graphicsy1,app.graphicsx2,app.graphicsy2)+1
        elif graphicsGroup.children[len(graphicsGroup.children)-1].type=='Line':
            app.graphicsx2=rounded(graphicsGroup.children[0].left)+rounded(distance(graphicsGroup.children[0].left,0,x,0))
            app.graphicsy2=rounded(graphicsGroup.children[0].top)+rounded(distance(0,graphicsGroup.children[0].top,0,y))
            graphicsGroup.children[len(graphicsGroup.children)-1].x2=app.graphicsx2
            graphicsGroup.children[len(graphicsGroup.children)-1].y2=app.graphicsy2
def shapeStart(levelGroup,mouseX,mouseY,graphicsGroup):
    app.creating=True
    # creates shape
    if app.mode=='editor':
        app.shapex1=(rounded(distance(levelBorderA.left,0,mouseX,0)/app.pixelSize)*app.pixelSize)
        app.shapey1=(rounded(distance(0,levelBorderA.top,0,mouseY)/app.pixelSize)*app.pixelSize)
        app.shapex2=app.shapex1+app.pixelSize
        app.shapey2=app.shapey1+app.pixelSize
        if app.blockType=='1':
            roomGroup.add(Rect(levelBorderA.left+app.shapex1,levelBorderA.top+app.shapey1,app.pixelSize,app.pixelSize))
            roomGroup.children[len(roomGroup.children)-1].block='1'
            shapeBlockList.append('1')
        elif app.blockType=='2':
            roomGroup.add(Rect(levelBorderA.left+app.shapex1,levelBorderA.top+app.shapey1,app.pixelSize,app.pixelSize,fill='orange'))
            roomGroup.children[len(roomGroup.children)-1].block='2'
            shapeBlockList.append('2')
        elif app.blockType=='0':
            roomGroup.add(Rect(levelBorderA.left+app.shapex1,levelBorderA.top+app.shapey1,app.pixelSize,app.pixelSize,fill='white'))
            roomGroup.children[len(roomGroup.children)-1].block='0'
            shapeBlockList.append('0')
        elif app.blockType=='3':
            roomGroup.add(Rect(levelBorderA.left+app.shapex1,levelBorderA.top+app.shapey1,app.pixelSize,app.pixelSize,fill='yellow'))
            roomGroup.children[len(roomGroup.children)-1].block='3'
            shapeBlockList.append('3')
        elif app.blockType=='p':
            if mouseX>levelBorderA.left+app.shapex1:
                app.shapex1+=(app.pixelSize/2)
            elif mouseX<levelBorderA.left+app.shapex1:
                app.shapex1-=(app.pixelSize/2)
            if mouseY>levelBorderA.top+app.shapey1:
                app.shapey1+=(app.pixelSize/2)
            elif mouseY<levelBorderA.top+app.shapey1:
                app.shapey1-=(app.pixelSize/2)
            roomGroup.add(Portal(levelBorderA.left+app.shapex1-(2.5*app.pixelSize),levelBorderA.top+app.shapey1-(3.5*app.pixelSize)).shape)
            shapeBlockList.append('p')
        elif app.blockType=='l':
            roomGroup.add(Ladder(levelBorderA.left+app.shapex1,levelBorderA.top+app.shapey1).shape)
            shapeBlockList.append('l')
        elif app.blockType=='s':
            if mouseX>levelBorderA.left+app.shapex1:
                app.shapex1+=(app.pixelSize/2)
            elif mouseX<levelBorderA.left+app.shapex1:
                app.shapex1-=(app.pixelSize/2)
            if mouseY>levelBorderA.top+app.shapey1:
                app.shapey1+=(app.pixelSize/2)
            elif mouseY<levelBorderA.top+app.shapey1:
                app.shapey1-=(app.pixelSize/2)
            spawnPoint.centerX=levelBorderA.left+app.shapex1
            spawnPoint.centerY=levelBorderA.top+app.shapey1
            shapeBlockList.append('s')
        elif app.blockType=='t':
            torchGroup.add(Torch(levelBorderA.left+app.shapex1,levelBorderA.top+app.shapey1,app.lightRadius).shape)
            shapeBlockList.append('t')
    elif app.mode=='graphics':
        if app.shapeType=='Rect':
            app.graphicsx1=rounded(graphicsGroup.children[0].left)+rounded(distance(graphicsGroup.children[0].left,0,mouseX,0))
            app.graphicsy1=rounded(graphicsGroup.children[0].top)+rounded(distance(0,graphicsGroup.children[0].top,0,mouseY))
            app.graphicsx2=app.graphicsx1+1*app.sizeMulti
            app.graphicsy2=app.graphicsy1+1*app.sizeMulti
            graphicsGroup.add(Rect(mouseX,mouseY,1*app.sizeMulti,1*app.sizeMulti,fill=app.graphicsColor))
            graphicsGroup.children[len(graphicsGroup.children)-1].type='Rect'
            graphicsGroup.children[len(graphicsGroup.children)-1].r=app.r
            graphicsGroup.children[len(graphicsGroup.children)-1].g=app.g
            graphicsGroup.children[len(graphicsGroup.children)-1].b=app.b
        elif app.shapeType=='Circle':
            app.graphicsx1=rounded(graphicsGroup.children[0].left)+rounded(distance(graphicsGroup.children[0].left,0,mouseX,0))
            app.graphicsy1=rounded(graphicsGroup.children[0].top)+rounded(distance(0,graphicsGroup.children[0].top,0,mouseY))
            app.graphicsx2=app.graphicsx1+1*app.sizeMulti
            app.graphicsy2=app.graphicsy1+1*app.sizeMulti
            graphicsGroup.add(Circle(mouseX,mouseY,1*app.sizeMulti,fill=app.graphicsColor))
            graphicsGroup.children[len(graphicsGroup.children)-1].type='Circle'
            graphicsGroup.children[len(graphicsGroup.children)-1].r=app.r
            graphicsGroup.children[len(graphicsGroup.children)-1].g=app.g
            graphicsGroup.children[len(graphicsGroup.children)-1].b=app.b
        elif app.shapeType=='Line':
            app.graphicsx1=rounded(graphicsGroup.children[0].left)+rounded(distance(graphicsGroup.children[0].left,0,mouseX,0))
            app.graphicsy1=rounded(graphicsGroup.children[0].top)+rounded(distance(0,graphicsGroup.children[0].top,0,mouseY))
            app.graphicsx2=app.graphicsx1+1*app.sizeMulti
            app.graphicsy2=app.graphicsy1+1*app.sizeMulti
            graphicsGroup.add(Line(app.graphicsx1,app.graphicsy1,app.graphicsx2,app.graphicsy2,fill=app.graphicsColor))
            graphicsGroup.children[len(graphicsGroup.children)-1].type='Line'
            graphicsGroup.children[len(graphicsGroup.children)-1].r=app.r
            graphicsGroup.children[len(graphicsGroup.children)-1].g=app.g
            graphicsGroup.children[len(graphicsGroup.children)-1].b=app.b
def arrayCopy(array,original):
    # clears array
    array.clear()
    # adds empty rows
    a=0
    while a<len(original):
        array.append([])
        a+=1
    # for every element in "original", adds to array
    a=0
    while a<len(original):
        b=0
        while b<len(original[a]):
            array[a].append(original[a][b])
            b+=1
        a+=1
def respawn(array,original,levelGroup,graphicsGroup):
    app.dashing=False
    app.dashTime=0
    app.jumpTime=15
    app.falling=True
    app.airTime=0
    app.cheats=False
    character.centerX=app.centerx
    character.centerY=app.centery
    roomGroup.centerX=app.centerx
    roomGroup.centerY=app.centery
    torchGroup.centerX=app.centerx
    torchGroup.centerY=app.centery
    graphicsGroup.centerX=app.centerx
    graphicsGroup.centerY=app.centery
    arrayCopy(array,original)
def redo(array,original,levelGroup,undoGroup,graphicsGroup):
    if len(undoGroup.children)>0:
        roomGroup.centerX=undoGroup.children[len(undoGroup.children)-1].levelX
        roomGroup.centerY=undoGroup.children[len(undoGroup.children)-1].levelY
        graphicsGroup.centerX=undoGroup.children[len(undoGroup.children)-1].levelX
        graphicsGroup.centerY=undoGroup.children[len(undoGroup.children)-1].levelY
        character.centerX=undoGroup.children[len(undoGroup.children)-1].levelX
        character.centerY=undoGroup.children[len(undoGroup.children)-1].levelY
        app.minX=rounded(distance(0,roomGroup.left,0,undoGroup.children[len(undoGroup.children)-1].left)/app.pixelSize)
        app.maxX=rounded(distance(0,roomGroup.left,0,undoGroup.children[len(undoGroup.children)-1].right)/app.pixelSize)
        app.minY=rounded(distance(0,roomGroup.top,0,undoGroup.children[len(undoGroup.children)-1].top)/app.pixelSize)
        app.maxY=rounded(distance(0,roomGroup.top,0,undoGroup.children[len(undoGroup.children)-1].bottom)/app.pixelSize)
        app.minYSave=app.minY
        undoArrays.append([])
        while app.minX<app.maxX:
            app.minY=app.minYSave
            undoArrays[len(undoArrays)-1].append([])
            while app.minY<app.maxY:
                undoArrays[len(undoArrays)-1][len(undoArrays[len(undoArrays)-1])-1].append(original[app.minY][app.minX])
                original[app.minY][app.minX]=undoGroup.children[len(undoGroup.children)-1].block
                app.minY+=1
            app.minX+=1
        roomGroup.add(undoGroup.children[len(undoGroup.children)-1])
        if roomGroup.children[len(roomGroup.children)-1].block=='p' and len(portalList[app.portals])==1:
            portalList[app.portals].append(roomGroup.children[len(roomGroup.children)-1])
            app.portals+=1
        elif roomGroup.children[len(roomGroup.children)-1].block=='p':
            portalList[app.portals].append(roomGroup.children[len(roomGroup.children)-1])
        p=0
        for i in portalList:
            if len(i)==0 or len(i)==1:
                if p==0:
                    p+=1
                else:
                    portalList.remove(i)
        app.portals=len(portalList)-1
        p=0
        for i in portalList:
            if p>app.portals:
                portalList.remove(i)
            p+=1
def undo(array,original,levelGroup,undoGroup,graphicsGroup):
    if len(levelGroup.children)-1>1:
        levelGroup.centerX=levelGroup.children[len(levelGroup.children)-1].levelX
        levelGroup.centerY=levelGroup.children[len(levelGroup.children)-1].levelY
        graphicsGroup.centerX=levelGroup.children[len(levelGroup.children)-1].levelX
        graphicsGroup.centerY=levelGroup.children[len(levelGroup.children)-1].levelY
        character.centerX=levelGroup.children[len(levelGroup.children)-1].levelX
        character.centerY=levelGroup.children[len(levelGroup.children)-1].levelY
        app.minX=rounded(distance(0,levelGroup.left,0,levelGroup.children[len(levelGroup.children)-1].left)/app.pixelSize)
        app.maxX=rounded(distance(0,levelGroup.left,0,levelGroup.children[len(levelGroup.children)-1].right)/app.pixelSize)
        app.minY=rounded(distance(0,levelGroup.top,0,levelGroup.children[len(levelGroup.children)-1].top)/app.pixelSize)
        app.maxY=rounded(distance(0,levelGroup.top,0,levelGroup.children[len(levelGroup.children)-1].bottom)/app.pixelSize)
        app.minYSave=app.minY
        i=0
        while app.minX<app.maxX:
            j=0
            app.minY=app.minYSave
            while app.minY<app.maxY:
                original[app.minY][app.minX]=undoArrays[len(undoArrays)-1][i][j]
                app.minY+=1
                j+=1
            app.minX+=1
            i+=1
        undoArrays.pop()
        undoGroup.add(levelGroup.children[len(levelGroup.children)-1])
        if undoGroup.children[len(undoGroup.children)-1].block=='p' and len(portalList[app.portals])==0:
            onMousePress(380*app.sizeMulti,205*app.sizeMulti)
            app.portals-=1
            portalList[app.portals].pop()
        elif undoGroup.children[len(undoGroup.children)-1].block=='p':
            portalList[app.portals].pop()
            for i in buttonList:
                i.opacity=100
        p=0
        for i in portalList:
            if len(i)==0 or len(i)==1:
                if p==0:
                    p+=1
                else:
                    portalList.remove(i)
        app.portals=len(portalList)-1
        p=0
        for i in portalList:
            if p>app.portals:
                portalList.remove(i)
            p+=1
def resize(array,original,levelGroup,levelBorder,graphicsGroup,shapeBorder):
    warning=app.getTextInput("This will create a new level, are you sure? (yes/no)")
    if warning[0].lower()!='y':
        return False
    width=int("0"+(app.getTextInput("Insert a new width (Must be a odd # from 101 to 699):").split(".")[0]))
    if width%2==0 or width<=99 or width>699:
        app.getTextInput("INVALID WIDTH")
        return False
    height=int("0"+(app.getTextInput("Insert a new height (Must be a odd # from 101 to 699):").split(".")[0]))
    if height%2==0 or height<=99 or height>699:
        app.getTextInput("INVALID HEIGHT")
        return False
    roomGroup.clear()
    roomGroup.add(levelBorderA)
    x1=0-(app.pixelSize*((width-99)/2))
    x2=app.width+(app.pixelSize*((width-99)/2))
    x3=0-(app.pixelSize*((width-99)/2))-(50*app.pixelSize)
    x4=app.width+(app.pixelSize*((width-99)/2))+(50*app.pixelSize)
    y1=0-(app.pixelSize*((height-99)/2))
    y2=app.height+(app.pixelSize*((height-99)/2))
    y3=0-(app.pixelSize*((height-99)/2))-(50*app.pixelSize)
    y4=app.height+(app.pixelSize*((height-99)/2))+(50*app.pixelSize)
    print(x1)
    print(x2)
    print(x3)
    print(x4)
    print(y1)
    print(y2)
    print(y3)
    print(y4)
    levelBorderA.pointList=[[x1,y1],[x2,y1],[x2,y2],[x1,y2],[x1,y1],[x3,y3],[x3,y4],[x4,y4],[x4,y3],[x3,y3]]
    graphicsGroup.clear()
    graphicsGroup.add(shapeBorder)
    graphicsGroup.children[0].pointList=[[rounded(x1),rounded(y1)],[rounded(x2),rounded(y1)],[rounded(x2),rounded(y2)],[rounded(x1),rounded(y2)],[rounded(x1),rounded(y1)],[rounded(x3),rounded(y3)],[rounded(x3),rounded(y4)],[rounded(x4),rounded(y4)],[rounded(x4),rounded(y3)],[rounded(x3),rounded(y3)]]
    newLevel(array,original,roomGroup,levelBorder,graphicsGroup,shapeBorder,width,height)
def roomSwitchEdit(roomArray,array,original,levelGroup,levelBorder,graphicsGroup,shapeBorder,x,y):
    app.choosingRoom=True
    roomArray[app.roomY][app.roomX]=exportSave(array,original,roomGroup,levelBorderA,graphicsGroup,shapeBorder)
    app.choosingRoom=False
    app.roomX=x
    app.roomY=y
    loadFile(array,original,roomGroup,levelBorderA,graphicsGroup,shapeBorder,str(roomArray[app.roomY][app.roomX]).strip("'").strip("[").strip("]"))
    LoadingInLine.x2=130*app.sizeMulti
    undoneGroup.clear()
    undoArrays.clear()
    loadingGroup.visible=True
    app.gamePause=True
    
# move array
def moveRight(array,levelGroup,graphicsGroup):
    # moves array right, moves graphics left
    for i in array:
        i.append(i[0])
        i.remove(i[0])
    if (not (rounded(levelGroup.children[0].pointList[2][0]-app.pixelSize)<app.width)) and character.centerX==app.centerx:
        levelGroup.centerX-=app.pixelSize
        graphicsGroup.centerX-=app.pixelSize
        torchGroup.centerX-=app.pixelSize
    else:
        character.centerX+=app.pixelSize
def moveLeft(array,levelGroup,graphicsGroup):
    # moves array left, moves graphics right
    for i in array:
        i.insert(0,i[len(i)-1])
        del i[len(i)-1]
    if (not (rounded(levelGroup.children[0].pointList[0][0]+app.pixelSize)>0)) and character.centerX==app.centerx:
        levelGroup.centerX+=app.pixelSize
        graphicsGroup.centerX+=app.pixelSize
        torchGroup.centerX+=app.pixelSize
    else:
        character.centerX-=app.pixelSize
def moveDown(array,levelGroup,graphicsGroup):
    array.append(array[0])
    array.remove(array[0])
    if (not (rounded(levelGroup.children[0].pointList[2][1]-app.pixelSize)<app.height)) and character.centerY==app.centery:
        levelGroup.centerY-=app.pixelSize
        graphicsGroup.centerY-=app.pixelSize
        torchGroup.centerY-=app.pixelSize
    else:
        character.centerY+=app.pixelSize
def moveUp(array,levelGroup,graphicsGroup):
    array.insert(0,array[len(array)-1])
    del array[len(array)-1]
    if (not (rounded(levelGroup.children[0].pointList[0][1]+app.pixelSize)>0)) and character.centerY==app.centery:
        levelGroup.centerY+=app.pixelSize
        graphicsGroup.centerY+=app.pixelSize
        torchGroup.centerY+=app.pixelSize
    else:
        character.centerY-=app.pixelSize
# collision checking
def collisionCheck(array,xPos,yPos,xDis,yDis,blockType,equals):
    x=0
    if xDis==0 and yDis!=0:
        y=0
        while y<yDis:
            if equals==True:
                if array[int(len(array)/2-0.5+yPos+y)][int(len(array[int(len(array)/2-0.5+yPos+y)])/2-0.5+xPos)]==blockType:
                    y+=1
                else:
                    return False
            else:
                if array[int(len(array)/2-0.5+yPos+y)][int(len(array[int(len(array)/2-0.5+yPos+y)])/2-0.5+xPos)]!=blockType:
                    y+=1
                else:
                    return False
        return True
    if yDis==0 and xDis!=0:
        while x<xDis:
            if equals==True:
                if array[int(len(array)/2-0.5+yPos)][int(len(array[int(len(array)/2-0.5+yPos)])/2-0.5+xPos+x)]==blockType:
                    x+=1
                else:
                    return False
            else:
                if array[int(len(array)/2-0.5+yPos)][int(len(array[int(len(array)/2-0.5+yPos)])/2-0.5+xPos+x)]!=blockType:
                    x+=1
                else:
                    return False
        return True
    while x<xDis:
        y=0
        while y<yDis:
            if equals==True:
                if array[int(len(array)/2-0.5+yPos+y)][int(len(array[int(len(array)/2-0.5+yPos+y)])/2-0.5+xPos+x)]==blockType:
                    y+=1
                else:
                    return False
            else:
                if array[int(len(array)/2-0.5+yPos+y)][int(len(array[int(len(array)/2-0.5+yPos+y)])/2-0.5+xPos+x)]!=blockType:
                    y+=1
                else:
                    return False
        x+=1
    return True
def transitionCheck():
    return
    if character.left<=levelBorderA.pointList[0][0] and app.roomX!=0:
        roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,app.roomX-1,app.roomY)
        runLevel(collisionArray,editArray,roomGroup,graphicGroup)
        while app.moveH<0:
            moveRight(collisionArray,roomGroup,graphicGroup)
            app.moveH+=1
        while app.moveV<0:
            moveUp(collisionArray,roomGroup,graphicGroup)
            app.moveV+=1
        while app.moveV>0:
            moveDown(collisionArray,roomGroup,graphicGroup)
            app.moveV-=1
    elif character.right>=levelBorderA.pointList[2][0] and app.roomX!=len(levelList[app.roomY])-1:
        roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,app.roomX+1,app.roomY)
        runLevel(collisionArray,editArray,roomGroup,graphicGroup)
        while app.moveH>0:
            moveLeft(collisionArray,roomGroup,graphicGroup)
            app.moveH-=1
        while app.moveV<0:
            moveUp(collisionArray,roomGroup,graphicGroup)
            app.moveV+=1
        while app.moveV>0:
            moveDown(collisionArray,roomGroup,graphicGroup)
            app.moveV-=1
    elif character.top<=levelBorderA.pointList[0][1] and app.roomY!=0:
        # roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,app.roomX,app.roomY-1)
        pass
    elif character.bottom>=levelBorderA.pointList[2][1] and app.roomY!=len(levelList)-1:
        # roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,app.roomX,app.roomY+1)
        pass
# character movement
def jump(array,original,levelGroup,graphicsGroup):
    # does things depending on what character would be jumping into
    i=0
    while i<2:
        if collisionCheck(array,-1,-3,3,0,'1',False)==True:
            if collisionCheck(array,-1,-3,3,0,'2',False)==True:
                if collisionCheck(array,-1,-3,3,0,'3',False)==True:
                    moveUp(array,levelGroup,graphicsGroup)
                    app.moveV-=1
                else:
                    respawn(array,original,levelGroup,graphicsGroup)
                    score.value+=1
                    break
            else:
                respawn(array,original,levelGroup,graphicsGroup)
                break
        i+=1
def gravity(array,original,levelGroup,graphicsGroup):
    i=0
    while i<2:
        if collisionCheck(array,-1,3,3,0,'1',False)==True:
            if collisionCheck(array,-1,3,3,0,'2',False)==True:
                if collisionCheck(array,-1,3,3,0,'3',False)==True:
                    moveDown(array,levelGroup,graphicsGroup)
                    app.moveV+=1
                else:
                    respawn(array,original,levelGroup,graphicsGroup)
                    score.value+=1
                    break
            else:
                respawn(array,original,levelGroup,graphicsGroup)
                break
        else:
            app.falling=False
            app.down=False
            break
        i+=1
    app.drop=True
def dashLeft(array,original,levelGroup,graphicsGroup):
    # does things depending on what character would be dashing into
    i=0
    while i<5:
        if collisionCheck(array,-2,-2,0,5,'1',False)==True:
            if collisionCheck(array,-2,-2,0,5,'2',False)==True:
                if collisionCheck(array,-2,-2,0,5,'3',False)==True:
                    moveLeft(array,levelGroup,graphicsGroup)
                    app.moveH-=1
                else:
                    respawn(array,original,levelGroup,graphicsGroup)
                    score.value+=1
                    break
            else:
                respawn(array,original,levelGroup,graphicsGroup)
                break
        else:
            app.dashing=False
            app.dashTime=0
            break
        i+=1
def dashRight(array,original,levelGroup,graphicsGroup):
    # does things depending on what character would be dashing into
    i=0
    while i<5:
        if collisionCheck(array,2,-2,0,5,'1',False)==True:
            if collisionCheck(array,2,-2,0,5,'2',False)==True:
                if collisionCheck(array,2,-2,0,5,'3',False)==True:
                    moveRight(array,levelGroup,graphicsGroup)
                    app.moveH+=1
                else:
                    respawn(array,original,levelGroup,graphicsGroup)
                    score.value+=1
                    break
            else:
                respawn(array,original,levelGroup,graphicsGroup)
                break
        else:
            app.dashing=False
            app.dashTime=0
            break
        i+=1
def fall(array,original,levelGroup,graphicsGroup):
    if app.jumpTime==0 and app.airTime<=0 and app.dashTime<=0 and app.onLadder==False:
        if app.onWall==True:
            if collisionCheck(array,-1,3,3,0,'1',False)==True:
                if collisionCheck(array,-1,3,3,0,'2',False)==True:
                    if collisionCheck(array,-1,3,3,0,'3',False)==True:
                        moveDown(array,levelGroup,graphicsGroup)
                        app.moveV+=1
                        app.falling=True
                    else:
                        respawn(array,original,levelGroup,graphicsGroup)
                        score.value+=1
                else:
                    respawn(array,original,levelGroup,graphicsGroup)
            else:
                app.falling=False
                app.down=False
        else:
            gravity(array,original,levelGroup,graphicsGroup)
    if app.airTime>0:
        app.airTime-=1
        if collisionCheck(array,-1,3,3,0,'1',False)==True:
            if collisionCheck(array,-1,3,3,0,'2',False)==True:
                if collisionCheck(array,-1,3,3,0,'3',False)==True:
                    moveDown(array,levelGroup,graphicsGroup)
                    app.moveV+=1
                else:
                    respawn(array,original,levelGroup,graphicsGroup)
                    score.value+=1
            else:
                respawn(array,original,levelGroup,graphicsGroup)
        else:
            app.airTime=0
            app.jumpTime=0
        if app.airTime<=0:
            app.jumpTime=0
def wallCheck(array,original):
    if (array[int((len(array)/2)+1.5)][int((len(array[int((len(array)/2)-2.5)])/2)+1.5)]=="1" or array[int((len(array)/2)+0.5)][int((len(array[int((len(array)/2)-2.5)])/2)+1.5)]=="1" or array[int((len(array)/2)-0.5)][int((len(array[int((len(array)/2)-2.5)])/2)+1.5)]=="1" or 
    array[int((len(array)/2)-1.5)][int((len(array[int((len(array)/2)-2.5)])/2)+1.5)]=="1" or array[int((len(array)/2)-2.5)][int((len(array[int((len(array)/2)-2.5)])/2)+1.5)]=="1" or array[int((len(array)/2)+1.5)][int((len(array[int((len(array)/2)-2.5)])/2)-2.5)]=="1" or 
    array[int((len(array)/2)+0.5)][int((len(array[int((len(array)/2)-2.5)])/2)-2.5)]=="1" or array[int((len(array)/2)-0.5)][int((len(array[int((len(array)/2)-2.5)])/2)-2.5)]=="1" or array[int((len(array)/2)-1.5)][int((len(array[int((len(array)/2)-2.5)])/2)-2.5)]=="1" or 
    array[int((len(array)/2)-2.5)][int((len(array[int((len(array)/2)-2.5)])/2)-2.5)]=="1"):
        if app.down==False:
            app.onWall=True
    else:
        app.onWall=False
        app.down=False
def dashing(array,original,levelGroup,graphicsGroup):
    if app.dash==True:
        if app.dashTime>0:
            if app.dashTime%2==0:
                if app.direction==False:
                    dashLeft(array,original,levelGroup,graphicsGroup)
                if app.direction==True:
                    dashRight(array,original,levelGroup,graphicsGroup)
            app.dashTime-=1
        if app.dashTime<=0:
            app.dashing=False
        if app.dashing==False:
            if app.dashCooldown>0 and (array[int((len(array)/2)+2.5)][int((len(array[int((len(array)/2)+2.5)])/2)+0.5)]=="1" or array[int((len(array)/2)+2.5)][int((len(array[int((len(array)/2)+2.5)])/2)-0.5)]=="1" or array[int((len(array)/2)+2.5)][int((len(array[int((len(array)/2)+2.5)])/2)-1.5)]=="1"):
                app.dashCooldown-=1
def movement(array,original,levelGroup,keys,graphicsGroup): 
    if app.gamePause==False:
        if app.dashing==False:
            if app.mode=='running':
                # move character
                if 'left' in keys:
                    app.direction=False
                    if collisionCheck(array,-2,-2,0,5,'1',False)==True:
                        if collisionCheck(array,-2,-2,0,5,'2',False)==True:
                            if collisionCheck(array,-2,-2,0,5,'3',False)==True:
                                moveLeft(array,levelGroup,graphicsGroup)
                                transitionCheck()
                                app.moveH-=1
                            else:
                                respawn(array,original,levelGroup,graphicsGroup)
                                score.value+=1
                        else:
                            respawn(array,original,levelGroup,graphicsGroup)
                if 'right' in keys:
                    app.direction=True
                    if collisionCheck(array,2,-2,0,5,'1',False)==True:
                        if collisionCheck(array,2,-2,0,5,'2',False)==True:
                            if collisionCheck(array,2,-2,0,5,'3',False)==True:
                                moveRight(array,levelGroup,graphicsGroup)
                                app.moveH+=1
                            else:
                                respawn(array,original,levelGroup,graphicsGroup)
                                score.value+=1
                        else:
                            respawn(array,original,levelGroup,graphicsGroup)
                # jump
                if 'up' in keys:
                    if app.falling==False and app.onLadder==False:
                        jump(array,original,levelGroup,graphicsGroup)
                        app.jumpTime+=1
                        if app.cheat==True:
                            if app.jumpTime==50000:
                                app.airTime=5
                                app.falling=True
                        else:
                            if app.jumpTime>=app.jumpMax:
                                app.airTime=5
                                app.falling=True
                    elif app.onLadder==True:
                        app.airTime=0
                        app.falling=False
                        app.jumpTime=0
                        if collisionCheck(array,-1,-3,3,0,'1',False)==True:
                            if collisionCheck(array,-1,-3,3,0,'2',False)==True:
                                if collisionCheck(array,-1,-3,3,0,'3',False)==True:
                                    moveUp(array,levelGroup,graphicsGroup)
                                    app.moveV-=1
                                else:
                                    respawn(array,original,levelGroup,graphicsGroup)
                                    score.value+=1
                            else:
                                respawn(array,original,levelGroup,graphicsGroup)
                    app.drop=False
                if 'down' in keys:
                    if app.onLadder==True:
                        app.falling=True
                        app.drop=True
                        app.onLadder=False
                        app.down=False
            else:
                if 'up' in keys:
                    if not (levelBorderA.top+app.pixelSize>0):
                        levelGroup.centerY+=app.pixelSize
                        graphicsGroup.centerY+=app.pixelSize
                        character.centerY+=app.pixelSize
                        torchGroup.centerY+=app.pixelSize
                if 'down' in keys:
                    if not (levelBorderA.bottom-app.pixelSize<app.height):
                        levelGroup.centerY-=app.pixelSize
                        graphicsGroup.centerY-=app.pixelSize
                        character.centerY-=app.pixelSize
                        torchGroup.centerY-=app.pixelSize
                if 'right' in keys:
                    if not (levelBorderA.right-app.pixelSize<app.width):
                        levelGroup.centerX-=app.pixelSize
                        graphicsGroup.centerX-=app.pixelSize
                        character.centerX-=app.pixelSize
                        torchGroup.centerX-=app.pixelSize
                if 'left' in keys:
                    if not (levelBorderA.left+app.pixelSize>0):
                        levelGroup.centerX+=app.pixelSize
                        graphicsGroup.centerX+=app.pixelSize
                        character.centerX+=app.pixelSize
                        torchGroup.centerX+=app.pixelSize
# game
def onKeyHold(keys):
    movement(collisionArray,editArray,roomGroup,keys,graphicGroup)
def onStep():
    if len(portalList[app.portals])!=0:
        if len(portalList[app.portals])==2 and app.creating==False:
            for i in buttonList:
                i.opacity=100
        else:
            for i in buttonList:
                i.opacity=70
    else:
        if app.creating==False:
            for i in buttonList:
                i.opacity=100
    if app.start==True:
        app.start=False
        resize(collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA)
        app.choosingRoom=True
        for i in levelList:
            for r in i:
                r.append(exportSave(collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA))
        app.choosingRoom=False
    if app.gamePause==True:
        loadingGroup.visible=True
        # Loading screen

        if LoadingInLine.x2<272*app.sizeMulti:
            LoadingInLine.x2+=(149*app.sizeMulti/299*app.sizeMulti)*5*app.sizeMulti
        else:
            loadingGroup.visible=False
            app.gamePause=False
    elif app.gamePause==False:
        if app.mode=='running':
            fall(collisionArray,editArray,roomGroup,graphicGroup)
            wallCheck(collisionArray,editArray)
            dashing(collisionArray,editArray,roomGroup,graphicGroup)
            if app.modeChanged==False:
                roomGroup.opacity=100
                graphicGroup.opacity=100
                spawnPoint.fill=None
                app.modeChanged=True
                darkGroup.visible=True
                homeGroup.visible=False
            for i in portalListSelf:
                if character.hitsShape(i.shape) and i.shape.transported==False and i.shape.visible==True:
                    i.teleport()
                if character.hitsShape(i.shape)==False:
                    i.shape.transported=False
            for i in ladderList:
                if character.hitsShape(i):
                    # if app.drop==False:
                    app.onLadder=True
                    if app.drop==True:
                        app.onLadder=False
                    break
                else:
                    app.onLadder=False
            # if app.drop==True:
            #     for i in ladderList:
            #         if i.hitsShape(character):
            #             app.onLadder=False
            #             break
        elif app.mode=='graphics':
            if app.modeChanged==False:
                for i in roomGroup:
                    if i.fill!='white':
                        i.opacity=35
                graphicGroup.opacity=80
                spawnPoint.fill='blue'
                app.modeChanged=True
                darkGroup.visible=False
                homeGroup.visible=False
        elif app.mode=='editor':
            if app.modeChanged==False:
                roomGroup.opacity=100
                graphicGroup.opacity=35
                spawnPoint.fill='blue'
                app.modeChanged=True
                darkGroup.visible=False
                homeGroup.visible=False
def onKeyRelease(key):
    #Start Falling
    if key=='up':
        if app.onLadder==False:
            if app.cheat==False:
                app.airTime=5
                app.falling=True
            else:
                app.jumpTime=0
def onKeyPress(key):
    if app.creating==False:
        if app.gamePause==False:
            if app.mode=='running':
                if app.dash==True:
                    # Dash
                    if key=='space':
                        if app.dashCooldown==0:
                            app.dashCooldown=2
                            app.dashing=True
                            app.dashTime=9
                            app.airTime=5
                            app.falling=True
                            if app.direction==False:
                                dashLeft(collisionArray,editArray,roomGroup,graphicGroup)
                            elif app.direction==True:
                                dashRight(collisionArray,editArray,roomGroup,graphicGroup)
            if app.onWall==True:
                # fall down wall
                if key=='down':
                    if app.onLadder==False:
                        app.onWall=False
                        app.down=True
            if key=='C':
                if app.cheat==False:
                    app.cheat=True
                else:
                    app.cheat=False
            if key=='D':
                if app.dash==False:
                    app.dash=True
                else:
                    app.dash=False
        # save/export saved level
        if key=='s':
            loadingGroup.visible=True
            LoadingInLine.x2=130*app.sizeMulti
            exportSave(collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA)
        # start game
        if key=='n':
            loadingGroup.visible=True
            LoadingInLine.x2=130*app.sizeMulti
            resize(collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA)
        # load save
        if key=='l':
            loadingGroup.visible=True
            LoadingInLine.x2=130*app.sizeMulti
            code=app.getTextInput("Enter Save Code")
            loadFile(collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,code)
        if app.mode=='editor':
            if key=='Z':
                undo(collisionArray,editArray,roomGroup,undoneGroup,graphicGroup)
            if key=='Y':
                redo(collisionArray,editArray,roomGroup,undoneGroup,graphicGroup)
        if key=='h':
            if app.hitboxes==False:
                app.hitboxes=True
                if app.mode=='running':
                    roomGroup.visible=True
            else:
                app.hitboxes=False
                if app.mode=='running':
                    roomGroup.visible=False
    if key=='t':
        roomGroup.centerX=app.centerx
        roomGroup.centerY=app.centery
def onMousePress(mouseX,mouseY):
    if app.mousePressed==True:
        app.mousePressed=False
        return
    if ((not colorGroup.hits(mouseX,mouseY)) or colorGroup.opacity==70 or colorGroup.visible==False) and ((not buttonGroupAll.hits(mouseX,mouseY)) or buttonGroupAll.opacity==70 or buttonGroupAll.visible==False) and ((not buttonGroupEditor.hits(mouseX,mouseY)) or buttonGroupEditor.opacity==70 or buttonGroupEditor.visible==False) and ((not buttonGroupRunning.hits(mouseX,mouseY)) or buttonGroupRunning.opacity==70 or buttonGroupRunning.visible==False) and ((not buttonGroupGraphics.hits(mouseX,mouseY)) or buttonGroupGraphics.opacity==70 or buttonGroupGraphics.visible==False) and ((not gridGroup.hits(mouseX,mouseY)) or gridGroup.visible==False) and ((not homeGroup.hits(mouseX,mouseY)) or homeGroup.visible==False):
        if app.creating!=True:
            app.creating=True
        shapeStart(roomGroup,mouseX,mouseY,graphicGroup)
    elif colorGroup.hits(mouseX,mouseY) and colorGroup.visible==True and colorGroup.opacity!=70:
        for i in colorGroup:
            if i.hits(mouseX,mouseY):
                if i!=custom and i!=current:
                    app.graphicsColor=i.fill
                    current.fill=app.graphicsColor
                    app.r=colorRGBDict[i][0]
                    app.g=colorRGBDict[i][1]
                    app.b=colorRGBDict[i][2]
                elif i==custom:
                    app.r=int(app.getTextInput("Insert RGB R-value:"))
                    app.g=int(app.getTextInput("Insert RGB G-value:"))
                    app.b=int(app.getTextInput("Insert RGB B-value:"))
                    if 0<=app.r<=255 and 0<=app.g<=255 and 0<=app.b<=255:
                        app.graphicsColor=rgb(app.r,app.g,app.b)
                        current.fill=app.graphicsColor
                    else:
                        app.graphicsColor=rgb(0,0,0)
                        current.fill=app.graphicsColor
    elif buttonGroupEditor.hits(mouseX,mouseY) and buttonGroupEditor.visible==True and buttonGroupEditor.opacity!=70:
        for i in buttonGroupEditor:
            if i.hits(mouseX,mouseY):
                if i==ch1:
                    app.blockType='1'
                    i.border='gold'
                    cg1.border='steelblue'
                    ca1.border='dimgray'
                    cd1.border='navy'
                    cr1.border='crimson'
                    tb.border='purple'
                    rp.border='gray'
                    lc.border='deeppink'
                elif i==cg1:
                    app.blockType='3'
                    i.border='gold'
                    ca1.border='dimgray'
                    ch1.border='dimgray'
                    cd1.border='navy'
                    cr1.border='crimson'
                    tb.border='purple'
                    rp.border='gray'
                    lc.border='deeppink'
                elif i==ca1:
                    app.blockType='2'
                    i.border='gold'
                    cg1.border='steelblue'
                    ch1.border='dimgray'
                    cd1.border='navy'
                    cr1.border='crimson'
                    tb.border='purple'
                    rp.border='gray'
                    lc.border='deeppink'
                elif i==cd1:
                    app.blockType='0'
                    i.border='gold'
                    cg1.border='steelblue'
                    ch1.border='dimgray'
                    ca1.border='dimgray'
                    cr1.border='crimson'
                    tb.border='purple'
                    rp.border='gray'
                    lc.border='deeppink'
                elif i==cr1:
                    app.blockType='p'
                    i.border='gold'
                    cg1.border='steelblue'
                    ch1.border='dimgray'
                    ca1.border='dimgray'
                    cd1.border='navy'
                    tb.border='purple'
                    rp.border='gray'
                    lc.border='deeppink'
                elif i==lc:
                    app.blockType='l'
                    i.border='gold'
                    cg1.border='steelblue'
                    ch1.border='dimgray'
                    ca1.border='dimgray'
                    cd1.border='navy'
                    cr1.border='crimson'
                    tb.border='purple'
                    rp.border='gray'
                elif i==rp:
                    app.blockType='s'
                    i.border='gold'
                    cg1.border='steelblue'
                    ch1.border='dimgray'
                    ca1.border='dimgray'
                    cd1.border='navy'
                    cr1.border='crimson'
                    tb.border='purple'
                    lc.border='deeppink'
                elif i==tb:
                    app.blockType='t'
                    i.border='gold'
                    cg1.border='steelblue'
                    ch1.border='dimgray'
                    ca1.border='dimgray'
                    cd1.border='navy'
                    cr1.border='crimson'
                    lc.border='deeppink'
                    rp.border='gray'
    elif buttonGroupAll.hits(mouseX,mouseY) and buttonGroupAll.visible==True and buttonGroupAll.opacity!=70:
        for i in buttonGroupAll:
            if i.hits(mouseX,mouseY):
                if i==h1:
                    app.mode='title'
                    app.modeChanged=False
                    colorGroup.visible=False
                    buttonGroupGraphics.visible=False
                    buttonGroupRunning.visible=False
                    buttonGroupEditor.visible=False
                    homeGroup.visible=True
                elif i==e1:
                    app.blockType='1'
                    tempGraphicsButton.border='black'
                    play.border='darkred'
                    e1.border='gold'
                    app.mode='editor'
                    play2.fill='white'
                    play2.border='gray'
                    play3.fill=None
                    play3.border=None
                    play4.fill=None
                    play5.fill=None
                    app.dashing=False
                    roomGroup.visible=True
                    arrayCopy(collisionArray,editArray)
                    roomGroup.centerX=app.centerx
                    roomGroup.centerY=app.centery
                    graphicGroup.centerX=app.centerx
                    graphicGroup.centerY=app.centery
                    character.centerX=app.centerx
                    character.centerY=app.centery
                    app.modeChanged=False
                    colorGroup.visible=False
                    buttonGroupGraphics.visible=False
                    buttonGroupRunning.visible=False
                    buttonGroupEditor.visible=True
                elif i==play:
                    tempGraphicsButton.border='black'
                    play.border='gold'
                    e1.border='black'
                    app.dashing=False
                    play2.fill=None
                    play2.border=None
                    play3.fill='white'
                    play3.border='gray'
                    play4.fill='red'
                    play5.fill='gray'
                    if app.hitboxes==True:
                        roomGroup.visible=True
                    else:
                        roomGroup.visible=False
                    if app.mode!='running':
                        runLevel(collisionArray,editArray,roomGroup,graphicGroup)
                        app.mode='running'
                    else:
                        respawn(collisionArray,editArray,roomGroup,graphicGroup)
                    app.modeChanged=False
                    colorGroup.visible=False
                    buttonGroupGraphics.visible=False
                    buttonGroupRunning.visible=True
                    buttonGroupEditor.visible=False
                    score.value=0
                elif i==tempGraphicsButton:
                    play2.fill='white'
                    play2.border='gray'
                    play3.fill=None
                    play3.border=None
                    play4.fill=None
                    play5.fill=None
                    tempGraphicsButton.border='gold'
                    play.border='darkred'
                    e1.border='black'
                    app.mode='graphics'
                    app.dashing=False
                    app.modeChanged=False
                    roomGroup.visible=True
                    arrayCopy(collisionArray,editArray)
                    roomGroup.centerX=app.centerx
                    roomGroup.centerY=app.centery
                    graphicGroup.centerX=app.centerx
                    graphicGroup.centerY=app.centery
                    character.centerX=app.centerx
                    character.centerY=app.centery
                    colorGroup.visible=True
                    buttonGroupGraphics.visible=True
                    buttonGroupRunning.visible=False
                    buttonGroupEditor.visible=False
                elif i==room1:
                    gridGroup.visible=True
                    for i in buttonList:
                        if i!=gridGroup:
                            i.opacity=70
                    app.creating=False
                elif i==ll:
                    app.darklevel=int(("0"+app.getTextInput("Enter darkness level from 0 to 50:")).split(".")[0].strip())
                    if 0<=app.darklevel<=50:
                        darkGroup.opacity=app.darklevel
                    else:
                        a=app.getTextInput("Invalid #")
    elif gridGroup.hits(mouseX,mouseY) and gridGroup.visible==True:
        for i in gridGroup:
            if i.hits(mouseX,mouseY) and i!=menuBack and i!=gridBorder and i!=selected:
                if i==room00:
                    roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,0,0)
                elif i==room01:
                    roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,0,1)
                elif i==room02:
                    roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,0,2)
                elif i==room10:
                    roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,1,0)
                elif i==room11:
                    roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,1,1)
                elif i==room12:
                    roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,1,2)
                elif i==room20:
                    roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,2,0)
                elif i==room21:
                    roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,2,1)
                elif i==room22:
                    roomSwitchEdit(levelList,collisionArray,editArray,roomGroup,levelBorderA,graphicGroup,shapeBorderA,2,2)
                if i!=exitBox and i!=exit:
                    selected.centerX=i.centerX
                    selected.centerY=i.centerY
                gridGroup.visible=False
                for i in buttonList:
                    i.opacity=100
                app.creating=False
                break
    elif buttonGroupGraphics.hits(mouseX,mouseY) and buttonGroupGraphics.visible==True and buttonGroupGraphics.opacity!=70:
        for i in buttonGroupGraphics:
            if i.hits(mouseX,mouseY):
                if i==tempCircleButton:
                    app.shapeType='Circle'
                    tempCircleButton.border='gold'
                    tempRectButton.border='black'
                    tempLineButton.border='black'
                elif i==tempRectButton:
                    app.shapeType='Rect'
                    tempCircleButton.border='black'
                    tempRectButton.border='gold'
                    tempLineButton.border='black'
                elif i==tempLineButton:
                    app.shapeType='Line'
                    tempCircleButton.border='black'
                    tempRectButton.border='black'
                    tempLineButton.border='gold'
    elif homeGroup.hits(mouseX,mouseY) and homeGroup.visible==True:
        for i in homeGroup:
            if i.hits(mouseX,mouseY):
                if i==a1:
                    pass
                elif i==b1:
                    pass
                elif i==c1:
                    pass
    app.mousePressed=True
def onMouseDrag(mouseX,mouseY):
    if ((not colorGroup.hits(mouseX,mouseY)) or colorGroup.opacity==70 or colorGroup.visible==False) and ((not buttonGroupAll.hits(mouseX,mouseY)) or buttonGroupAll.opacity==70 or buttonGroupAll.visible==False) and ((not buttonGroupEditor.hits(mouseX,mouseY)) or buttonGroupEditor.opacity==70 or buttonGroupEditor.visible==False) and ((not buttonGroupRunning.hits(mouseX,mouseY)) or buttonGroupRunning.opacity==70 or buttonGroupRunning.visible==False) and ((not buttonGroupGraphics.hits(mouseX,mouseY)) or buttonGroupGraphics.opacity==70 or buttonGroupGraphics.visible==False) and ((not gridGroup.hits(mouseX,mouseY)) or gridGroup.visible==False):
        if app.creating==True and app.blockType!='s':
            shapeDrag(roomGroup,mouseX,mouseY,graphicGroup)
            if app.mode!='running':
                for i in buttonList:
                    if i!=gridGroup:
                        i.opacity=70
def onMouseRelease(mouseX,mouseY):
    if ((not colorGroup.hits(mouseX,mouseY)) or colorGroup.opacity==70 or colorGroup.visible==False) and ((not buttonGroupAll.hits(mouseX,mouseY)) or buttonGroupAll.opacity==70 or buttonGroupAll.visible==False) and ((not buttonGroupEditor.hits(mouseX,mouseY)) or buttonGroupEditor.opacity==70 or buttonGroupEditor.visible==False) and ((not buttonGroupRunning.hits(mouseX,mouseY)) or buttonGroupRunning.opacity==70 or buttonGroupRunning.visible==False) and ((not buttonGroupGraphics.hits(mouseX,mouseY)) or buttonGroupGraphics.opacity==70 or buttonGroupGraphics.visible==False) and ((not gridGroup.hits(mouseX,mouseY)) or gridGroup.visible==False):
        if app.creating==True:
            shapeSet(editArray,roomGroup,levelBorderA)
    app.creating=False
    app.mousePressed=False
    for i in buttonList:
        i.opacity=100
    p=0
    for i in portalList:
        if len(i)==0 or len(i)==1:
            if p==0:
                p+=1
            else:
                portalList.remove(i)
    app.portals=len(portalList)-1
    p=0
    for i in portalList:
        if p>app.portals:
            portalList.remove(i)
        p+=1
def onMouseMove(mouseX,mouseY):
    if app.mode=='editor':
        if app.blockType=='p':
            centerX=levelBorderA.left+(rounded(distance(levelBorderA.left,0,mouseX,0)/app.pixelSize)*app.pixelSize)
            centerY=levelBorderA.top+(rounded(distance(0,levelBorderA.top,0,mouseY)/app.pixelSize)*app.pixelSize)
            if mouseX>centerX:
                centerX+=(app.pixelSize/2)
            elif mouseX<centerX:
                centerX-=(app.pixelSize/2)
            if mouseY>centerY:
                centerY+=(app.pixelSize/2)
            elif mouseY<centerY:
                centerY-=(app.pixelSize/2)
            portalSign.visible=True
            portalSign.centerX=centerX
            portalSign.centerY=centerY
        else:
            portalSign.visible=False
    elif app.mode=='title':
        portalSign.visible=False
        if mouseX>130*app.sizeMulti and mouseX<270*app.sizeMulti:
            if mouseY>310*app.sizeMulti and mouseY<330*app.sizeMulti:
                b.fill=None
                b1.fill=gradient('white','azure','aliceBlue',start='left')
                c.fill=gradient('white','azure','aliceBlue',start='left')
                c1.fill=None
                a.fill=gradient('white','azure','aliceBlue',start='left')
                a1.fill=None
            if mouseY>350*app.sizeMulti and mouseY<370*app.sizeMulti:
                c.fill=None
                c1.fill=gradient('white','azure','aliceBlue',start='left')
                b.fill=gradient('white','azure','aliceBlue',start='left')
                b1.fill=None
                a.fill=gradient('white','azure','aliceBlue',start='left')
                a1.fill=None
            if mouseY>270*app.sizeMulti and mouseY<290*app.sizeMulti:
                c.fill=gradient('white','azure','aliceBlue',start='left')
                c1.fill=None
                b.fill=gradient('white','azure','aliceBlue',start='left')
                b1.fill=None
                a.fill=None
                a1.fill=gradient('white','azure','aliceBlue',start='left')
        else:
            c.fill=gradient('white','azure','aliceBlue',start='left')
            c1.fill=None
            b.fill=gradient('white','azure','aliceBlue',start='left')
            b1.fill=None
            a.fill=gradient('white','azure','aliceBlue',start='left')
            a1.fill=None
cmu_graphics.run()