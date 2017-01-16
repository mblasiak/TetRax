from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
#from direct.task.Task import Task
from direct.actor.Actor import Actor


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.camera.setPos(0,0,0)
       # self.lens.setFov(100)
        '''
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")
        '''

        self.wall=self.loader.loadModel("graund.egg")
        self.wall.reparentTo(self.render)
        self.wall.setPos(0,100,-20)
        self.L=self.Lway(4)
        self.x=self.L
        self.L.changePozVar(1,100,-21)
        self.z=self.fillUp()

        self.info=self.objInfo(0,0,0,1,1)
        self.taskMgr.add(self.printlogs,'print Log',extraArgs=[self.info,self.L])
        self.taskMgr.add(self.fall, 'fall', extraArgs=[self.L])
        self.taskMgr.add(self.ster,'steer', extraArgs=[self.L])
      #  self.taskMgr.add(self.printPos,'posPrint', extraArgs=[self.L])


    class pudlo():
        def __init__(self):
            self.pudlo=loader.loadModel("PS.egg")
            self.pudlo.reparentTo(render)
            self.x = 1
            self.y = 1
            self.z = 1
            self.showStatus=1
        def notShow(self):
           # self.pudlo.detachNode()
            self.pudlo.hide()
            self.showStatus=0
        def Show(self):
            self.pudlo.show()
            self.showStatus=1
        def setPozVar(self,X,Y,Z):
            self.x=X
            self.y=Y
            self.z=Z
        def setPoz(self):
            self.pudlo.setPos(self.x,self.y,self.z)



    def ster(self,ob):
        self.accept("a",ob.moveL)
        self.accept("d",ob.moveR)
        self.accept("w", ob.moveUp)
        self.accept("s", ob.moveDown)

    class Lway():
        def __init__(self,stat):
            self.x=0
            self.y=0
            self.z=0
            self.state=stat
            if(self.state==1):
                self.p0=MyApp.pudlo()
                self.p0.setPozVar(self.x,self.y,self.z)
                self.p0.setPoz()

                self.p1=MyApp.pudlo()
                self. p1.setPozVar(self.x,self.y,self.z+2)
                self. p1.setPoz()
                self. p2=MyApp.pudlo()
                self. p2.setPozVar(self.x+2,self.y,self.z+2)
                self. p2.setPoz()

                self.p3=MyApp.pudlo()
                self.p3.setPozVar(self.x+4,self.y,self.z+2)
                self.p3.setPoz()
            if(self.state==2):
                self.p0 = MyApp.pudlo()
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()

                self.p1 = MyApp.pudlo()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2 = MyApp.pudlo()
                self.p2.setPozVar(self.x, self.y, self.z + 4)
                self.p2.setPoz()

                self.p3 = MyApp.pudlo()
                self.p3.setPozVar(self.x+2, self.y, self.z)
                self.p3.setPoz()
            if(self.state==3):
                self.p0 = MyApp.pudlo()
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()

                self.p1 = MyApp.pudlo()
                self.p1.setPozVar(self.x+2, self.y, self.z )
                self.p1.setPoz()
                self.p2 = MyApp.pudlo()
                self.p2.setPozVar(self.x + 4, self.y, self.z)
                self.p2.setPoz()

                self.p3 = MyApp.pudlo()
                self.p3.setPozVar(self.x + 4, self.y, self.z + 2)
                self.p3.setPoz()
            if(self.state==4):
                self.p0 = MyApp.pudlo()
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()

                self.p1 = MyApp.pudlo()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2 = MyApp.pudlo()
                self.p2.setPozVar(self.x , self.y, self.z + 4)
                self.p2.setPoz()

                self.p3 = MyApp.pudlo()
                self.p3.setPozVar(self.x -2, self.y, self.z + 4)
                self.p3.setPoz()

        def updatePoz(self):
            if(self.state==1):
                self.p0.setPozVar(self.x,self.y,self.z)
                self.p0.setPoz()
                self. p1.setPozVar(self.x,self.y,self.z+2)
                self. p1.setPoz()
                self. p2.setPozVar(self.x+2,self.y,self.z+2)
                self. p2.setPoz()
                self.p3.setPozVar(self.x+4,self.y,self.z+2)
                self.p3.setPoz()

            if(self.state==2):
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2.setPozVar(self.x, self.y, self.z + 4)
                self.p2.setPoz()
                self.p3.setPozVar(self.x + 2, self.y, self.z)
                self.p3.setPoz()
            if(self.state==3):
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()
                self.p1.setPozVar(self.x+2, self.y, self.z )
                self.p1.setPoz()
                self.p2.setPozVar(self.x + 4, self.y, self.z)
                self.p2.setPoz()
                self.p3.setPozVar(self.x + 4, self.y, self.z + 2)
                self.p3.setPoz()


            if(self.state==4):
                self.p0.setPozVar(self.x, self.y, self.z)
                self.p0.setPoz()
                self.p1.setPozVar(self.x, self.y, self.z + 2)
                self.p1.setPoz()
                self.p2.setPozVar(self.x , self.y, self.z + 4)
                self.p2.setPoz()
                self.p3.setPozVar(self.x -2, self.y, self.z + 4)
                self.p3.setPoz()

        def changePozVar(self,X,Y,Z):
            self.x=X
            self.y=Y
            self.z=Z
        def IncPoz(self,X,Y,Z):
            self.x=self.x+X
            self.y=self.y+Y
            self.z=self.z+Z
        def moveL(self):
            self.IncPoz(-2,0,0)
            self.updatePoz()
        def moveR(self):
            self.IncPoz(2,0,0)
            self.updatePoz()
        def moveUp(self):
            self.IncPoz(0,0,2)
            self.updatePoz()
        def moveDown(self):
            self.IncPoz(0,0,-2)
            self.updatePoz()

    class objInfo():
        def __init__(self,X,Y,Z,typ,typRot):
            self.logX=X
            self.logY=Y
            self.logZ=Z
            self.type=typ
            self.typeRot=typRot
        def setLogs(self,x,y,z):
            self.logX=(x+9)//2
            self.logZ=(z-21)//2

    def printlogs(self,obj,obj2):
        obj.setLogs(obj2.x,obj2.y,obj2.z)
        print(obj.logX)
        print(obj.logY)
        print(obj.logZ)
        print("-----------------------")
        return Task.cont

    def fall(self,obj):
        obj.IncPoz(0,0,-0.01)
        obj.updatePoz()
        return Task.cont
    def printPos(self,obj):
        print(obj.x)
        print(obj.y)
        print(obj.z)
        print ("/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
        return Task.cont

    class fillUp(pudlo):
        class cell():
            def __init__(self):
                self.boxHold=MyApp.pudlo()
                exsist=0
        def __init__(self):
            self.boxTab=[]

            for i in range(20):
                self.littleTab = []
                for j in range(10):
                    self.pom=self.cell()
                    self.pom.boxHold.setPozVar(9-2*j,100,2*i-21)
                    self.pom.boxHold.setPoz()
                    self.pom.boxHold.notShow()
                    self.littleTab.append(self.pom)


                    #self.boxTab[i][j].append(self.pom)

                    #self.boxTab[i][j].boxHold.notShow
                    #self.pom=MyApp.pudlo()
                    #self.pom.setPozVar(9-2*j,100,2*i-21)
                    #self.pom.setPoz()
                    #self.boxTab.append(self.pom)
                self.boxTab.append(self.littleTab)
        def showBox(self):
            for i in range(20):
                for j in range(10):
                    if(self.boxTab[i][j].boxHold.showStatus==0 and  self.boxTab[i][j].exist==1):
                        self.boxTab[i][j].boxHold.Show()
                    if(self.boxTab[i][j].boxHold.showStatus == 1 and self.boxTab[i][j].exist==0):
                        self.boxTab[i][j].boxHold.notShow()
app = MyApp()
app.run()