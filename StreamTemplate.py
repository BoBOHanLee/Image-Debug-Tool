'''
Hank Lee maintain in 2021/11/17
Using QT tool
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QImage, QPixmap
from UItemplate import *
import telnetlib
import threading
import time
import paramiko
import cv2
import numpy as np


# Command Line for SSH and Telnet
commend = '/usr/sbin/venc'              # Run venc
commend2 = '/etc/init.d/venc stop'      # Stop venc
commend3 = 'imgsys_test -l 10000000'    # Open DNS tuning log
commend4 = '/etc/init.d/rtsps restart'
UICLOSE_FLAG = False


# FUNCTION
def command(con, flag, str_=""):
    data = con.read_until(flag.encode())
    print(data.decode(errors='ignore'))
    con.write(str_.encode() + b"\n")
    return data

# CLASS
class StreamObj:
    def __init__(self, url, label):
        self.url = url
        self.label = label
        self.img = None

    def Get_CVImage(self):
        return self.img

    def Obj_showing(self):
        Width_mutiple = 1.0
        Height_mutiple = 1.0
        Multiple = 1.0
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Waiting...")
        time.sleep(15.0)  #To avoid get NULL camera obj

        cap =cv2.VideoCapture(self.url)
        while cap.isOpened():
            frame = cap.read()[1]
            self.img = frame

            '''  ---Reshape Image to show full FOV---   '''
            shape = frame.shape
            Width_mutiple = float(shape[1] / self.label.width())
            Height_mutiple = float(shape[0] / self.label.height())

            if(Width_mutiple > Height_mutiple): Multiple = Width_mutiple
            else: Multiple = Height_mutiple

            Multiple = int(1.2 * Multiple)  #Size protection
            NewShape = (int(shape[1] / Multiple), int(shape[0] / Multiple))
            frame = cv2.resize(frame, NewShape, interpolation=cv2.INTER_CUBIC)

            ''' ---HMI Showing--- '''
            if UICLOSE_FLAG:
                cap.release()
                break
            else:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.label.setPixmap(QPixmap.fromImage(img))
                cv2.waitKey(1)

# Main HMI
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connectButton.clicked.connect(self.HMI_THREAD_CONNECT)
        self.Button_photo.clicked.connect(self.HMI_FUNCTION_PHOTO)
        self.lineEdit_commend.editingFinished.connect(self.HMI_COMMEND_EVENT)
        self.CloseFlag = False
        self.CommendFlag = False
        self.LogInfo = ""
        self.HMIurl = ""
        self.StreamObj = None
        self.label_Ravg.setStyleSheet("color:red")
        self.label_Gavg.setStyleSheet("color:green")
        self.label_Bavg.setStyleSheet("color:blue")

    def HMI_FUNCTION_PHOTO(self):
        img = self.StreamObj.Get_CVImage()
        cv2.imwrite("test.jpg", img)
        print("Take photo")

    def HMI_IMGSHOWING(self):
        # User can calculate any image features with this function
        time.sleep(30.0)
        while True:
            time.sleep(1.0) #limitation
            img = self.StreamObj.Get_CVImage()
            if img.any() != 0:
                # Average brightness
                img_R = img[:, :, 0]
                img_G = img[:, :, 1]
                img_B = img[:, :, 2]
                img_Y = 0.299 * img_R + 0.587 * img_G + 0.114 * img_B

                Ravg = np.mean(img_R)
                Gavg = np.mean(img_G)
                Bavg = np.mean(img_B)
                Yavg = np.mean(img_Y)

                sd_R = np.std(img_R)
                sd_G = np.std(img_G)
                sd_B = np.std(img_B)
                sd_Y = np.std(img_Y)

                snr_R = np.where(sd_R == 0, 0, Ravg / sd_R)
                snr_G = np.where(sd_G == 0, 0, Gavg / sd_G)
                snr_B = np.where(sd_B == 0, 0, Bavg / sd_B)
                snr_Y = np.where(sd_Y == 0, 0, Yavg / sd_Y)

                self.label_Ravg.setText(str(round(Ravg)))
                self.label_Gavg.setText(str(round(Gavg)))
                self.label_Bavg.setText(str(round(Bavg)))
                self.label_Yavg.setText(str(round(Yavg)))

                self.label_snrR.setText(str(np.around(snr_R, decimals= 3)))
                self.label_snrG.setText(str(np.around(snr_G, decimals= 3)))
                self.label_snrB.setText(str(np.around(snr_B, decimals= 3)))
                self.label_snrY.setText(str(np.around(snr_Y, decimals= 3)))

            if self.CloseFlag == True:
                break

    def HMI_COMMEND_EVENT(self):
        if(self.lineEdit_commend.hasFocus()): #To avoid error trigger
            self.CommendFlag = True
        else :
            self.CommendFlag = False

    def HMI_THREAD_CONNECT(self):
        self.ShowBlowser_flag = 1

        # ------------ 1. Thread for log and commend -------------
        if self.radioButton_ssh.isChecked() == True:
            threading.Thread(target=self.HMI_GET_SSHLOGINFO, args=()).start()
            threading.Thread(target=self.HMI_SET_SSHCOMMEND, args=()).start()
            print("SSH connecting")
        else:
            threading.Thread(target=self.HMI_GET_TELLOGINFO, args=()).start()
            threading.Thread(target=self.HMI_SET_TELCOMMEND, args=()).start()
            print("Telnet connecting")

        # ------------ 2. Thread for streaming ------------
        '''
        ex. rtsp://root:IOD000000@10.66.104.145/live1s1.sdp
        '''
        ip = self.ipEdit.toPlainText()
        username = self.ipEdit_username.toPlainText()
        password = self.ipEdit_password.toPlainText()
        self.HMIurl = "rtsp://" + username + ":" + password + "@" + ip + "/live1s1.sdp"
        StreamObj_con = StreamObj(self.HMIurl,self.CurImage)
        self.StreamObj = StreamObj_con
        threading.Thread(target = self.StreamObj.Obj_showing, args=()).start()

        # ------------ 3. Thread for img showing ------------
        threading.Thread(target = self.HMI_IMGSHOWING, args=()).start()

    def HMI_SET_SSHCOMMEND(self):
        # ------------ Wait for ssh connection -------------
        time.sleep(6.0)
        # ------------ Detect commend and enter event -------------
        while True:
            textC = self.lineEdit_commend.text()   #check ok
            if(self.CommendFlag == True):
                Commend = textC
                print("Enter : " + Commend)
                stdin_com, stdout_comp, stderr_com = self.client.exec_command(Commend, get_pty=True)
                self.CommendFlag = False

    def HMI_SET_TELCOMMEND(self):
        # ------------ Wait for ssh connection -------------
        time.sleep(6.0)
        # ------------ Detect commend and enter event -------------
        while True:
            textC = self.lineEdit_commend.text()   #check ok
            if(self.CommendFlag == True):
                Commend = textC
                print("Enter : " + Commend)
                command(self.tn, "", Commend)
                self.CommendFlag = False

    def HMI_GET_SSHLOGINFO(self):
        # ------------ Build a ssh Object -------------
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.ipEdit.toPlainText(), port=22, username=self.ipEdit_username.toPlainText(), password=self.ipEdit_password.toPlainText())  # Connecting

        # ------------ Commend Process ------------
        stdin_stop, stdout_stop, stderr_stop = self.client.exec_command(commend2, get_pty=True)
        print("Stop venc  " + commend2)
        time.sleep(6.0)
        stdin, stdout, stderr = self.client.exec_command(commend, get_pty=True)
        print("Start venc  " + commend)
        time.sleep(6.0)
        stdin2, stdout2, stderr2 = self.client.exec_command(commend4, get_pty=True)
        print("Return rtsp  " + commend4)
        time.sleep(2.0)

        for line in iter(stdout.readline, ""):
            # ------------ Log filter process ------------
            # User can design any logic with this function
            self.LogInfo = line
            LogContent = self.LogFileter_Edit.toPlainText()
            LogContent = LogContent.split('&&')
            for LogInfo in LogContent:
                if LogInfo in self.LogInfo:
                    print(self.LogInfo)


            # Disconnect HMI
            if (self.CloseFlag == True):
                print("Stop venc and close the window")
                stdin, stdout, stderr = self.client.exec_command(commend2, get_pty=True)
                time.sleep(6.0)
                QApplication.closeAllWindows()
                break

    def HMI_GET_TELLOGINFO(self):
        # ------------ Build a ssh Object -------------
        # Front view
        self.tn = telnetlib.Telnet(self.ipEdit.toPlainText(), port=23)
        command(self.tn, "", self.ipEdit_username.toPlainText())
        command(self.tn, "", self.ipEdit_password.toPlainText())
        # For other commend
        self.tn2 = telnetlib.Telnet(self.ipEdit.toPlainText(), port=23)
        command(self.tn2, "", self.ipEdit_username.toPlainText())
        command(self.tn2, "", self.ipEdit_password.toPlainText())

        # ------------ Commend Process ------------
        command(self.tn, "", commend2)
        print("Stop venc  " + commend2)
        time.sleep(6.0)
        command(self.tn, "", commend)
        print("Start venc  " + commend)
        time.sleep(6.0)


        while True:
            # ------------ Log filter process ------------
            # User can design any logic with this function
            data = self.tn.read_until("\n".encode())
            self.LogInfo = data
            LogContent = self.LogFileter_Edit.toPlainText()
            LogContent = LogContent.split('&&')
            for LogInfo in LogContent:
                if LogInfo in self.LogInfo:
                    print(self.LogInfo)

            # dis connect the machine
            if (self.CloseFlag == 1):
                command(self.tn2, "", commend2)
                print("Stop venc  " + commend2)
                self.tn.close()
                time.sleep(6.0)
                QApplication.closeAllWindows()
                break

    def closeEvent(self, event):   #closeEvent - close HMI event
        self.CloseFlag = True
        UICLOSE_FLAG = True

        if (self.CloseFlag): # Wait for this thread close
            threading.Thread(target = self.StreamObj.Obj_showing, args=()).join()
            threading.Thread(target=self.HMI_IMGSHOWING, args=()).join()

            if self.radioButton_ssh.isChecked() == True:
                threading.Thread(target=self.HMI_SET_SSHCOMMEND, args=()).join()
                threading.Thread(target = self.HMI_GET_SSHLOGINFO, args=()).join()
            else:
                threading.Thread(target=self.HMI_SET_TELCOMMEND, args=()).join()
                threading.Thread(target = self.HMI_GET_TELLOGINFO, args=()).join()
            QApplication.closeAllWindows()

if __name__ == "__main__":

    #Create HMI
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())









