from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
#from direct.task.Task import Task
from direct.actor.Actor import Actor


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
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
        self.L=self.Lway()
        self.L.changePozVar(0,100,5)
        self.L.updatePoz()
        #taskMgr.doMethodLater(1, 'DP')
        #self.task=Task(self.fall(self.L))
        self.taskMgr.add(self.fall, 'MyTaskName', extraArgs=[self.L])
        #self.taskMgr.add(self.task, "Fall")
        #self.fall(self.L)


    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    class pudlo():
        def __init__(self):
            self.pudlo=loader.loadModel("PS.egg")
            self.pudlo.reparentTo(render)
            self.x = 1
            self.y = 1
            self.z = 1

        def setPozVar(self,X,Y,Z):
            self.x=X
            self.y=Y
            self.z=Z
        def setPoz(self):
            self.pudlo.setPos(self.x,self.y,self.z)

   # class PlayBox():
    #    def __init__(self):



    class Lway():
        def __init__(self):
            self.x=0
            self.y=0
            self.z=0

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
        def updatePoz(self):
            self.p0.setPozVar(self.x,self.y,self.z)
            self.p0.setPoz()
            self. p1.setPozVar(self.x,self.y,self.z+2)
            self. p1.setPoz()
            self. p2.setPozVar(self.x+2,self.y,self.z+2)
            self. p2.setPoz()
            self.p3.setPozVar(self.x+4,self.y,self.z+2)
            self.p3.setPoz()
        def changePozVar(self,X,Y,Z):
            self.x=X
            self.y=Y
            self.z=Z
        def IncPoz(self,X,Y,Z):
            self.x=self.x+X
            self.y=self.y+Y
            self.z=self.z+Z
    def fall(self,obj):
        obj.IncPoz(0,0,-0.01)
        obj.updatePoz()
        print("1")
        return Task.cont


app = MyApp()
app.run()