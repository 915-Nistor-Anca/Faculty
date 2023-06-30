/********************************************************************************
** Form generated from reading UI file 'PracticalExam.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PRACTICALEXAM_H
#define UI_PRACTICALEXAM_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_PracticalExamClass
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QListWidget *zonewidget;
    QListWidget *listWidget;
    QPushButton *pushButton;
    QComboBox *comboBox;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *PracticalExamClass)
    {
        if (PracticalExamClass->objectName().isEmpty())
            PracticalExamClass->setObjectName(QString::fromUtf8("PracticalExamClass"));
        PracticalExamClass->resize(493, 400);
        centralWidget = new QWidget(PracticalExamClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        zonewidget = new QListWidget(centralWidget);
        zonewidget->setObjectName(QString::fromUtf8("zonewidget"));

        verticalLayout->addWidget(zonewidget);

        listWidget = new QListWidget(centralWidget);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));

        verticalLayout->addWidget(listWidget);

        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        verticalLayout->addWidget(pushButton);

        comboBox = new QComboBox(centralWidget);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        verticalLayout->addWidget(comboBox);

        PracticalExamClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(PracticalExamClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 493, 22));
        PracticalExamClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(PracticalExamClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        PracticalExamClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(PracticalExamClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        PracticalExamClass->setStatusBar(statusBar);

        retranslateUi(PracticalExamClass);

        QMetaObject::connectSlotsByName(PracticalExamClass);
    } // setupUi

    void retranslateUi(QMainWindow *PracticalExamClass)
    {
        PracticalExamClass->setWindowTitle(QCoreApplication::translate("PracticalExamClass", "PracticalExam", nullptr));
        pushButton->setText(QCoreApplication::translate("PracticalExamClass", "Deliver", nullptr));
    } // retranslateUi

};

namespace Ui {
    class PracticalExamClass: public Ui_PracticalExamClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PRACTICALEXAM_H
