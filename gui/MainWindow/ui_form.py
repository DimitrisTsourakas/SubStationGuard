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
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QSize(1280, 800))
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
        icon = QIcon()
        icon.addFile(u":/images/images/SubStationGuard.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.actionImport_Parameters = QAction(MainWindow)
        self.actionImport_Parameters.setObjectName(u"actionImport_Parameters")
        self.actionExport_Parameters = QAction(MainWindow)
        self.actionExport_Parameters.setObjectName(u"actionExport_Parameters")
        self.actionShow_Logs = QAction(MainWindow)
        self.actionShow_Logs.setObjectName(u"actionShow_Logs")
        self.actionShow_Logs.setCheckable(True)
        self.actionShow_Logs.setChecked(True)
        self.actionShow_Parameters = QAction(MainWindow)
        self.actionShow_Parameters.setObjectName(u"actionShow_Parameters")
        self.actionShow_Parameters.setCheckable(True)
        self.actionShow_Parameters.setChecked(True)
        self.actionShow_Plot = QAction(MainWindow)
        self.actionShow_Plot.setObjectName(u"actionShow_Plot")
        self.actionShow_Plot.setCheckable(True)
        self.actionShow_Plot.setChecked(True)
        self.actionSave_Plot = QAction(MainWindow)
        self.actionSave_Plot.setObjectName(u"actionSave_Plot")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setEnabled(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_2 = QVBoxLayout(self.tab_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(self.tab_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.tabWidget_2, 1, 0, 1, 2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy1)
        self.tab.setTabletTracking(False)
        self.gridLayout_27 = QGridLayout(self.tab)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setSizeConstraint(QLayout.SetFixedSize)
        self.groupBox_9 = QGroupBox(self.tab)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy2)
        self.groupBox_9.setMaximumSize(QSize(506, 476))
        self.groupBox_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout_29 = QGridLayout(self.groupBox_9)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_3.setContentsMargins(-1, -1, 10, -1)
        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_30.setHorizontalSpacing(6)
        self.gridLayout_30.setVerticalSpacing(0)
        self.label_80 = QLabel(self.groupBox_9)
        self.label_80.setObjectName(u"label_80")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label_80.setFont(font)

        self.gridLayout_30.addWidget(self.label_80, 0, 0, 1, 1)

        self.toolButton_63 = QToolButton(self.groupBox_9)
        self.toolButton_63.setObjectName(u"toolButton_63")
        self.toolButton_63.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/info-tooltip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_63.setIcon(icon1)
        self.toolButton_63.setIconSize(QSize(40, 40))
        self.toolButton_63.setCheckable(False)
        self.toolButton_63.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_63.setAutoRaise(False)
        self.toolButton_63.setArrowType(Qt.NoArrow)

        self.gridLayout_30.addWidget(self.toolButton_63, 0, 1, 1, 1)

        self.comboBox_9 = QComboBox(self.groupBox_9)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_30.addWidget(self.comboBox_9, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_30)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setVerticalSpacing(0)
        self.label_81 = QLabel(self.groupBox_9)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font)

        self.gridLayout_6.addWidget(self.label_81, 0, 0, 1, 1)

        self.toolButton_64 = QToolButton(self.groupBox_9)
        self.toolButton_64.setObjectName(u"toolButton_64")
        self.toolButton_64.setMaximumSize(QSize(30, 30))
        self.toolButton_64.setIcon(icon1)
        self.toolButton_64.setIconSize(QSize(40, 40))
        self.toolButton_64.setCheckable(False)
        self.toolButton_64.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_64.setAutoRaise(False)
        self.toolButton_64.setArrowType(Qt.NoArrow)

        self.gridLayout_6.addWidget(self.toolButton_64, 0, 1, 1, 1)

        self.lineEdit_32 = QLineEdit(self.groupBox_9)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_32.setFrame(True)
        self.lineEdit_32.setDragEnabled(False)
        self.lineEdit_32.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.lineEdit_32, 1, 0, 1, 1)

        self.label_82 = QLabel(self.groupBox_9)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_6.addWidget(self.label_82, 1, 1, 1, 1)

        self.label_102 = QLabel(self.groupBox_9)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setEnabled(False)
        self.label_102.setStyleSheet(u"color: rgb(170, 0, 0)")
        self.label_102.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_6.addWidget(self.label_102, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_6)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(5)
        self.label_83 = QLabel(self.groupBox_9)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font)

        self.gridLayout_3.addWidget(self.label_83, 0, 0, 1, 1)

        self.toolButton_65 = QToolButton(self.groupBox_9)
        self.toolButton_65.setObjectName(u"toolButton_65")
        self.toolButton_65.setMaximumSize(QSize(30, 30))
        self.toolButton_65.setIcon(icon1)
        self.toolButton_65.setIconSize(QSize(40, 40))
        self.toolButton_65.setCheckable(False)
        self.toolButton_65.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_65.setAutoRaise(False)
        self.toolButton_65.setArrowType(Qt.NoArrow)

        self.gridLayout_3.addWidget(self.toolButton_65, 0, 1, 1, 1)

        self.lineEdit_33 = QLineEdit(self.groupBox_9)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.lineEdit_33, 2, 0, 1, 1)

        self.label_84 = QLabel(self.groupBox_9)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_3.addWidget(self.label_84, 2, 1, 1, 1)

        self.label_101 = QLabel(self.groupBox_9)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy2)
        self.label_101.setLayoutDirection(Qt.LeftToRight)
        self.label_101.setStyleSheet(u"color: rgb(170, 0, 0)")
        self.label_101.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.label_101, 3, 0, 1, 1)

        self.lineEdit_35 = QLineEdit(self.groupBox_9)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.lineEdit_35, 4, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_9)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/images/images/upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(14, 14))

        self.gridLayout_3.addWidget(self.pushButton, 4, 1, 1, 1)

        self.comboBox_10 = QComboBox(self.groupBox_9)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.comboBox_10, 1, 0, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_5.setVerticalSpacing(0)
        self.label_85 = QLabel(self.groupBox_9)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font)

        self.gridLayout_5.addWidget(self.label_85, 0, 0, 1, 1)

        self.toolButton_66 = QToolButton(self.groupBox_9)
        self.toolButton_66.setObjectName(u"toolButton_66")
        self.toolButton_66.setMaximumSize(QSize(30, 30))
        self.toolButton_66.setIcon(icon1)
        self.toolButton_66.setIconSize(QSize(40, 40))
        self.toolButton_66.setCheckable(False)
        self.toolButton_66.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_66.setAutoRaise(False)
        self.toolButton_66.setArrowType(Qt.NoArrow)

        self.gridLayout_5.addWidget(self.toolButton_66, 0, 1, 1, 1)

        self.lineEdit_34 = QLineEdit(self.groupBox_9)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.lineEdit_34, 1, 0, 1, 1)

        self.label_86 = QLabel(self.groupBox_9)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_5.addWidget(self.label_86, 1, 1, 1, 1)

        self.label_100 = QLabel(self.groupBox_9)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setEnabled(False)
        self.label_100.setStyleSheet(u"color: rgb(170, 0, 0)")
        self.label_100.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.label_100, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_5)


        self.gridLayout_29.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        sizePolicy1.setHeightForWidth(self.tab_4.sizePolicy().hasHeightForWidth())
        self.tab_4.setSizePolicy(sizePolicy1)
        self.gridLayout_32 = QGridLayout(self.tab_4)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setSizeConstraint(QLayout.SetFixedSize)
        self.groupBox_8 = QGroupBox(self.tab_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMaximumSize(QSize(506, 476))
        self.groupBox_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout_33 = QGridLayout(self.groupBox_8)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_8.setVerticalSpacing(0)
        self.label_47 = QLabel(self.groupBox_8)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)

        self.gridLayout_8.addWidget(self.label_47, 0, 0, 1, 1)

        self.toolButton_47 = QToolButton(self.groupBox_8)
        self.toolButton_47.setObjectName(u"toolButton_47")
        self.toolButton_47.setMaximumSize(QSize(30, 30))
        self.toolButton_47.setIcon(icon1)
        self.toolButton_47.setIconSize(QSize(40, 40))
        self.toolButton_47.setCheckable(False)
        self.toolButton_47.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_47.setAutoRaise(False)
        self.toolButton_47.setArrowType(Qt.NoArrow)

        self.gridLayout_8.addWidget(self.toolButton_47, 0, 1, 1, 1)

        self.comboBox_7 = QComboBox(self.groupBox_8)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.comboBox_7, 1, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_8)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_9.setVerticalSpacing(0)
        self.label_48 = QLabel(self.groupBox_8)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.gridLayout_9.addWidget(self.label_48, 0, 0, 1, 1)

        self.toolButton_48 = QToolButton(self.groupBox_8)
        self.toolButton_48.setObjectName(u"toolButton_48")
        self.toolButton_48.setMaximumSize(QSize(30, 30))
        self.toolButton_48.setIcon(icon1)
        self.toolButton_48.setIconSize(QSize(40, 40))
        self.toolButton_48.setCheckable(False)
        self.toolButton_48.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_48.setAutoRaise(False)
        self.toolButton_48.setArrowType(Qt.NoArrow)

        self.gridLayout_9.addWidget(self.toolButton_48, 0, 1, 1, 1)

        self.lineEdit_22 = QLineEdit(self.groupBox_8)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setClearButtonEnabled(True)

        self.gridLayout_9.addWidget(self.lineEdit_22, 1, 0, 1, 1)

        self.label_49 = QLabel(self.groupBox_8)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_9.addWidget(self.label_49, 1, 1, 1, 1)

        self.label_61 = QLabel(self.groupBox_8)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setEnabled(False)
        self.label_61.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_9.addWidget(self.label_61, 2, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_9)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_10.setVerticalSpacing(0)
        self.label_51 = QLabel(self.groupBox_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.gridLayout_10.addWidget(self.label_51, 0, 0, 1, 1)

        self.toolButton_49 = QToolButton(self.groupBox_8)
        self.toolButton_49.setObjectName(u"toolButton_49")
        self.toolButton_49.setMaximumSize(QSize(30, 30))
        self.toolButton_49.setIcon(icon1)
        self.toolButton_49.setIconSize(QSize(40, 40))
        self.toolButton_49.setCheckable(False)
        self.toolButton_49.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_49.setAutoRaise(False)
        self.toolButton_49.setArrowType(Qt.NoArrow)

        self.gridLayout_10.addWidget(self.toolButton_49, 0, 1, 1, 1)

        self.lineEdit_23 = QLineEdit(self.groupBox_8)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setClearButtonEnabled(True)

        self.gridLayout_10.addWidget(self.lineEdit_23, 1, 0, 1, 1)

        self.label_52 = QLabel(self.groupBox_8)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_10.addWidget(self.label_52, 1, 1, 1, 1)

        self.label_60 = QLabel(self.groupBox_8)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setEnabled(False)
        self.label_60.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_10.addWidget(self.label_60, 2, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_10)


        self.gridLayout_33.addLayout(self.verticalLayout_8, 0, 0, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        sizePolicy1.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.groupBox_7 = QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(506, 476))
        self.groupBox_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout_28 = QGridLayout(self.groupBox_7)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_11.setVerticalSpacing(0)
        self.label_40 = QLabel(self.groupBox_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font)

        self.gridLayout_11.addWidget(self.label_40, 0, 0, 1, 1)

        self.toolButton_43 = QToolButton(self.groupBox_7)
        self.toolButton_43.setObjectName(u"toolButton_43")
        self.toolButton_43.setMaximumSize(QSize(30, 30))
        self.toolButton_43.setIcon(icon1)
        self.toolButton_43.setIconSize(QSize(40, 40))
        self.toolButton_43.setCheckable(False)
        self.toolButton_43.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_43.setAutoRaise(False)
        self.toolButton_43.setArrowType(Qt.NoArrow)

        self.gridLayout_11.addWidget(self.toolButton_43, 0, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.groupBox_7)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_11.addWidget(self.comboBox_6, 1, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_11)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setVerticalSpacing(0)
        self.label_41 = QLabel(self.groupBox_7)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.gridLayout_12.addWidget(self.label_41, 0, 0, 1, 1)

        self.toolButton_44 = QToolButton(self.groupBox_7)
        self.toolButton_44.setObjectName(u"toolButton_44")
        self.toolButton_44.setMaximumSize(QSize(30, 30))
        self.toolButton_44.setIcon(icon1)
        self.toolButton_44.setIconSize(QSize(40, 40))
        self.toolButton_44.setCheckable(False)
        self.toolButton_44.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_44.setAutoRaise(False)
        self.toolButton_44.setArrowType(Qt.NoArrow)

        self.gridLayout_12.addWidget(self.toolButton_44, 0, 1, 1, 1)

        self.lineEdit_20 = QLineEdit(self.groupBox_7)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setClearButtonEnabled(True)

        self.gridLayout_12.addWidget(self.lineEdit_20, 1, 0, 1, 1)

        self.label_42 = QLabel(self.groupBox_7)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_12.addWidget(self.label_42, 1, 1, 1, 1)

        self.label_97 = QLabel(self.groupBox_7)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setEnabled(False)
        self.label_97.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_12.addWidget(self.label_97, 2, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_12)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(0)
        self.label_43 = QLabel(self.groupBox_7)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.gridLayout_13.addWidget(self.label_43, 0, 0, 1, 1)

        self.toolButton_45 = QToolButton(self.groupBox_7)
        self.toolButton_45.setObjectName(u"toolButton_45")
        self.toolButton_45.setMaximumSize(QSize(30, 30))
        self.toolButton_45.setIcon(icon1)
        self.toolButton_45.setIconSize(QSize(40, 40))
        self.toolButton_45.setCheckable(False)
        self.toolButton_45.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_45.setAutoRaise(False)
        self.toolButton_45.setArrowType(Qt.NoArrow)

        self.gridLayout_13.addWidget(self.toolButton_45, 0, 1, 1, 1)

        self.lineEdit_21 = QLineEdit(self.groupBox_7)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setClearButtonEnabled(True)

        self.gridLayout_13.addWidget(self.lineEdit_21, 1, 0, 1, 1)

        self.label_44 = QLabel(self.groupBox_7)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_13.addWidget(self.label_44, 1, 1, 1, 1)

        self.label_98 = QLabel(self.groupBox_7)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setEnabled(False)
        self.label_98.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_13.addWidget(self.label_98, 2, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_13)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setVerticalSpacing(0)
        self.label_45 = QLabel(self.groupBox_7)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)

        self.gridLayout_14.addWidget(self.label_45, 0, 0, 1, 1)

        self.toolButton_46 = QToolButton(self.groupBox_7)
        self.toolButton_46.setObjectName(u"toolButton_46")
        self.toolButton_46.setMaximumSize(QSize(30, 30))
        self.toolButton_46.setIcon(icon1)
        self.toolButton_46.setIconSize(QSize(40, 40))
        self.toolButton_46.setCheckable(False)
        self.toolButton_46.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_46.setAutoRaise(False)
        self.toolButton_46.setArrowType(Qt.NoArrow)

        self.gridLayout_14.addWidget(self.toolButton_46, 0, 1, 1, 1)

        self.lineEdit_28 = QLineEdit(self.groupBox_7)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setClearButtonEnabled(True)

        self.gridLayout_14.addWidget(self.lineEdit_28, 1, 0, 1, 1)

        self.label_46 = QLabel(self.groupBox_7)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_14.addWidget(self.label_46, 1, 1, 1, 1)

        self.label_99 = QLabel(self.groupBox_7)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setEnabled(False)
        self.label_99.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_14.addWidget(self.label_99, 2, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_14)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(0)
        self.label_73 = QLabel(self.groupBox_7)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font)

        self.gridLayout_15.addWidget(self.label_73, 0, 0, 1, 1)

        self.toolButton_59 = QToolButton(self.groupBox_7)
        self.toolButton_59.setObjectName(u"toolButton_59")
        self.toolButton_59.setMaximumSize(QSize(30, 30))
        self.toolButton_59.setIcon(icon1)
        self.toolButton_59.setIconSize(QSize(40, 40))
        self.toolButton_59.setCheckable(False)
        self.toolButton_59.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_59.setAutoRaise(False)
        self.toolButton_59.setArrowType(Qt.NoArrow)

        self.gridLayout_15.addWidget(self.toolButton_59, 0, 1, 1, 1)

        self.comboBox_16 = QComboBox(self.groupBox_7)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_15.addWidget(self.comboBox_16, 1, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_15)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setVerticalSpacing(0)
        self.label_74 = QLabel(self.groupBox_7)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font)

        self.gridLayout_16.addWidget(self.label_74, 0, 0, 1, 1)

        self.toolButton_60 = QToolButton(self.groupBox_7)
        self.toolButton_60.setObjectName(u"toolButton_60")
        self.toolButton_60.setMaximumSize(QSize(30, 30))
        self.toolButton_60.setIcon(icon1)
        self.toolButton_60.setIconSize(QSize(40, 40))
        self.toolButton_60.setCheckable(False)
        self.toolButton_60.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_60.setAutoRaise(False)
        self.toolButton_60.setArrowType(Qt.NoArrow)

        self.gridLayout_16.addWidget(self.toolButton_60, 0, 1, 1, 1)

        self.lineEdit_45 = QLineEdit(self.groupBox_7)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setClearButtonEnabled(True)

        self.gridLayout_16.addWidget(self.lineEdit_45, 1, 0, 1, 1)

        self.label_75 = QLabel(self.groupBox_7)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_16.addWidget(self.label_75, 1, 1, 1, 1)

        self.label_88 = QLabel(self.groupBox_7)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setEnabled(False)
        self.label_88.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_16.addWidget(self.label_88, 2, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_16)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setVerticalSpacing(0)
        self.label_76 = QLabel(self.groupBox_7)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font)

        self.gridLayout_17.addWidget(self.label_76, 0, 0, 1, 1)

        self.toolButton_61 = QToolButton(self.groupBox_7)
        self.toolButton_61.setObjectName(u"toolButton_61")
        self.toolButton_61.setMaximumSize(QSize(30, 30))
        self.toolButton_61.setIcon(icon1)
        self.toolButton_61.setIconSize(QSize(40, 40))
        self.toolButton_61.setCheckable(False)
        self.toolButton_61.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_61.setAutoRaise(False)
        self.toolButton_61.setArrowType(Qt.NoArrow)

        self.gridLayout_17.addWidget(self.toolButton_61, 0, 1, 1, 1)

        self.lineEdit_46 = QLineEdit(self.groupBox_7)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setClearButtonEnabled(True)

        self.gridLayout_17.addWidget(self.lineEdit_46, 1, 0, 1, 1)

        self.label_77 = QLabel(self.groupBox_7)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_17.addWidget(self.label_77, 1, 1, 1, 1)

        self.label_87 = QLabel(self.groupBox_7)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setEnabled(False)
        self.label_87.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_17.addWidget(self.label_87, 2, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_17)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setVerticalSpacing(0)
        self.label_78 = QLabel(self.groupBox_7)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font)

        self.gridLayout_18.addWidget(self.label_78, 0, 0, 1, 1)

        self.toolButton_62 = QToolButton(self.groupBox_7)
        self.toolButton_62.setObjectName(u"toolButton_62")
        self.toolButton_62.setMaximumSize(QSize(30, 30))
        self.toolButton_62.setIcon(icon1)
        self.toolButton_62.setIconSize(QSize(40, 40))
        self.toolButton_62.setCheckable(False)
        self.toolButton_62.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_62.setAutoRaise(False)
        self.toolButton_62.setArrowType(Qt.NoArrow)

        self.gridLayout_18.addWidget(self.toolButton_62, 0, 1, 1, 1)

        self.lineEdit_38 = QLineEdit(self.groupBox_7)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setClearButtonEnabled(True)

        self.gridLayout_18.addWidget(self.lineEdit_38, 1, 0, 1, 1)

        self.label_79 = QLabel(self.groupBox_7)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_18.addWidget(self.label_79, 1, 1, 1, 1)

        self.label_62 = QLabel(self.groupBox_7)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setEnabled(False)
        self.label_62.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_18.addWidget(self.label_62, 2, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_18)


        self.gridLayout_28.addLayout(self.verticalLayout_7, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        sizePolicy1.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy1)
        self.tab_3.setMaximumSize(QSize(524, 496))
        self.gridLayout_31 = QGridLayout(self.tab_3)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_31.setContentsMargins(-1, 9, -1, -1)
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.groupBox_4.setMaximumSize(QSize(506, 476))
        self.groupBox_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_53 = QLabel(self.groupBox_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)

        self.gridLayout_7.addWidget(self.label_53, 0, 0, 1, 1)

        self.toolButton_50 = QToolButton(self.groupBox_4)
        self.toolButton_50.setObjectName(u"toolButton_50")
        self.toolButton_50.setMaximumSize(QSize(30, 30))
        self.toolButton_50.setIcon(icon1)
        self.toolButton_50.setIconSize(QSize(40, 40))
        self.toolButton_50.setCheckable(False)
        self.toolButton_50.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_50.setAutoRaise(False)
        self.toolButton_50.setArrowType(Qt.NoArrow)

        self.gridLayout_7.addWidget(self.toolButton_50, 0, 1, 1, 1)

        self.comboBox_8 = QComboBox(self.groupBox_4)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_8.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_7.addWidget(self.comboBox_8, 1, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_7)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(6)
        self.gridLayout_19.setVerticalSpacing(0)
        self.label_54 = QLabel(self.groupBox_4)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.gridLayout_19.addWidget(self.label_54, 0, 0, 1, 1)

        self.toolButton_51 = QToolButton(self.groupBox_4)
        self.toolButton_51.setObjectName(u"toolButton_51")
        self.toolButton_51.setMaximumSize(QSize(30, 30))
        self.toolButton_51.setIcon(icon1)
        self.toolButton_51.setIconSize(QSize(40, 40))
        self.toolButton_51.setCheckable(False)
        self.toolButton_51.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_51.setAutoRaise(False)
        self.toolButton_51.setArrowType(Qt.NoArrow)

        self.gridLayout_19.addWidget(self.toolButton_51, 0, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.groupBox_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setClearButtonEnabled(True)

        self.gridLayout_19.addWidget(self.lineEdit_13, 1, 0, 1, 1)

        self.label_55 = QLabel(self.groupBox_4)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_19.addWidget(self.label_55, 1, 1, 1, 1)

        self.label_96 = QLabel(self.groupBox_4)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setEnabled(False)
        self.label_96.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_19.addWidget(self.label_96, 2, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_19)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setVerticalSpacing(0)
        self.label_56 = QLabel(self.groupBox_4)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)

        self.gridLayout_20.addWidget(self.label_56, 0, 0, 1, 1)

        self.toolButton_52 = QToolButton(self.groupBox_4)
        self.toolButton_52.setObjectName(u"toolButton_52")
        self.toolButton_52.setMaximumSize(QSize(30, 30))
        self.toolButton_52.setIcon(icon1)
        self.toolButton_52.setIconSize(QSize(40, 40))
        self.toolButton_52.setCheckable(False)
        self.toolButton_52.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_52.setAutoRaise(False)
        self.toolButton_52.setArrowType(Qt.NoArrow)

        self.gridLayout_20.addWidget(self.toolButton_52, 0, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setClearButtonEnabled(True)

        self.gridLayout_20.addWidget(self.lineEdit_14, 1, 0, 1, 1)

        self.label_57 = QLabel(self.groupBox_4)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_20.addWidget(self.label_57, 1, 1, 1, 1)

        self.label_95 = QLabel(self.groupBox_4)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setEnabled(False)
        self.label_95.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_20.addWidget(self.label_95, 2, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_20)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(6)
        self.gridLayout_21.setVerticalSpacing(0)
        self.label_58 = QLabel(self.groupBox_4)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font)

        self.gridLayout_21.addWidget(self.label_58, 0, 0, 1, 1)

        self.toolButton_53 = QToolButton(self.groupBox_4)
        self.toolButton_53.setObjectName(u"toolButton_53")
        self.toolButton_53.setMaximumSize(QSize(30, 30))
        self.toolButton_53.setIcon(icon1)
        self.toolButton_53.setIconSize(QSize(40, 40))
        self.toolButton_53.setCheckable(False)
        self.toolButton_53.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_53.setAutoRaise(False)
        self.toolButton_53.setArrowType(Qt.NoArrow)

        self.gridLayout_21.addWidget(self.toolButton_53, 0, 1, 1, 1)

        self.lineEdit_24 = QLineEdit(self.groupBox_4)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setClearButtonEnabled(True)

        self.gridLayout_21.addWidget(self.lineEdit_24, 1, 0, 1, 1)

        self.label_59 = QLabel(self.groupBox_4)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_21.addWidget(self.label_59, 1, 1, 1, 1)

        self.label_94 = QLabel(self.groupBox_4)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setEnabled(False)
        self.label_94.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_21.addWidget(self.label_94, 2, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_21)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setVerticalSpacing(0)
        self.label_63 = QLabel(self.groupBox_4)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font)

        self.gridLayout_22.addWidget(self.label_63, 0, 0, 1, 1)

        self.toolButton_54 = QToolButton(self.groupBox_4)
        self.toolButton_54.setObjectName(u"toolButton_54")
        self.toolButton_54.setMaximumSize(QSize(30, 30))
        self.toolButton_54.setIcon(icon1)
        self.toolButton_54.setIconSize(QSize(40, 40))
        self.toolButton_54.setCheckable(False)
        self.toolButton_54.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_54.setAutoRaise(False)
        self.toolButton_54.setArrowType(Qt.NoArrow)

        self.gridLayout_22.addWidget(self.toolButton_54, 0, 1, 1, 1)

        self.lineEdit_25 = QLineEdit(self.groupBox_4)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setClearButtonEnabled(True)

        self.gridLayout_22.addWidget(self.lineEdit_25, 1, 0, 1, 1)

        self.label_64 = QLabel(self.groupBox_4)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_22.addWidget(self.label_64, 1, 1, 1, 1)

        self.label_93 = QLabel(self.groupBox_4)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setEnabled(False)
        self.label_93.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_22.addWidget(self.label_93, 2, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_22)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setVerticalSpacing(0)
        self.label_65 = QLabel(self.groupBox_4)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font)

        self.gridLayout_23.addWidget(self.label_65, 0, 0, 1, 1)

        self.toolButton_55 = QToolButton(self.groupBox_4)
        self.toolButton_55.setObjectName(u"toolButton_55")
        self.toolButton_55.setMaximumSize(QSize(30, 30))
        self.toolButton_55.setIcon(icon1)
        self.toolButton_55.setIconSize(QSize(40, 40))
        self.toolButton_55.setCheckable(False)
        self.toolButton_55.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_55.setAutoRaise(False)
        self.toolButton_55.setArrowType(Qt.NoArrow)

        self.gridLayout_23.addWidget(self.toolButton_55, 0, 1, 1, 1)

        self.lineEdit_26 = QLineEdit(self.groupBox_4)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setClearButtonEnabled(True)

        self.gridLayout_23.addWidget(self.lineEdit_26, 1, 0, 1, 1)

        self.label_66 = QLabel(self.groupBox_4)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_23.addWidget(self.label_66, 1, 1, 1, 1)

        self.label_92 = QLabel(self.groupBox_4)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setEnabled(False)
        self.label_92.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_23.addWidget(self.label_92, 2, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_23)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setVerticalSpacing(0)
        self.label_67 = QLabel(self.groupBox_4)
        self.label_67.setObjectName(u"label_67")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        self.label_67.setFont(font1)

        self.gridLayout_26.addWidget(self.label_67, 0, 0, 1, 1)

        self.toolButton_56 = QToolButton(self.groupBox_4)
        self.toolButton_56.setObjectName(u"toolButton_56")
        self.toolButton_56.setMaximumSize(QSize(30, 30))
        self.toolButton_56.setIcon(icon1)
        self.toolButton_56.setIconSize(QSize(40, 40))
        self.toolButton_56.setCheckable(False)
        self.toolButton_56.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_56.setAutoRaise(False)
        self.toolButton_56.setArrowType(Qt.NoArrow)

        self.gridLayout_26.addWidget(self.toolButton_56, 0, 1, 1, 1)

        self.lineEdit_29 = QLineEdit(self.groupBox_4)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setClearButtonEnabled(True)

        self.gridLayout_26.addWidget(self.lineEdit_29, 1, 0, 1, 1)

        self.label_68 = QLabel(self.groupBox_4)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_26.addWidget(self.label_68, 1, 1, 1, 1)

        self.label_91 = QLabel(self.groupBox_4)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setEnabled(False)
        self.label_91.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_26.addWidget(self.label_91, 2, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_26)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setVerticalSpacing(0)
        self.label_69 = QLabel(self.groupBox_4)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font)

        self.gridLayout_25.addWidget(self.label_69, 0, 0, 1, 1)

        self.toolButton_57 = QToolButton(self.groupBox_4)
        self.toolButton_57.setObjectName(u"toolButton_57")
        self.toolButton_57.setMaximumSize(QSize(30, 30))
        self.toolButton_57.setIcon(icon1)
        self.toolButton_57.setIconSize(QSize(40, 40))
        self.toolButton_57.setCheckable(False)
        self.toolButton_57.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_57.setAutoRaise(False)
        self.toolButton_57.setArrowType(Qt.NoArrow)

        self.gridLayout_25.addWidget(self.toolButton_57, 0, 1, 1, 1)

        self.lineEdit_30 = QLineEdit(self.groupBox_4)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setClearButtonEnabled(True)

        self.gridLayout_25.addWidget(self.lineEdit_30, 1, 0, 1, 1)

        self.label_70 = QLabel(self.groupBox_4)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_25.addWidget(self.label_70, 1, 1, 1, 1)

        self.label_90 = QLabel(self.groupBox_4)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setEnabled(False)
        self.label_90.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_25.addWidget(self.label_90, 2, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_25)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setVerticalSpacing(0)
        self.label_71 = QLabel(self.groupBox_4)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font)

        self.gridLayout_24.addWidget(self.label_71, 0, 0, 1, 1)

        self.toolButton_58 = QToolButton(self.groupBox_4)
        self.toolButton_58.setObjectName(u"toolButton_58")
        self.toolButton_58.setMaximumSize(QSize(30, 30))
        self.toolButton_58.setIcon(icon1)
        self.toolButton_58.setIconSize(QSize(40, 40))
        self.toolButton_58.setCheckable(False)
        self.toolButton_58.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_58.setAutoRaise(False)
        self.toolButton_58.setArrowType(Qt.NoArrow)

        self.gridLayout_24.addWidget(self.toolButton_58, 0, 1, 1, 1)

        self.lineEdit_31 = QLineEdit(self.groupBox_4)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setClearButtonEnabled(True)

        self.gridLayout_24.addWidget(self.lineEdit_31, 1, 0, 1, 1)

        self.label_72 = QLabel(self.groupBox_4)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_24.addWidget(self.label_72, 1, 1, 1, 1)

        self.label_89 = QLabel(self.groupBox_4)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setEnabled(False)
        self.label_89.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.gridLayout_24.addWidget(self.label_89, 2, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_24)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.verticalLayout_9)


        self.gridLayout_31.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.evaluateButton = QPushButton(self.centralwidget)
        self.evaluateButton.setObjectName(u"evaluateButton")
        self.evaluateButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.evaluateButton)

        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.resetButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/images/images/auth-logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Sitka"])
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalLayout_2.setStretch(0, 10)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.toolButton_63, self.comboBox_9)
        QWidget.setTabOrder(self.comboBox_9, self.toolButton_64)
        QWidget.setTabOrder(self.toolButton_64, self.lineEdit_32)
        QWidget.setTabOrder(self.lineEdit_32, self.toolButton_65)
        QWidget.setTabOrder(self.toolButton_65, self.lineEdit_33)
        QWidget.setTabOrder(self.lineEdit_33, self.toolButton_66)
        QWidget.setTabOrder(self.toolButton_66, self.lineEdit_34)
        QWidget.setTabOrder(self.lineEdit_34, self.toolButton_43)
        QWidget.setTabOrder(self.toolButton_43, self.comboBox_6)
        QWidget.setTabOrder(self.comboBox_6, self.toolButton_44)
        QWidget.setTabOrder(self.toolButton_44, self.lineEdit_20)
        QWidget.setTabOrder(self.lineEdit_20, self.toolButton_45)
        QWidget.setTabOrder(self.toolButton_45, self.lineEdit_21)
        QWidget.setTabOrder(self.lineEdit_21, self.toolButton_46)
        QWidget.setTabOrder(self.toolButton_46, self.lineEdit_28)
        QWidget.setTabOrder(self.lineEdit_28, self.toolButton_59)
        QWidget.setTabOrder(self.toolButton_59, self.comboBox_16)
        QWidget.setTabOrder(self.comboBox_16, self.toolButton_60)
        QWidget.setTabOrder(self.toolButton_60, self.lineEdit_45)
        QWidget.setTabOrder(self.lineEdit_45, self.toolButton_61)
        QWidget.setTabOrder(self.toolButton_61, self.lineEdit_46)
        QWidget.setTabOrder(self.lineEdit_46, self.toolButton_62)
        QWidget.setTabOrder(self.toolButton_62, self.lineEdit_38)
        QWidget.setTabOrder(self.lineEdit_38, self.toolButton_50)
        QWidget.setTabOrder(self.toolButton_50, self.comboBox_8)
        QWidget.setTabOrder(self.comboBox_8, self.toolButton_51)
        QWidget.setTabOrder(self.toolButton_51, self.lineEdit_13)
        QWidget.setTabOrder(self.lineEdit_13, self.toolButton_52)
        QWidget.setTabOrder(self.toolButton_52, self.lineEdit_14)
        QWidget.setTabOrder(self.lineEdit_14, self.toolButton_53)
        QWidget.setTabOrder(self.toolButton_53, self.lineEdit_24)
        QWidget.setTabOrder(self.lineEdit_24, self.toolButton_54)
        QWidget.setTabOrder(self.toolButton_54, self.lineEdit_25)
        QWidget.setTabOrder(self.lineEdit_25, self.toolButton_55)
        QWidget.setTabOrder(self.toolButton_55, self.lineEdit_26)
        QWidget.setTabOrder(self.lineEdit_26, self.toolButton_56)
        QWidget.setTabOrder(self.toolButton_56, self.lineEdit_29)
        QWidget.setTabOrder(self.lineEdit_29, self.toolButton_57)
        QWidget.setTabOrder(self.toolButton_57, self.lineEdit_30)
        QWidget.setTabOrder(self.lineEdit_30, self.toolButton_58)
        QWidget.setTabOrder(self.toolButton_58, self.lineEdit_31)
        QWidget.setTabOrder(self.lineEdit_31, self.evaluateButton)
        QWidget.setTabOrder(self.evaluateButton, self.resetButton)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionImport_Parameters)
        self.menuFile.addAction(self.actionExport_Parameters)
        self.menuFile.addAction(self.actionSave_Plot)
        self.menuHelp.addSeparator()
        self.menuView.addAction(self.actionShow_Logs)
        self.menuView.addAction(self.actionShow_Parameters)
        self.menuView.addAction(self.actionShow_Plot)
        self.menuView.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SubStationGuard", None))
        self.actionImport_Parameters.setText(QCoreApplication.translate("MainWindow", u"Import Parameters...", None))
        self.actionExport_Parameters.setText(QCoreApplication.translate("MainWindow", u"Export Parameters...", None))
        self.actionShow_Logs.setText(QCoreApplication.translate("MainWindow", u"Show Logs", None))
        self.actionShow_Parameters.setText(QCoreApplication.translate("MainWindow", u"Show Parameters", None))
        self.actionShow_Plot.setText(QCoreApplication.translate("MainWindow", u"Show Plot", None))
        self.actionSave_Plot.setText(QCoreApplication.translate("MainWindow", u"Save Plot...", None))
        self.plainTextEdit.setPlainText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Execution Logs", None))
        self.groupBox_9.setTitle("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">System Type of MV/LV Substation<span style=\" text-decoration:none;\">                                           </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.toolButton_63.setToolTip(QCoreApplication.translate("MainWindow", u"Type of the Medium Voltage/ Low Voltage Substation", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"TN", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"TT", None))

        self.label_81.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Geometric proportionality factor<span style=\" text-decoration:none;\">                                   </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_32.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'kg', Unit of Measurement: 'm^-1')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_82.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"m^-1", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Surface potential proportionality factor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_33.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'ksp', Function)", None))
#endif // QT_CONFIG(tooltip)
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"function", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Error", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_35.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'ksp', Function)", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" Browse File", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"Data Points CSV File", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"Custom Mathematical Expression", None))

        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Fault Duration", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_34.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'tf', Unit of Measurement: 's')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_86.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Global Settings", None))
        self.groupBox_8.setTitle("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calculate Soil Resistivity through Ground Resistance<span style=\" text-decoration:none;\">     </span></p></body></html>", None))
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
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Soil Resistivity", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_23.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: '\u03c1', Unit of Measurement: '\u03a9m')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_52.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u03a9m", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Soil Resistivity", None))
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
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Fault Current Division Factor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_21.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'Sf', Unit of Measurement: 'p.u,')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_44.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Maximum Grid Current", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_28.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'IG', Unit of Measurement: 'A')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_46.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Calculate Decrement Factor according to IEEE Std 80", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Inductive Reactance", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_45.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'X', Unit of Measurement: '\u03a9')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_75.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"System resistance at fault", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_46.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'R', Unit of Measurement: '\u03a9')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_77.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Decrement Factor", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_38.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'Df', Unit of Measurement: 'p.u.')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_79.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Maximum Grid Current", None))
        self.groupBox_4.setTitle("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Safety Standard", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"IEEE Std 80", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"CENELEC EN 50522", None))

        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resistance of the human body<span style=\" text-decoration:none;\">                                              </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_13.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'Rb', Unit of Measurement: '\u03a9')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_55.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Factor related to tolerable electric shock energy<span style=\" text-decoration:none;\">                   </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_14.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'k', Unit of Measurement: 'A\u221as')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_57.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"A\u221as", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Body current limit<span style=\" text-decoration:none;\">                                                                           </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_24.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'IB', Unit of Measurement: 'A')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_59.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Body impedance<span style=\" text-decoration:none;\">                                                                            </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_25.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'ZT', Unit of Measurement: '\u03a9')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_64.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Heart current factor<span style=\" text-decoration:none;\">                                                                      </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_26.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'HF', Unit of Measurement: 'p.u.')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_66.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Body factor</span>                                                                                       </p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_29.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'BF', Unit of Measurement: 'p.u.')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_68.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Constant F<span style=\" text-decoration:none;\">                                                                                         </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_30.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'F', Unit of Measurement: 'p.u.')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_70.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"p.u.", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal; text-decoration: underline;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Voltage limit<span style=\" text-decoration:none;\">                                                                                     </span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_31.setToolTip(QCoreApplication.translate("MainWindow", u"(Variable: 'Vlim', Unit of Measurement: 'V')", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_72.setToolTip(QCoreApplication.translate("MainWindow", u"Unit of Measurement", None))
#endif // QT_CONFIG(tooltip)
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Safety Standard Constants", None))
        self.evaluateButton.setText(QCoreApplication.translate("MainWindow", u"Evaluate", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_3.setText("")
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Aristotle University of Thessaloniki. All rights reserved.", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

