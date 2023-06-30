/********************************************************************************
** Form generated from reading UI file 'couriercompany.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_COURIERCOMPANY_H
#define UI_COURIERCOMPANY_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_couriercompanyClass
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QListWidget *listWidget;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QLineEdit *lineEdit_3;
    QPushButton *pushButton;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *couriercompanyClass)
    {
        if (couriercompanyClass->objectName().isEmpty())
            couriercompanyClass->setObjectName(QString::fromUtf8("couriercompanyClass"));
        couriercompanyClass->resize(600, 400);
        centralWidget = new QWidget(couriercompanyClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        listWidget = new QListWidget(centralWidget);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));

        verticalLayout->addWidget(listWidget);

        lineEdit = new QLineEdit(centralWidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        verticalLayout->addWidget(lineEdit);

        lineEdit_2 = new QLineEdit(centralWidget);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        verticalLayout->addWidget(lineEdit_2);

        lineEdit_3 = new QLineEdit(centralWidget);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));

        verticalLayout->addWidget(lineEdit_3);

        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        verticalLayout->addWidget(pushButton);

        couriercompanyClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(couriercompanyClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 600, 22));
        couriercompanyClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(couriercompanyClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        couriercompanyClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(couriercompanyClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        couriercompanyClass->setStatusBar(statusBar);

        retranslateUi(couriercompanyClass);

        QMetaObject::connectSlotsByName(couriercompanyClass);
    } // setupUi

    void retranslateUi(QMainWindow *couriercompanyClass)
    {
        couriercompanyClass->setWindowTitle(QCoreApplication::translate("couriercompanyClass", "couriercompany", nullptr));
        pushButton->setText(QCoreApplication::translate("couriercompanyClass", "Add package", nullptr));
    } // retranslateUi

};

namespace Ui {
    class couriercompanyClass: public Ui_couriercompanyClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_COURIERCOMPANY_H
