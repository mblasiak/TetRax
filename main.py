from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

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
        self.pud=self.pudlo()
        self.pud.setPozVar(3,3,3)
        self.pud.setPoz()
        self.L=self.Lway()





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


    class Lway():
        def __init__(self):
            self.x=0
            self.y=0
            self.z=0

            self.p0=MyApp.pudlo()
            self.p0.setPozVar(self.x,self.y,self.z)
            self.p0.setPoz()

            self.p1=MyApp.pudlo()
            self. p1.setPozVar(self.x,self.y+2,self.z)
            self. p1.setPoz()
            self. p2=MyApp.pudlo()
            self. p2.setPozVar(self.x+2,self.y+2,self.z)
            self. p2.setPoz()

            self.p3=MyApp.pudlo()
            self.p3.setPozVar(self.x+4,self.y+2,self.z)
            self.p3.setPoz()
        def updatePoz(self):
            self.p0.setPozVar(self.x,self.y,self.z)
            self.p0.setPoz()
            self. p1.setPozVar(self.x,self.y+2,self.z)
            self. p1.setPoz()
            self. p2.setPozVar(self.x+2,self.y+2,self.z)
            self. p2.setPoz()
            self.p3.setPozVar(self.x+4,self.y+2,self.z)
            self.p3.setPoz()
        def changePozVar(self,X,Y,Z):
            self.x=X
            self.y=Y
            self.z=Z



app = MyApp()
app.run()