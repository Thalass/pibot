import socket
import sys
from PySide import QtGui, QtCore


HOST, PORT = "pibotomg.local", 9999


#GUI
class Interface(QtGui.QMainWindow):
    
    def __init__(self):
        super(Interface, self).__init__()

        self.initUI()
        print "UI initialised. Connecting..."
        networkstuff.connect()
        print "Connected?"

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Pibot Controller')
        self.show()

    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_Escape:
            sock.close()
            self.close()

        elif e.key() == QtCore.Qt.Key_W:
            senddata(w)
            print recvdata()


class networkstuff(socket):

    def connect(HOST, PORT):
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT)
        sock.sendall("testing\n")
#        return "connected to %s" % HOST

    def senddata(key):

        sock.sendall(key + "\n")
        
    def recvdata():

        received = sock.recv(1024)


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
