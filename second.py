from PyQt4 import QtCore, QtGui
import cv2 as cv
import numpy as np

inWidth = 300
inHeight = 300
WHRatio = inWidth / float(inHeight)
inScaleFactor = 0.007843
meanVal = 127.5
count=0
i=0



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(450, 200)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 120, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):

  
    num_classes=2
    prototxt="MobileNetSSD_deploy.prototxt"
    weights="MobileNetSSD_deploy.caffemodel"
    thr=0.0001

    if num_classes == 2:
        net = cv.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt","MobileNetSSD_deploy.caffemodel")
        swapRB = False
        classNames = { 0: 'background',
            1: 'solar'}

   
    cap = cv.VideoCapture('they.mp4')
   

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        blob = cv.dnn.blobFromImage(frame, inScaleFactor, (inWidth, inHeight), (meanVal, meanVal, meanVal), swapRB)
        net.setInput(blob)
        detections = net.forward()
       
        count=0
        
        cols = frame.shape[1]
        rows = frame.shape[0]

        if cols / float(rows) > WHRatio:
            cropSize = (int(rows * WHRatio), rows)
        else:
            cropSize = (cols, int(cols / WHRatio))

        y1 = int((rows - cropSize[1]) / 2)
        y2 = y1 + cropSize[1]
        x1 = int((cols - cropSize[0]) / 2)
        x2 = x1 + cropSize[0]
        frame = frame[y1:y2, x1:x2]

        cols = frame.shape[1]
        rows = frame.shape[0]

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > thr:
                
                class_id = int(detections[0, 0, i, 1])

                xLeftBottom = int(detections[0, 0, i, 3] * cols)
                yLeftBottom = int(detections[0, 0, i, 4] * rows)
                xRightTop   = int(detections[0, 0, i, 5] * cols)
                yRightTop   = int(detections[0, 0, i, 6] * rows)

                cv.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                              (0, 255, 0))

                if class_id in classNames:
                    count=count+1
                    label = classNames[class_id] + ": " + str(confidence)
                    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)

                    yLeftBottom = max(yLeftBottom, labelSize[1])
                   
                    
                    cv.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]),
                                         (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
                                         (255, 255, 255), cv.FILLED)
                    cv.putText(frame, label, (xLeftBottom, yLeftBottom),
                                cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
      
        fram = cv.resize(frame, (800,600)) 
        cv.imshow("detections", fram)
        if cv.waitKey(1) >= 0:
          break
    cv.destroyAllWindows()
    cap.release()
    self.label.setText(_translate("MainWindow","21", None))
  def setupUii(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(450, 200)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUii(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


  def retranslateUi(self, MainWindow):

  
    num_classes=2
    prototxt="MobileNetSSD_deploy.prototxt"
    weights="MobileNetSSD_deploy.caffemodel"
    thr=0.0001

    if num_classes == 2:
        net = cv.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt","MobileNetSSD_deploy.caffemodel")
        swapRB = False
        classNames = { 0: 'background',
            1: 'solar'}

   
    cap = cv.VideoCapture('they.mp4')
   

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        blob = cv.dnn.blobFromImage(frame, inScaleFactor, (inWidth, inHeight), (meanVal, meanVal, meanVal), swapRB)
        net.setInput(blob)
        detections = net.forward()
       
        count=0
        
        cols = frame.shape[1]
        rows = frame.shape[0]

        if cols / float(rows) > WHRatio:
            cropSize = (int(rows * WHRatio), rows)
        else:
            cropSize = (cols, int(cols / WHRatio))

        y1 = int((rows - cropSize[1]) / 2)
        y2 = y1 + cropSize[1]
        x1 = int((cols - cropSize[0]) / 2)
        x2 = x1 + cropSize[0]
        frame = frame[y1:y2, x1:x2]

        cols = frame.shape[1]
        rows = frame.shape[0]

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > thr:
                
                class_id = int(detections[0, 0, i, 1])

                xLeftBottom = int(detections[0, 0, i, 3] * cols)
                yLeftBottom = int(detections[0, 0, i, 4] * rows)
                xRightTop   = int(detections[0, 0, i, 5] * cols)
                yRightTop   = int(detections[0, 0, i, 6] * rows)

                cv.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                              (0, 255, 0))

                if class_id in classNames:
                    count=count+1
                    label = classNames[class_id] + ": " + str(confidence)
                    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)

                    yLeftBottom = max(yLeftBottom, labelSize[1])
                   
                    
                    cv.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]),
                                         (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
                                         (255, 255, 255), cv.FILLED)
                    cv.putText(frame, label, (xLeftBottom, yLeftBottom),
                                cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
      
        fram = cv.resize(frame, (800,600)) 
        cv.imshow("detections", fram)
        if cv.waitKey(1) >= 0:
          break
    cv.destroyAllWindows()
    cap.release()
    self.label.setText(_translate("MainWindow",str(count), None))
  def retranslateUii(self, MainWindow):
    num_classes=2
    prototxt="MobileNetSSD_deploy2.prototxt"
    weights="MobileNetSSD_deploy2.caffemodel"
    thr=0.0001

    if num_classes == 2:
        net = cv.dnn.readNetFromCaffe("MobileNetSSD_deploy2.prototxt","MobileNetSSD_deploy2.caffemodel")
        swapRB = False
        classNames = { 0: 'background',
            1: 'anomaly'}

   
    cap = cv.VideoCapture('demo2.mp4')
   

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        blob = cv.dnn.blobFromImage(frame, inScaleFactor, (inWidth, inHeight), (meanVal, meanVal, meanVal), swapRB)
        net.setInput(blob)
        detections = net.forward()
       
        count=0
        
        cols = frame.shape[1]
        rows = frame.shape[0]

        if cols / float(rows) > WHRatio:
            cropSize = (int(rows * WHRatio), rows)
        else:
            cropSize = (cols, int(cols / WHRatio))

        y1 = int((rows - cropSize[1]) / 2)
        y2 = y1 + cropSize[1]
        x1 = int((cols - cropSize[0]) / 2)
        x2 = x1 + cropSize[0]
        frame = frame[y1:y2, x1:x2]

        cols = frame.shape[1]
        rows = frame.shape[0]

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > thr:
                
                class_id = int(detections[0, 0, i, 1])

                xLeftBottom = int(detections[0, 0, i, 3] * cols)
                yLeftBottom = int(detections[0, 0, i, 4] * rows)
                xRightTop   = int(detections[0, 0, i, 5] * cols)
                yRightTop   = int(detections[0, 0, i, 6] * rows)

                cv.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                              (0, 255, 0))

                if class_id in classNames:
                    count=count+1
                    label = classNames[class_id] + ": " + str(confidence)
                    labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)

                    yLeftBottom = max(yLeftBottom, labelSize[1])
                   
                    
                    cv.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]),
                                         (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
                                         (255, 255, 255), cv.FILLED)
                    cv.putText(frame, label, (xLeftBottom, yLeftBottom),
                                cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
      
        fram = cv.resize(frame, (800,600)) 
        cv.imshow("detections", fram)
        if cv.waitKey(1) >= 0:
          break
    cv.destroyAllWindows()
    cap.release()
    self.label.setText(_translate("MainWindow",str(count), None))









