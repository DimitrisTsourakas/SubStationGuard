# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1156, 762)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(179, 179, 179, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(217, 217, 217, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(89, 89, 89, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(119, 119, 119, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(240, 240, 240, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        brush9 = QBrush(QColor(227, 227, 227, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush9)
        brush10 = QBrush(QColor(160, 160, 160, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush11 = QBrush(QColor(105, 105, 105, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush11)
        brush12 = QBrush(QColor(245, 245, 245, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 128))
        brush13.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setMouseTracking(False)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 1121, 631))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayoutWidget_7 = QWidget(self.groupBox_7)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(20, 20, 351, 268))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_22 = QFormLayout()
        self.formLayout_22.setObjectName(u"formLayout_22")
        self.formLayout_22.setVerticalSpacing(0)
        self.label_40 = QLabel(self.verticalLayoutWidget_7)
        self.label_40.setObjectName(u"label_40")

        self.formLayout_22.setWidget(0, QFormLayout.LabelRole, self.label_40)

        self.comboBox_6 = QComboBox(self.verticalLayoutWidget_7)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.formLayout_22.setWidget(1, QFormLayout.LabelRole, self.comboBox_6)

        self.toolButton_43 = QToolButton(self.verticalLayoutWidget_7)
        self.toolButton_43.setObjectName(u"toolButton_43")
        self.toolButton_43.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"../images/info-tooltip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_43.setIcon(icon)
        self.toolButton_43.setIconSize(QSize(40, 40))
        self.toolButton_43.setCheckable(False)
        self.toolButton_43.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_43.setAutoRaise(False)
        self.toolButton_43.setArrowType(Qt.NoArrow)

        self.formLayout_22.setWidget(0, QFormLayout.FieldRole, self.toolButton_43)


        self.verticalLayout_7.addLayout(self.formLayout_22)

        self.formLayout_23 = QFormLayout()
        self.formLayout_23.setObjectName(u"formLayout_23")
        self.formLayout_23.setVerticalSpacing(0)
        self.label_41 = QLabel(self.verticalLayoutWidget_7)
        self.label_41.setObjectName(u"label_41")

        self.formLayout_23.setWidget(0, QFormLayout.LabelRole, self.label_41)

        self.lineEdit_20 = QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setClearButtonEnabled(True)

        self.formLayout_23.setWidget(1, QFormLayout.LabelRole, self.lineEdit_20)

        self.toolButton_44 = QToolButton(self.verticalLayoutWidget_7)
        self.toolButton_44.setObjectName(u"toolButton_44")
        self.toolButton_44.setMaximumSize(QSize(30, 30))
        self.toolButton_44.setIcon(icon)
        self.toolButton_44.setIconSize(QSize(40, 40))
        self.toolButton_44.setCheckable(False)
        self.toolButton_44.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_44.setAutoRaise(False)
        self.toolButton_44.setArrowType(Qt.NoArrow)

        self.formLayout_23.setWidget(0, QFormLayout.FieldRole, self.toolButton_44)

        self.label_42 = QLabel(self.verticalLayoutWidget_7)
        self.label_42.setObjectName(u"label_42")

        self.formLayout_23.setWidget(1, QFormLayout.FieldRole, self.label_42)


        self.verticalLayout_7.addLayout(self.formLayout_23)

        self.formLayout_27 = QFormLayout()
        self.formLayout_27.setObjectName(u"formLayout_27")
        self.formLayout_27.setVerticalSpacing(0)
        self.label_43 = QLabel(self.verticalLayoutWidget_7)
        self.label_43.setObjectName(u"label_43")

        self.formLayout_27.setWidget(0, QFormLayout.LabelRole, self.label_43)

        self.lineEdit_21 = QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setClearButtonEnabled(True)

        self.formLayout_27.setWidget(1, QFormLayout.LabelRole, self.lineEdit_21)

        self.toolButton_45 = QToolButton(self.verticalLayoutWidget_7)
        self.toolButton_45.setObjectName(u"toolButton_45")
        self.toolButton_45.setMaximumSize(QSize(30, 30))
        self.toolButton_45.setIcon(icon)
        self.toolButton_45.setIconSize(QSize(40, 40))
        self.toolButton_45.setCheckable(False)
        self.toolButton_45.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_45.setAutoRaise(False)
        self.toolButton_45.setArrowType(Qt.NoArrow)

        self.formLayout_27.setWidget(0, QFormLayout.FieldRole, self.toolButton_45)

        self.label_44 = QLabel(self.verticalLayoutWidget_7)
        self.label_44.setObjectName(u"label_44")

        self.formLayout_27.setWidget(1, QFormLayout.FieldRole, self.label_44)


        self.verticalLayout_7.addLayout(self.formLayout_27)

        self.formLayout_28 = QFormLayout()
        self.formLayout_28.setObjectName(u"formLayout_28")
        self.formLayout_28.setVerticalSpacing(0)
        self.label_45 = QLabel(self.verticalLayoutWidget_7)
        self.label_45.setObjectName(u"label_45")

        self.formLayout_28.setWidget(0, QFormLayout.LabelRole, self.label_45)

        self.lineEdit_28 = QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setClearButtonEnabled(True)

        self.formLayout_28.setWidget(1, QFormLayout.LabelRole, self.lineEdit_28)

        self.toolButton_46 = QToolButton(self.verticalLayoutWidget_7)
        self.toolButton_46.setObjectName(u"toolButton_46")
        self.toolButton_46.setMaximumSize(QSize(30, 30))
        self.toolButton_46.setIcon(icon)
        self.toolButton_46.setIconSize(QSize(40, 40))
        self.toolButton_46.setCheckable(False)
        self.toolButton_46.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_46.setAutoRaise(False)
        self.toolButton_46.setArrowType(Qt.NoArrow)

        self.formLayout_28.setWidget(0, QFormLayout.FieldRole, self.toolButton_46)

        self.label_46 = QLabel(self.verticalLayoutWidget_7)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_28.setWidget(1, QFormLayout.FieldRole, self.label_46)


        self.verticalLayout_7.addLayout(self.formLayout_28)


        self.gridLayout.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayoutWidget_8 = QWidget(self.groupBox_8)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(20, 20, 321, 200))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_29 = QFormLayout()
        self.formLayout_29.setObjectName(u"formLayout_29")
        self.formLayout_29.setVerticalSpacing(0)
        self.label_47 = QLabel(self.verticalLayoutWidget_8)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_29.setWidget(0, QFormLayout.LabelRole, self.label_47)

        self.comboBox_7 = QComboBox(self.verticalLayoutWidget_8)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.formLayout_29.setWidget(1, QFormLayout.LabelRole, self.comboBox_7)

        self.toolButton_47 = QToolButton(self.verticalLayoutWidget_8)
        self.toolButton_47.setObjectName(u"toolButton_47")
        self.toolButton_47.setMaximumSize(QSize(30, 30))
        self.toolButton_47.setIcon(icon)
        self.toolButton_47.setIconSize(QSize(40, 40))
        self.toolButton_47.setCheckable(False)
        self.toolButton_47.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_47.setAutoRaise(False)
        self.toolButton_47.setArrowType(Qt.NoArrow)

        self.formLayout_29.setWidget(0, QFormLayout.FieldRole, self.toolButton_47)


        self.verticalLayout_8.addLayout(self.formLayout_29)

        self.formLayout_30 = QFormLayout()
        self.formLayout_30.setObjectName(u"formLayout_30")
        self.formLayout_30.setVerticalSpacing(0)
        self.label_48 = QLabel(self.verticalLayoutWidget_8)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_30.setWidget(0, QFormLayout.LabelRole, self.label_48)

        self.lineEdit_22 = QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setClearButtonEnabled(True)

        self.formLayout_30.setWidget(1, QFormLayout.LabelRole, self.lineEdit_22)

        self.toolButton_48 = QToolButton(self.verticalLayoutWidget_8)
        self.toolButton_48.setObjectName(u"toolButton_48")
        self.toolButton_48.setMaximumSize(QSize(30, 30))
        self.toolButton_48.setIcon(icon)
        self.toolButton_48.setIconSize(QSize(40, 40))
        self.toolButton_48.setCheckable(False)
        self.toolButton_48.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_48.setAutoRaise(False)
        self.toolButton_48.setArrowType(Qt.NoArrow)

        self.formLayout_30.setWidget(0, QFormLayout.FieldRole, self.toolButton_48)

        self.label_49 = QLabel(self.verticalLayoutWidget_8)
        self.label_49.setObjectName(u"label_49")

        self.formLayout_30.setWidget(1, QFormLayout.FieldRole, self.label_49)


        self.verticalLayout_8.addLayout(self.formLayout_30)

        self.formLayout_31 = QFormLayout()
        self.formLayout_31.setObjectName(u"formLayout_31")
        self.formLayout_31.setVerticalSpacing(0)
        self.label_51 = QLabel(self.verticalLayoutWidget_8)
        self.label_51.setObjectName(u"label_51")

        self.formLayout_31.setWidget(0, QFormLayout.LabelRole, self.label_51)

        self.lineEdit_23 = QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setClearButtonEnabled(True)

        self.formLayout_31.setWidget(1, QFormLayout.LabelRole, self.lineEdit_23)

        self.toolButton_49 = QToolButton(self.verticalLayoutWidget_8)
        self.toolButton_49.setObjectName(u"toolButton_49")
        self.toolButton_49.setMaximumSize(QSize(30, 30))
        self.toolButton_49.setIcon(icon)
        self.toolButton_49.setIconSize(QSize(40, 40))
        self.toolButton_49.setCheckable(False)
        self.toolButton_49.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_49.setAutoRaise(False)
        self.toolButton_49.setArrowType(Qt.NoArrow)

        self.formLayout_31.setWidget(0, QFormLayout.FieldRole, self.toolButton_49)

        self.label_52 = QLabel(self.verticalLayoutWidget_8)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_31.setWidget(1, QFormLayout.FieldRole, self.label_52)


        self.verticalLayout_8.addLayout(self.formLayout_31)


        self.gridLayout.addWidget(self.groupBox_8, 1, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayoutWidget_10 = QWidget(self.groupBox_12)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(20, 20, 331, 268))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout_41 = QFormLayout()
        self.formLayout_41.setObjectName(u"formLayout_41")
        self.formLayout_41.setVerticalSpacing(0)
        self.label_73 = QLabel(self.verticalLayoutWidget_10)
        self.label_73.setObjectName(u"label_73")

        self.formLayout_41.setWidget(0, QFormLayout.LabelRole, self.label_73)

        self.toolButton_59 = QToolButton(self.verticalLayoutWidget_10)
        self.toolButton_59.setObjectName(u"toolButton_59")
        self.toolButton_59.setMaximumSize(QSize(30, 30))
        self.toolButton_59.setIcon(icon)
        self.toolButton_59.setIconSize(QSize(40, 40))
        self.toolButton_59.setCheckable(False)
        self.toolButton_59.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_59.setAutoRaise(False)
        self.toolButton_59.setArrowType(Qt.NoArrow)

        self.formLayout_41.setWidget(0, QFormLayout.FieldRole, self.toolButton_59)

        self.comboBox_16 = QComboBox(self.verticalLayoutWidget_10)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")

        self.formLayout_41.setWidget(1, QFormLayout.LabelRole, self.comboBox_16)


        self.verticalLayout_10.addLayout(self.formLayout_41)

        self.formLayout_42 = QFormLayout()
        self.formLayout_42.setObjectName(u"formLayout_42")
        self.formLayout_42.setVerticalSpacing(0)
        self.lineEdit_45 = QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setClearButtonEnabled(True)

        self.formLayout_42.setWidget(1, QFormLayout.LabelRole, self.lineEdit_45)

        self.label_74 = QLabel(self.verticalLayoutWidget_10)
        self.label_74.setObjectName(u"label_74")

        self.formLayout_42.setWidget(0, QFormLayout.LabelRole, self.label_74)

        self.toolButton_60 = QToolButton(self.verticalLayoutWidget_10)
        self.toolButton_60.setObjectName(u"toolButton_60")
        self.toolButton_60.setMaximumSize(QSize(30, 30))
        self.toolButton_60.setIcon(icon)
        self.toolButton_60.setIconSize(QSize(40, 40))
        self.toolButton_60.setCheckable(False)
        self.toolButton_60.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_60.setAutoRaise(False)
        self.toolButton_60.setArrowType(Qt.NoArrow)

        self.formLayout_42.setWidget(0, QFormLayout.FieldRole, self.toolButton_60)

        self.label_75 = QLabel(self.verticalLayoutWidget_10)
        self.label_75.setObjectName(u"label_75")

        self.formLayout_42.setWidget(1, QFormLayout.FieldRole, self.label_75)


        self.verticalLayout_10.addLayout(self.formLayout_42)

        self.formLayout_43 = QFormLayout()
        self.formLayout_43.setObjectName(u"formLayout_43")
        self.formLayout_43.setVerticalSpacing(0)
        self.label_76 = QLabel(self.verticalLayoutWidget_10)
        self.label_76.setObjectName(u"label_76")

        self.formLayout_43.setWidget(0, QFormLayout.LabelRole, self.label_76)

        self.lineEdit_46 = QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setClearButtonEnabled(True)

        self.formLayout_43.setWidget(1, QFormLayout.LabelRole, self.lineEdit_46)

        self.toolButton_61 = QToolButton(self.verticalLayoutWidget_10)
        self.toolButton_61.setObjectName(u"toolButton_61")
        self.toolButton_61.setMaximumSize(QSize(30, 30))
        self.toolButton_61.setIcon(icon)
        self.toolButton_61.setIconSize(QSize(40, 40))
        self.toolButton_61.setCheckable(False)
        self.toolButton_61.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_61.setAutoRaise(False)
        self.toolButton_61.setArrowType(Qt.NoArrow)

        self.formLayout_43.setWidget(0, QFormLayout.FieldRole, self.toolButton_61)

        self.label_77 = QLabel(self.verticalLayoutWidget_10)
        self.label_77.setObjectName(u"label_77")

        self.formLayout_43.setWidget(1, QFormLayout.FieldRole, self.label_77)


        self.verticalLayout_10.addLayout(self.formLayout_43)

        self.formLayout_44 = QFormLayout()
        self.formLayout_44.setObjectName(u"formLayout_44")
        self.formLayout_44.setVerticalSpacing(0)
        self.label_78 = QLabel(self.verticalLayoutWidget_10)
        self.label_78.setObjectName(u"label_78")

        self.formLayout_44.setWidget(0, QFormLayout.LabelRole, self.label_78)

        self.lineEdit_38 = QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setClearButtonEnabled(True)

        self.formLayout_44.setWidget(1, QFormLayout.LabelRole, self.lineEdit_38)

        self.toolButton_62 = QToolButton(self.verticalLayoutWidget_10)
        self.toolButton_62.setObjectName(u"toolButton_62")
        self.toolButton_62.setMaximumSize(QSize(30, 30))
        self.toolButton_62.setIcon(icon)
        self.toolButton_62.setIconSize(QSize(40, 40))
        self.toolButton_62.setCheckable(False)
        self.toolButton_62.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_62.setAutoRaise(False)
        self.toolButton_62.setArrowType(Qt.NoArrow)

        self.formLayout_44.setWidget(0, QFormLayout.FieldRole, self.toolButton_62)

        self.label_79 = QLabel(self.verticalLayoutWidget_10)
        self.label_79.setObjectName(u"label_79")

        self.formLayout_44.setWidget(1, QFormLayout.FieldRole, self.label_79)


        self.verticalLayout_10.addLayout(self.formLayout_44)


        self.gridLayout.addWidget(self.groupBox_12, 1, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayoutWidget_11 = QWidget(self.groupBox_9)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(20, 20, 439, 244))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.formLayout_45 = QFormLayout()
        self.formLayout_45.setObjectName(u"formLayout_45")
        self.formLayout_45.setVerticalSpacing(0)
        self.label_80 = QLabel(self.verticalLayoutWidget_11)
        self.label_80.setObjectName(u"label_80")

        self.formLayout_45.setWidget(0, QFormLayout.LabelRole, self.label_80)

        self.comboBox_9 = QComboBox(self.verticalLayoutWidget_11)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.formLayout_45.setWidget(1, QFormLayout.LabelRole, self.comboBox_9)

        self.toolButton_63 = QToolButton(self.verticalLayoutWidget_11)
        self.toolButton_63.setObjectName(u"toolButton_63")
        self.toolButton_63.setMaximumSize(QSize(30, 30))
        self.toolButton_63.setIcon(icon)
        self.toolButton_63.setIconSize(QSize(40, 40))
        self.toolButton_63.setCheckable(False)
        self.toolButton_63.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_63.setAutoRaise(False)
        self.toolButton_63.setArrowType(Qt.NoArrow)

        self.formLayout_45.setWidget(0, QFormLayout.FieldRole, self.toolButton_63)


        self.verticalLayout_11.addLayout(self.formLayout_45)

        self.formLayout_46 = QFormLayout()
        self.formLayout_46.setObjectName(u"formLayout_46")
        self.formLayout_46.setVerticalSpacing(0)
        self.label_81 = QLabel(self.verticalLayoutWidget_11)
        self.label_81.setObjectName(u"label_81")

        self.formLayout_46.setWidget(0, QFormLayout.LabelRole, self.label_81)

        self.toolButton_64 = QToolButton(self.verticalLayoutWidget_11)
        self.toolButton_64.setObjectName(u"toolButton_64")
        self.toolButton_64.setMaximumSize(QSize(30, 30))
        self.toolButton_64.setIcon(icon)
        self.toolButton_64.setIconSize(QSize(40, 40))
        self.toolButton_64.setCheckable(False)
        self.toolButton_64.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_64.setAutoRaise(False)
        self.toolButton_64.setArrowType(Qt.NoArrow)

        self.formLayout_46.setWidget(0, QFormLayout.FieldRole, self.toolButton_64)

        self.lineEdit_32 = QLineEdit(self.verticalLayoutWidget_11)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_32.setFrame(True)
        self.lineEdit_32.setDragEnabled(False)
        self.lineEdit_32.setClearButtonEnabled(True)

        self.formLayout_46.setWidget(1, QFormLayout.LabelRole, self.lineEdit_32)

        self.label_82 = QLabel(self.verticalLayoutWidget_11)
        self.label_82.setObjectName(u"label_82")

        self.formLayout_46.setWidget(1, QFormLayout.FieldRole, self.label_82)


        self.verticalLayout_11.addLayout(self.formLayout_46)

        self.formLayout_47 = QFormLayout()
        self.formLayout_47.setObjectName(u"formLayout_47")
        self.formLayout_47.setVerticalSpacing(0)
        self.label_83 = QLabel(self.verticalLayoutWidget_11)
        self.label_83.setObjectName(u"label_83")

        self.formLayout_47.setWidget(0, QFormLayout.LabelRole, self.label_83)

        self.toolButton_65 = QToolButton(self.verticalLayoutWidget_11)
        self.toolButton_65.setObjectName(u"toolButton_65")
        self.toolButton_65.setMaximumSize(QSize(30, 30))
        self.toolButton_65.setIcon(icon)
        self.toolButton_65.setIconSize(QSize(40, 40))
        self.toolButton_65.setCheckable(False)
        self.toolButton_65.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_65.setAutoRaise(False)
        self.toolButton_65.setArrowType(Qt.NoArrow)

        self.formLayout_47.setWidget(0, QFormLayout.FieldRole, self.toolButton_65)

        self.lineEdit_33 = QLineEdit(self.verticalLayoutWidget_11)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setClearButtonEnabled(True)

        self.formLayout_47.setWidget(1, QFormLayout.LabelRole, self.lineEdit_33)

        self.label_84 = QLabel(self.verticalLayoutWidget_11)
        self.label_84.setObjectName(u"label_84")

        self.formLayout_47.setWidget(1, QFormLayout.FieldRole, self.label_84)


        self.verticalLayout_11.addLayout(self.formLayout_47)

        self.formLayout_48 = QFormLayout()
        self.formLayout_48.setObjectName(u"formLayout_48")
        self.formLayout_48.setVerticalSpacing(0)
        self.label_85 = QLabel(self.verticalLayoutWidget_11)
        self.label_85.setObjectName(u"label_85")

        self.formLayout_48.setWidget(0, QFormLayout.LabelRole, self.label_85)

        self.toolButton_66 = QToolButton(self.verticalLayoutWidget_11)
        self.toolButton_66.setObjectName(u"toolButton_66")
        self.toolButton_66.setMaximumSize(QSize(30, 30))
        self.toolButton_66.setIcon(icon)
        self.toolButton_66.setIconSize(QSize(40, 40))
        self.toolButton_66.setCheckable(False)
        self.toolButton_66.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_66.setAutoRaise(False)
        self.toolButton_66.setArrowType(Qt.NoArrow)

        self.formLayout_48.setWidget(0, QFormLayout.FieldRole, self.toolButton_66)

        self.lineEdit_34 = QLineEdit(self.verticalLayoutWidget_11)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setClearButtonEnabled(True)

        self.formLayout_48.setWidget(1, QFormLayout.LabelRole, self.lineEdit_34)

        self.label_86 = QLabel(self.verticalLayoutWidget_11)
        self.label_86.setObjectName(u"label_86")

        self.formLayout_48.setWidget(1, QFormLayout.FieldRole, self.label_86)


        self.verticalLayout_11.addLayout(self.formLayout_48)


        self.gridLayout.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayoutWidget_9 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(20, 10, 301, 602))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.formLayout_32 = QFormLayout()
        self.formLayout_32.setObjectName(u"formLayout_32")
        self.formLayout_32.setHorizontalSpacing(0)
        self.formLayout_32.setVerticalSpacing(0)
        self.label_53 = QLabel(self.verticalLayoutWidget_9)
        self.label_53.setObjectName(u"label_53")

        self.formLayout_32.setWidget(0, QFormLayout.LabelRole, self.label_53)

        self.comboBox_8 = QComboBox(self.verticalLayoutWidget_9)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_32.setWidget(1, QFormLayout.LabelRole, self.comboBox_8)

        self.toolButton_50 = QToolButton(self.verticalLayoutWidget_9)
        self.toolButton_50.setObjectName(u"toolButton_50")
        self.toolButton_50.setMaximumSize(QSize(30, 30))
        self.toolButton_50.setIcon(icon)
        self.toolButton_50.setIconSize(QSize(40, 40))
        self.toolButton_50.setCheckable(False)
        self.toolButton_50.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_50.setAutoRaise(False)
        self.toolButton_50.setArrowType(Qt.NoArrow)

        self.formLayout_32.setWidget(0, QFormLayout.FieldRole, self.toolButton_50)


        self.verticalLayout_9.addLayout(self.formLayout_32)

        self.formLayout_33 = QFormLayout()
        self.formLayout_33.setObjectName(u"formLayout_33")
        self.formLayout_33.setHorizontalSpacing(6)
        self.formLayout_33.setVerticalSpacing(0)
        self.label_54 = QLabel(self.verticalLayoutWidget_9)
        self.label_54.setObjectName(u"label_54")

        self.formLayout_33.setWidget(0, QFormLayout.LabelRole, self.label_54)

        self.lineEdit_13 = QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setClearButtonEnabled(True)

        self.formLayout_33.setWidget(1, QFormLayout.LabelRole, self.lineEdit_13)

        self.toolButton_51 = QToolButton(self.verticalLayoutWidget_9)
        self.toolButton_51.setObjectName(u"toolButton_51")
        self.toolButton_51.setMaximumSize(QSize(30, 30))
        self.toolButton_51.setIcon(icon)
        self.toolButton_51.setIconSize(QSize(40, 40))
        self.toolButton_51.setCheckable(False)
        self.toolButton_51.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_51.setAutoRaise(False)
        self.toolButton_51.setArrowType(Qt.NoArrow)

        self.formLayout_33.setWidget(0, QFormLayout.FieldRole, self.toolButton_51)

        self.label_55 = QLabel(self.verticalLayoutWidget_9)
        self.label_55.setObjectName(u"label_55")

        self.formLayout_33.setWidget(1, QFormLayout.FieldRole, self.label_55)


        self.verticalLayout_9.addLayout(self.formLayout_33)

        self.formLayout_34 = QFormLayout()
        self.formLayout_34.setObjectName(u"formLayout_34")
        self.formLayout_34.setVerticalSpacing(0)
        self.label_56 = QLabel(self.verticalLayoutWidget_9)
        self.label_56.setObjectName(u"label_56")

        self.formLayout_34.setWidget(0, QFormLayout.LabelRole, self.label_56)

        self.lineEdit_14 = QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setClearButtonEnabled(True)

        self.formLayout_34.setWidget(1, QFormLayout.LabelRole, self.lineEdit_14)

        self.toolButton_52 = QToolButton(self.verticalLayoutWidget_9)
        self.toolButton_52.setObjectName(u"toolButton_52")
        self.toolButton_52.setMaximumSize(QSize(30, 30))
        self.toolButton_52.setIcon(icon)
        self.toolButton_52.setIconSize(QSize(40, 40))
        self.toolButton_52.setCheckable(False)
        self.toolButton_52.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_52.setAutoRaise(False)
        self.toolButton_52.setArrowType(Qt.NoArrow)

        self.formLayout_34.setWidget(0, QFormLayout.FieldRole, self.toolButton_52)

        self.label_57 = QLabel(self.verticalLayoutWidget_9)
        self.label_57.setObjectName(u"label_57")

        self.formLayout_34.setWidget(1, QFormLayout.FieldRole, self.label_57)


        self.verticalLayout_9.addLayout(self.formLayout_34)

        self.formLayout_35 = QFormLayout()
        self.formLayout_35.setObjectName(u"formLayout_35")
        self.formLayout_35.setHorizontalSpacing(6)
        self.formLayout_35.setVerticalSpacing(0)
        self.label_58 = QLabel(self.verticalLayoutWidget_9)
        self.label_58.setObjectName(u"label_58")

        self.formLayout_35.setWidget(0, QFormLayout.LabelRole, self.label_58)

        self.lineEdit_24 = QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setClearButtonEnabled(True)

        self.formLayout_35.setWidget(1, QFormLayout.LabelRole, self.lineEdit_24)

        self.toolButton_53 = QToolButton(self.verticalLayoutWidget_9)
        self.toolButton_53.setObjectName(u"toolButton_53")
        self.toolButton_53.setMaximumSize(QSize(30, 30))
        self.toolButton_53.setIcon(icon)
        self.toolButton_53.setIconSize(QSize(40, 40))
        self.toolButton_53.setCheckable(False)
        self.toolButton_53.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_53.setAutoRaise(False)
        self.toolButton_53.setArrowType(Qt.NoArrow)

        self.formLayout_35.setWidget(0, QFormLayout.FieldRole, self.toolButton_53)

        self.label_59 = QLabel(self.verticalLayoutWidget_9)
        self.label_59.setObjectName(u"label_59")

        self.formLayout_35.setWidget(1, QFormLayout.FieldRole, self.label_59)


        self.verticalLayout_9.addLayout(self.formLayout_35)

        self.formLayout_36 = QFormLayout()
        self.formLayout_36.setObjectName(u"formLayout_36")
        self.formLayout_36.setVerticalSpacing(0)
        self.label_63 = QLabel(self.verticalLayoutWidget_9)
        self.label_63.setObjectName(u"label_63")

        self.formLayout_36.setWidget(0, QFormLayout.LabelRole, self.label_63)

        self.lineEdit_25 = QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setClearButtonEnabled(True)

        self.formLayout_36.setWidget(1, QFormLayout.LabelRole, self.lineEdit_25)

        self.toolButton_54 = QToolButton(self.verticalLayoutWidget_9)
        self.toolButton_54.setObjectName(u"toolButton_54")
        self.toolButton_54.setMaximumSize(QSize(30, 30))
        self.toolButton_54.setIcon(icon)
        self.toolButton_54.setIconSize(QSize(40, 40))
        self.toolButton_54.setCheckable(False)
        self.toolButton_54.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_54.setAutoRaise(False)
        self.toolButton_54.setArrowType(Qt.NoArrow)

        self.formLayout_36.setWidget(0, QFormLayout.FieldRole, self.toolButton_54)

        self.label_64 = QLabel(self.verticalLayoutWidget_9)
        self.label_64.setObjectName(u"label_64")

        self.formLayout_36.setWidget(1, QFormLayout.FieldRole, self.label_64)


        self.verticalLayout_9.addLayout(self.formLayout_36)

        self.formLayout_37 = QFormLayout()
        self.formLayout_37.setObjectName(u"formLayout_37")
        self.formLayout_37.setVerticalSpacing(0)
        self.label_65 = QLabel(self.verticalLayoutWidget_9)
        self.label_65.setObjectName(u"label_65")

        self.formLayout_37.setWidget(0, QFormLayout.LabelRole, self.label_65)

        self.lineEdit_26 = QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setClearButtonEnabled(True)

        self.formLayout_37.setWidget(1, QFormLayout.LabelRole, self.lineEdit_26)

        self.toolButton_55 = QToolButton(self.verticalLayoutWidget_9)
        self.toolButton_55.setObjectName(u"toolButton_55")
        self.toolButton_55.setMaximumSize(QSize(30, 30))
        self.toolButton_55.setIcon(icon)
        self.toolButton_55.setIconSize(QSize(40, 40))
        self.toolButton_55.setCheckable(False)
        self.toolButton_55.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_55.setAutoRaise(False)
        self.toolButton_55.setArrowType(Qt.NoArrow)

        self.formLayout_37.setWidget(0, QFormLayout.FieldRole, self.toolButton_55)

        self.label_66 = QLabel(self.verticalLayoutWidget_9)
        self.label_66.setObjectName(u"label_66")

        self.formLayout_37.setWidget(1, QFormLayout.FieldRole, self.label_66)


        self.verticalLayout_9.addLayout(self.formLayout_37)

        self.formLayout_38 = QFormLayout()
        self.formLayout_38.setObjectName(u"formLayout_38")
        self.formLayout_38.setVerticalSpacing(0)
        self.label_67 = QLabel(self.verticalLayoutWidget_9)
        self.label_67.setObjectName(u"label_67")

        self.formLayout_38.setWidget(0, QFormLayout.LabelRole, self.label_67)

        self.lineEdit_29 = QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setClearButtonEnabled(True)

        self.formLayout_38.setWidget(1, QFormLayout.LabelRole, self.lineEdit_29)

        self.toolButton_56 = QToolButton(self.verticalLayoutWidget_9)
        self.toolButton_56.setObjectName(u"toolButton_56")
        self.toolButton_56.setMaximumSize(QSize(30, 30))
        self.toolButton_56.setIcon(icon)
        self.toolButton_56.setIconSize(QSize(40, 40))
        self.toolButton_56.setCheckable(False)
        self.toolButton_56.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_56.setAutoRaise(False)
        self.toolButton_56.setArrowType(Qt.NoArrow)

        self.formLayout_38.setWidget(0, QFormLayout.FieldRole, self.toolButton_56)

        self.label_68 = QLabel(self.verticalLayoutWidget_9)
        self.label_68.setObjectName(u"label_68")

        self.formLayout_38.setWidget(1, QFormLayout.FieldRole, self.label_68)


        self.verticalLayout_9.addLayout(self.formLayout_38)

        self.formLayout_39 = QFormLayout()
        self.formLayout_39.setObjectName(u"formLayout_39")
        self.formLayout_39.setVerticalSpacing(0)
        self.label_69 = QLabel(self.verticalLayoutWidget_9)
        self.label_69.setObjectName(u"label_69")

        self.formLayout_39.setWidget(0, QFormLayout.LabelRole, self.label_69)

        self.lineEdit_30 = QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setClearButtonEnabled(True)

        self.formLayout_39.setWidget(1, QFormLayout.LabelRole, self.lineEdit_30)

        self.toolButton_57 = QToolButton(self.verticalLayoutWidget_9)
        self.toolButton_57.setObjectName(u"toolButton_57")
        self.toolButton_57.setMaximumSize(QSize(30, 30))
        self.toolButton_57.setIcon(icon)
        self.toolButton_57.setIconSize(QSize(40, 40))
        self.toolButton_57.setCheckable(False)
        self.toolButton_57.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_57.setAutoRaise(False)
        self.toolButton_57.setArrowType(Qt.NoArrow)

        self.formLayout_39.setWidget(0, QFormLayout.FieldRole, self.toolButton_57)

        self.label_70 = QLabel(self.verticalLayoutWidget_9)
        self.label_70.setObjectName(u"label_70")

        self.formLayout_39.setWidget(1, QFormLayout.FieldRole, self.label_70)


        self.verticalLayout_9.addLayout(self.formLayout_39)

        self.formLayout_40 = QFormLayout()
        self.formLayout_40.setObjectName(u"formLayout_40")
        self.formLayout_40.setVerticalSpacing(0)
        self.label_71 = QLabel(self.verticalLayoutWidget_9)
        self.label_71.setObjectName(u"label_71")

        self.formLayout_40.setWidget(0, QFormLayout.LabelRole, self.label_71)

        self.lineEdit_31 = QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setClearButtonEnabled(True)

        self.formLayout_40.setWidget(1, QFormLayout.LabelRole, self.lineEdit_31)

        self.toolButton_58 = QToolButton(self.verticalLayoutWidget_9)
        self.toolButton_58.setObjectName(u"toolButton_58")
        self.toolButton_58.setMaximumSize(QSize(30, 30))
        self.toolButton_58.setIcon(icon)
        self.toolButton_58.setIconSize(QSize(40, 40))
        self.toolButton_58.setCheckable(False)
        self.toolButton_58.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_58.setAutoRaise(False)
        self.toolButton_58.setArrowType(Qt.NoArrow)

        self.formLayout_40.setWidget(0, QFormLayout.FieldRole, self.toolButton_58)

        self.label_72 = QLabel(self.verticalLayoutWidget_9)
        self.label_72.setObjectName(u"label_72")

        self.formLayout_40.setWidget(1, QFormLayout.FieldRole, self.label_72)


        self.verticalLayout_9.addLayout(self.formLayout_40)


        self.gridLayout.addWidget(self.groupBox_4, 0, 2, 2, 1)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(880, 660, 168, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1156, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addSeparator()

        self.retranslateUi(MainWindow)
        self.comboBox_16.currentIndexChanged.connect(self.label_74.hide)
        self.comboBox_16.currentIndexChanged.connect(self.label_75.hide)
        self.comboBox_16.currentIndexChanged.connect(self.lineEdit_45.hide)
        self.comboBox_16.currentIndexChanged.connect(self.toolButton_60.hide)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SubStationGuard", None))
        self.groupBox_7.setTitle("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Calculate Maximum Grid Current according to IEEE Std 80", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Symmetrical Ground Fault Current", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_20.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'If', Unit of Measurement: 'A')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_42.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Fault Current Division Factor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_21.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'Sf', Unit of Measurement: 'p.u,')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_44.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Maximum Grid Current", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_28.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'IG', Unit of Measurement: 'A')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_46.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.groupBox_8.setTitle("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Calculate Soil Resistivity through Ground Resistance", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Ground Resistance", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_22.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'Rg', Unit of Measurement: '\u03a9')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_49.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Soil Resistivity", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_23.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: '\u03c1', Unit of Measurement: '\u03a9m')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_52.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u03a9m", None))
        self.groupBox_12.setTitle("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Calculate Decrement Factor according to IEEE Std 80", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

#if QT_CONFIG(tooltip)
        self.lineEdit_45.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'X', Unit of Measurement: '\u03a9')", None))
#endif // QT_CONFIG(tooltip)
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Inductive Reactance", None))
#if QT_CONFIG(tooltip)
        self.label_75.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"System resistance at fault", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_46.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'R', Unit of Measurement: '\u03a9')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_77.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Decrement Factor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_38.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'Df', Unit of Measurement: 'p.u.')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_79.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.groupBox_9.setTitle("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"System Type of MV/LV Substation", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"TN", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"TT", None))

#if QT_CONFIG(tooltip)
        self.toolButton_63.setToolTip(QCoreApplication.translate("MainWindow", u"Type of the Medium Voltage/ Low Voltage Substation", None))
#endif // QT_CONFIG(tooltip)
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Geometric proportionality factor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_32.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'kg', Unit of Measurement: 'm^-1')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_82.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"m^-1", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Surface potential proportionality factor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_33.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'ksp', Function)", None))
#endif // QT_CONFIG(tooltip)
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"function", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Fault Duration", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_34.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'tf', Unit of Measurement: 's')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_86.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.groupBox_4.setTitle("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Safety Standard", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"IEEE Std 80", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"CENELEC EN 50522", None))

        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Resistance of the human body", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_13.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'Rb', Unit of Measurement: '\u03a9')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_55.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Factor related to tolerable electric shock energy", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_14.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'k', Unit of Measurement: 'A\u221as')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_57.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"A\u221as", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Body current limit", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_24.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'IB', Unit of Measurement: 'A')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_59.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Body impedance", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_25.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'ZT', Unit of Measurement: '\u03a9')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_64.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Heart current factor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_26.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'HF', Unit of Measurement: 'p.u.')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_66.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Body factor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_29.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'BF', Unit of Measurement: 'p.u.')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_68.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Constant F", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_30.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'F', Unit of Measurement: 'p.u.')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_70.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Voltage limit", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_31.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'Vlim', Unit of Measurement: 'V')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_72.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Evaluate", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

