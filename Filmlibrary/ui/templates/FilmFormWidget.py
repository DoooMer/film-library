# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Filmlibrary/ui/templates/filmformwidget.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilmForm(object):
    def setupUi(self, FilmForm):
        FilmForm.setObjectName("FilmForm")
        FilmForm.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FilmForm.sizePolicy().hasHeightForWidth())
        FilmForm.setSizePolicy(sizePolicy)
        FilmForm.setMinimumSize(QtCore.QSize(640, 480))
        FilmForm.setMaximumSize(QtCore.QSize(16777215, 480))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FilmForm)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(FilmForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(640, 80))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.buttonSave = QtWidgets.QPushButton(self.frame)
        self.buttonSave.setGeometry(QtCore.QRect(20, 10, 121, 61))
        self.buttonSave.setObjectName("buttonSave")
        self.buttonCancel = QtWidgets.QPushButton(self.frame)
        self.buttonCancel.setGeometry(QtCore.QRect(160, 10, 121, 61))
        self.buttonCancel.setObjectName("buttonCancel")
        self.verticalLayout_2.addWidget(self.frame)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(20, -1, 20, -1)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.diskLabel = QtWidgets.QLabel(FilmForm)
        self.diskLabel.setObjectName("diskLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.diskLabel)
        self.diskInput = QtWidgets.QSpinBox(FilmForm)
        self.diskInput.setMinimum(1)
        self.diskInput.setMaximum(9999)
        self.diskInput.setObjectName("diskInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.diskInput)
        self.titleLabel = QtWidgets.QLabel(FilmForm)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleInput = QtWidgets.QLineEdit(FilmForm)
        self.titleInput.setObjectName("titleInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.titleInput)
        self.yearLabel = QtWidgets.QLabel(FilmForm)
        self.yearLabel.setObjectName("yearLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.yearLabel)
        self.yearInput = QtWidgets.QLineEdit(FilmForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearInput.sizePolicy().hasHeightForWidth())
        self.yearInput.setSizePolicy(sizePolicy)
        self.yearInput.setText("")
        self.yearInput.setCursorPosition(0)
        self.yearInput.setClearButtonEnabled(False)
        self.yearInput.setObjectName("yearInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yearInput)
        self.genreLabel = QtWidgets.QLabel(FilmForm)
        self.genreLabel.setObjectName("genreLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.genreLabel)
        self.genreInput = QtWidgets.QLineEdit(FilmForm)
        self.genreInput.setObjectName("genreInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.genreInput)
        self.directorLabel = QtWidgets.QLabel(FilmForm)
        self.directorLabel.setObjectName("directorLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.directorLabel)
        self.directorInput = QtWidgets.QLineEdit(FilmForm)
        self.directorInput.setObjectName("directorInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.directorInput)
        self.roleLabel = QtWidgets.QLabel(FilmForm)
        self.roleLabel.setObjectName("roleLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.roleLabel)
        self.roleInput = QtWidgets.QLineEdit(FilmForm)
        self.roleInput.setObjectName("roleInput")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.roleInput)
        self.verticalLayout_2.addLayout(self.formLayout)

        self.retranslateUi(FilmForm)
        QtCore.QMetaObject.connectSlotsByName(FilmForm)

    def retranslateUi(self, FilmForm):
        _translate = QtCore.QCoreApplication.translate
        FilmForm.setWindowTitle(_translate("FilmForm", "Form"))
        self.buttonSave.setText(_translate("FilmForm", "Сохранить"))
        self.buttonSave.setShortcut(_translate("FilmForm", "Ctrl+S"))
        self.buttonCancel.setText(_translate("FilmForm", "Отмена"))
        self.buttonCancel.setShortcut(_translate("FilmForm", "Esc"))
        self.diskLabel.setText(_translate("FilmForm", "Номер диска"))
        self.titleLabel.setText(_translate("FilmForm", "Название"))
        self.yearLabel.setText(_translate("FilmForm", "Год выхода"))
        self.yearInput.setInputMask(_translate("FilmForm", "9999"))
        self.genreLabel.setText(_translate("FilmForm", "Жанр"))
        self.directorLabel.setText(_translate("FilmForm", "Режиссер"))
        self.roleLabel.setText(_translate("FilmForm", "В ролях"))

