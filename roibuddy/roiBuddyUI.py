# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roiBuddyUI.ui'
#
# Created: Wed Feb 25 00:40:11 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_ROI_Buddy(object):
    def setupUi(self, ROI_Buddy):
        ROI_Buddy.setObjectName(_fromUtf8("ROI_Buddy"))
        ROI_Buddy.resize(1200, 942)
        self.centralwidget = QtGui.QWidget(ROI_Buddy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lookupTableFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lookupTableFrame.sizePolicy().hasHeightForWidth())
        self.lookupTableFrame.setSizePolicy(sizePolicy)
        self.lookupTableFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lookupTableFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.lookupTableFrame.setObjectName(_fromUtf8("lookupTableFrame"))
        self.gridLayout.addWidget(self.lookupTableFrame, 3, 1, 1, 1)
        self.channelSelectionFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.channelSelectionFrame.sizePolicy().hasHeightForWidth())
        self.channelSelectionFrame.setSizePolicy(sizePolicy)
        self.channelSelectionFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.channelSelectionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.channelSelectionFrame.setObjectName(_fromUtf8("channelSelectionFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.channelSelectionFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.channelSelectionFrame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.plane_index_box = QtGui.QSpinBox(self.channelSelectionFrame)
        self.plane_index_box.setObjectName(_fromUtf8("plane_index_box"))
        self.horizontalLayout.addWidget(self.plane_index_box)
        self.baseImage_label = QtGui.QLabel(self.channelSelectionFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseImage_label.sizePolicy().hasHeightForWidth())
        self.baseImage_label.setSizePolicy(sizePolicy)
        self.baseImage_label.setObjectName(_fromUtf8("baseImage_label"))
        self.horizontalLayout.addWidget(self.baseImage_label)
        self.baseImage_list = QtGui.QComboBox(self.channelSelectionFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseImage_list.sizePolicy().hasHeightForWidth())
        self.baseImage_list.setSizePolicy(sizePolicy)
        self.baseImage_list.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.baseImage_list.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.baseImage_list.setMinimumContentsLength(30)
        self.baseImage_list.setObjectName(_fromUtf8("baseImage_list"))
        self.horizontalLayout.addWidget(self.baseImage_list)
        self.processed_checkbox = QtGui.QCheckBox(self.channelSelectionFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processed_checkbox.sizePolicy().hasHeightForWidth())
        self.processed_checkbox.setSizePolicy(sizePolicy)
        self.processed_checkbox.setObjectName(_fromUtf8("processed_checkbox"))
        self.horizontalLayout.addWidget(self.processed_checkbox)
        self.gridLayout.addWidget(self.channelSelectionFrame, 4, 1, 1, 1)
        self.displayFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayFrame.sizePolicy().hasHeightForWidth())
        self.displayFrame.setSizePolicy(sizePolicy)
        self.displayFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.displayFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.displayFrame.setObjectName(_fromUtf8("displayFrame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.displayFrame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout.addWidget(self.displayFrame, 0, 0, 5, 1)
        self.tSeriesListFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.tSeriesListFrame.sizePolicy().hasHeightForWidth())
        self.tSeriesListFrame.setSizePolicy(sizePolicy)
        self.tSeriesListFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tSeriesListFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.tSeriesListFrame.setObjectName(_fromUtf8("tSeriesListFrame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tSeriesListFrame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tSeries_list = QtGui.QListWidget(self.tSeriesListFrame)
        self.tSeries_list.setObjectName(_fromUtf8("tSeries_list"))
        self.gridLayout_2.addWidget(self.tSeries_list, 1, 0, 1, 3)
        self.roi_set_widget = QtGui.QWidget(self.tSeriesListFrame)
        self.roi_set_widget.setObjectName(_fromUtf8("roi_set_widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.roi_set_widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.roi_set_widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.active_rois_combobox = QtGui.QComboBox(self.roi_set_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.active_rois_combobox.sizePolicy().hasHeightForWidth())
        self.active_rois_combobox.setSizePolicy(sizePolicy)
        self.active_rois_combobox.setObjectName(_fromUtf8("active_rois_combobox"))
        self.horizontalLayout_4.addWidget(self.active_rois_combobox)
        self.new_set_button = QtGui.QPushButton(self.roi_set_widget)
        self.new_set_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.new_set_button.setObjectName(_fromUtf8("new_set_button"))
        self.horizontalLayout_4.addWidget(self.new_set_button)
        self.delete_set_button = QtGui.QPushButton(self.roi_set_widget)
        self.delete_set_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delete_set_button.setObjectName(_fromUtf8("delete_set_button"))
        self.horizontalLayout_4.addWidget(self.delete_set_button)
        self.gridLayout_2.addWidget(self.roi_set_widget, 4, 0, 1, 3)
        self.show_rois_widget = QtGui.QWidget(self.tSeriesListFrame)
        self.show_rois_widget.setObjectName(_fromUtf8("show_rois_widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.show_rois_widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.show_ROIs_checkbox = QtGui.QCheckBox(self.show_rois_widget)
        self.show_ROIs_checkbox.setChecked(True)
        self.show_ROIs_checkbox.setObjectName(_fromUtf8("show_ROIs_checkbox"))
        self.verticalLayout_2.addWidget(self.show_ROIs_checkbox)
        self.show_all_checkbox = QtGui.QCheckBox(self.show_rois_widget)
        self.show_all_checkbox.setEnabled(False)
        self.show_all_checkbox.setCheckable(True)
        self.show_all_checkbox.setTristate(False)
        self.show_all_checkbox.setObjectName(_fromUtf8("show_all_checkbox"))
        self.verticalLayout_2.addWidget(self.show_all_checkbox)
        self.gridLayout_2.addWidget(self.show_rois_widget, 5, 0, 1, 1)
        self.widget = QtGui.QWidget(self.tSeriesListFrame)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.remove_tseries_button = QtGui.QPushButton(self.widget)
        self.remove_tseries_button.setObjectName(_fromUtf8("remove_tseries_button"))
        self.horizontalLayout_2.addWidget(self.remove_tseries_button, QtCore.Qt.AlignLeft)
        self.add_tseries_button = QtGui.QPushButton(self.widget)
        self.add_tseries_button.setObjectName(_fromUtf8("add_tseries_button"))
        self.horizontalLayout_2.addWidget(self.add_tseries_button, QtCore.Qt.AlignRight)
        self.gridLayout_2.addWidget(self.widget, 2, 2, 1, 1)
        self.save_rois_widget = QtGui.QWidget(self.tSeriesListFrame)
        self.save_rois_widget.setObjectName(_fromUtf8("save_rois_widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.save_rois_widget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.import_rois_button = QtGui.QPushButton(self.save_rois_widget)
        self.import_rois_button.setObjectName(_fromUtf8("import_rois_button"))
        self.verticalLayout_3.addWidget(self.import_rois_button)
        self.save_current_rois_button = QtGui.QPushButton(self.save_rois_widget)
        self.save_current_rois_button.setObjectName(_fromUtf8("save_current_rois_button"))
        self.verticalLayout_3.addWidget(self.save_current_rois_button)
        self.gridLayout_2.addWidget(self.save_rois_widget, 5, 2, 1, 1)
        self.mode_selection_widget = QtGui.QWidget(self.tSeriesListFrame)
        self.mode_selection_widget.setObjectName(_fromUtf8("mode_selection_widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.mode_selection_widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.edit_mode_radiobutton = QtGui.QRadioButton(self.mode_selection_widget)
        self.edit_mode_radiobutton.setChecked(True)
        self.edit_mode_radiobutton.setObjectName(_fromUtf8("edit_mode_radiobutton"))
        self.modeSelection = QtGui.QButtonGroup(ROI_Buddy)
        self.modeSelection.setObjectName(_fromUtf8("modeSelection"))
        self.modeSelection.addButton(self.edit_mode_radiobutton)
        self.horizontalLayout_3.addWidget(self.edit_mode_radiobutton, QtCore.Qt.AlignLeft)
        self.align_mode_radiobutton = QtGui.QRadioButton(self.mode_selection_widget)
        self.align_mode_radiobutton.setObjectName(_fromUtf8("align_mode_radiobutton"))
        self.modeSelection.addButton(self.align_mode_radiobutton)
        self.horizontalLayout_3.addWidget(self.align_mode_radiobutton, QtCore.Qt.AlignHCenter)
        self.register_rois_button = QtGui.QPushButton(self.mode_selection_widget)
        self.register_rois_button.setEnabled(False)
        self.register_rois_button.setCheckable(False)
        self.register_rois_button.setObjectName(_fromUtf8("register_rois_button"))
        self.horizontalLayout_3.addWidget(self.register_rois_button, QtCore.Qt.AlignRight)
        self.propagate_tags_button = QtGui.QPushButton(self.mode_selection_widget)
        self.propagate_tags_button.setEnabled(False)
        self.propagate_tags_button.setObjectName(_fromUtf8("propagate_tags_button"))
        self.horizontalLayout_3.addWidget(self.propagate_tags_button)
        self.gridLayout_2.addWidget(self.mode_selection_widget, 0, 0, 1, 3)
        self.line = QtGui.QFrame(self.tSeriesListFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 3)
        self.widget_2 = QtGui.QWidget(self.tSeriesListFrame)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.colorbyid_radioButton = QtGui.QRadioButton(self.widget_2)
        self.colorbyid_radioButton.setObjectName(_fromUtf8("colorbyid_radioButton"))
        self.colorbyMode = QtGui.QButtonGroup(ROI_Buddy)
        self.colorbyMode.setObjectName(_fromUtf8("colorbyMode"))
        self.colorbyMode.addButton(self.colorbyid_radioButton)
        self.verticalLayout.addWidget(self.colorbyid_radioButton)
        self.colorbytags_radioButton = QtGui.QRadioButton(self.widget_2)
        self.colorbytags_radioButton.setObjectName(_fromUtf8("colorbytags_radioButton"))
        self.colorbyMode.addButton(self.colorbytags_radioButton)
        self.verticalLayout.addWidget(self.colorbytags_radioButton)
        self.gridLayout_2.addWidget(self.widget_2, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.tSeriesListFrame, 0, 1, 1, 1)
        self.itemListFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.itemListFrame.sizePolicy().hasHeightForWidth())
        self.itemListFrame.setSizePolicy(sizePolicy)
        self.itemListFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.itemListFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.itemListFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.itemListFrame.setObjectName(_fromUtf8("itemListFrame"))
        self.gridLayout.addWidget(self.itemListFrame, 1, 1, 2, 1)
        ROI_Buddy.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ROI_Buddy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ROI_Buddy.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ROI_Buddy)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ROI_Buddy.setStatusBar(self.statusbar)

        self.retranslateUi(ROI_Buddy)
        QtCore.QMetaObject.connectSlotsByName(ROI_Buddy)

    def retranslateUi(self, ROI_Buddy):
        ROI_Buddy.setWindowTitle(_translate("ROI_Buddy", "MainWindow", None))
        self.label_2.setText(_translate("ROI_Buddy", "Plane:", None))
        self.baseImage_label.setText(_translate("ROI_Buddy", "Base Image:", None))
        self.processed_checkbox.setText(_translate("ROI_Buddy", "Processed", None))
        self.label.setText(_translate("ROI_Buddy", "ROI List:", None))
        self.new_set_button.setText(_translate("ROI_Buddy", "New Set", None))
        self.delete_set_button.setText(_translate("ROI_Buddy", "Delete Set", None))
        self.show_ROIs_checkbox.setText(_translate("ROI_Buddy", "show ROIs", None))
        self.show_all_checkbox.setText(_translate("ROI_Buddy", "show all", None))
        self.remove_tseries_button.setText(_translate("ROI_Buddy", "remove", None))
        self.add_tseries_button.setText(_translate("ROI_Buddy", "add ", None))
        self.import_rois_button.setText(_translate("ROI_Buddy", "import ROIs", None))
        self.save_current_rois_button.setText(_translate("ROI_Buddy", "save current ROIs", None))
        self.edit_mode_radiobutton.setText(_translate("ROI_Buddy", "Edit Mode", None))
        self.align_mode_radiobutton.setText(_translate("ROI_Buddy", "Align Mode", None))
        self.register_rois_button.setText(_translate("ROI_Buddy", "Register ROIs", None))
        self.propagate_tags_button.setText(_translate("ROI_Buddy", "Propagate Tags", None))
        self.colorbyid_radioButton.setText(_translate("ROI_Buddy", "color by ID", None))
        self.colorbytags_radioButton.setText(_translate("ROI_Buddy", "color by tags", None))

