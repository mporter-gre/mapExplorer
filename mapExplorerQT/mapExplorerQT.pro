#-------------------------------------------------
#
# Project created by QtCreator 2016-11-23T18:57:14
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = mapExplorerQT
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    connectiondlg.cpp

HEADERS  += mainwindow.h \
    connectiondlg.h

FORMS    += mainwindow.ui \
    connectiondlg.ui
