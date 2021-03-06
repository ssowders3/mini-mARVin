import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt
from pynput import keyboard

class App(QWidget):
    def __init__(self, OtherWindow):
    #def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        print("ths one is on github!!")
        self.setGeometry(100,100,400,720)
        # 715 x 385 => 720x  390
        #Assuming the world is 147m(height) by 77m(height)

        self.pixbycm_height = 630/147
        self.pixbycm_width = 320/77


        self.setWindowTitle("New GUI Interface Window")
        self.currentAngle = 0

        self.obstCounter = 0
        self.x = 10
        self.y = 650
        self.d = []

        self.image= QtGui.QImage('smallcar.png')
        self.rectImage = QtGui.QImage('rectOutline.png')

        self.pixmap = QtGui.QPixmap(self.image)
        self.pixmap_rect = QtGui.QPixmap(self.rectImage)

        self.tank = QtWidgets.QLabel(self)
        self.tank.setAlignment(QtCore.Qt.AlignCenter)
        self.tank.setPixmap(self.pixmap)
        self.tank.adjustSize()
        self.tank.move(self.x, self.y)

        self.boarder = QtWidgets.QLabel(self)
        self.boarder.setAlignment(QtCore.Qt.AlignCenter)
        self.boarder.setPixmap(self.pixmap_rect)
        self.boarder.adjustSize()
        self.createObstacle()
        #self.showObstacle([0,10])

        self.show()




    def moveCar(self, curPos):
        new_x = curPos[0]
        new_y = curPos[1]
        self.x = new_x * self.pixbycm_width + 10
        self.y = 650 - (new_y * self.pixbycm_height)

        if self.x > 330:
            self.x = 330
        if self.y > 650:
            self.y = 650
        if self.x < 10:
            self.x = 10
        if self.y <20:
            self.y = 20
        #self.x += new_x
        #self.y += new_y
        self.tank.move(self.x, self.y)
        print(self.showTankPos())

        #for testing show obstacle method /// comment it out later
        """
        if self.showTankPos() == [20, 590]:
            print("show Obstacle is called")
            self.showObstacle([20,round(-15 * self.pixbycm_height,2) + 590])
        elif self.showTankPos() == [60, 590]:
            print("show obstacle is called again")
            self.showObstacle([90,590])
        """

    def showTankPos(self):
        return [self.x, self.y]



    def createObstacle(self):

        self.obstImage = QtGui.QImage('obsta_edited.png')
        self.pixmap_obst = QtGui.QPixmap(self.obstImage)

        for i in range(0,80):
            self.d.append(["O{0}".format(i), []])
            label = QtWidgets.QLabel(self)
            label.setPixmap(self.pixmap_obst)
            label.move(9999, 9999)
            label.adjustSize()
            self.d[i][0] = label



        #print(self.d)


    def showObstacle(self,ObstPos, CurrPos):
        print("test if there is already another obstacle")

        [tankx, tanky] = self.showTankPos()
        carPosx = int(CurrPos[0])
        carPosy = int(CurrPos[1])

        ObstPos_x = int(ObstPos[0])
        ObstPos_y = int(ObstPos[1])
        print("car position x: " + str(ObstPos[0]))
        print("car position y: " + str(ObstPos[1]))

        if ObstPos_x <= 10 and ObstPos_y <= 10:

            x = (self.pixbycm_width* ObstPos_x) + 10 + tankx
            print('x obstacle: ' + str(x))
            y = (self.pixbycm_height* ObstPos_y*-1) + tanky
            print('y obstacle; ' + str(y))

            # if ObstPos_x <= 10:
            #     return
            # elif ObstPos_x >= 330:
            #     return
            # elif ObstPos_y <= 20:
            #     return
            # elif ObstPos_y >= 650:
            #     return

            #print([x,y])
            #print(self.d[self.obstCounter][1])
            # if self.obstCounter != 0:
            #     for i in range(0,self.obstCounter):
            #         if [x,y] == self.d[i][1]:
            #             print("The Obstacle is already there")
            #             return
            #

            #print("The Obstacle is not there")
            try:
                self.d[self.obstCounter][0].move(x, y)
                self.d[self.obstCounter][1].append(x)
                self.d[self.obstCounter][1].append(y)
                #print(self.d)
                #print(self.d[self.obstCounter])
                self.d[self.obstCounter][0].show()
                #print(self.obstCounter)
                self.obstCounter += 1
            except:
                print("I caught an error")


    def rotate(self, angle):
        if self.currentAngle == angle:
            print("current angle and received angle are same")
            return
        else:
            if (abs(angle) == 180):
                angle = 180;
            elif(angle < -45 and angle >= -135):
                angle = 90
            elif(angle < -135 or angle >= 130):
                angle = 180
            elif(angle <45 and angle >= -45):
                #dont rotate
                return
            elif(angle> 45 and angle <= 135):
                angle = 270

        self.currentAngle = angle


        transform = QtGui.QTransform().rotate(angle)
        self.pixmap = self.pixmap.transformed(transform)
        self.tank.setPixmap(self.pixmap)


    def printStatement(self, message):
        print("this is from print Statement in GUI")
        print(message)

"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())

"""