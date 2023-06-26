/********************************************************************************
** Form generated from reading UI file 'Screenwriting.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SCREENWRITING_H
#define UI_SCREENWRITING_H

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

class Ui_ScreenwritingClass
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout_3;
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout;
    QListWidget *listWidget;
    QPushButton *pushButton_2;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton;
    QPushButton *pushButton_3;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *ScreenwritingClass)
    {
        if (ScreenwritingClass->objectName().isEmpty())
            ScreenwritingClass->setObjectName(QString::fromUtf8("ScreenwritingClass"));
        ScreenwritingClass->resize(600, 400);
        centralWidget = new QWidget(ScreenwritingClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        verticalLayout_3 = new QVBoxLayout(centralWidget);
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setContentsMargins(11, 11, 11, 11);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        listWidget = new QListWidget(centralWidget);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));

        verticalLayout->addWidget(listWidget);

        pushButton_2 = new QPushButton(centralWidget);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        verticalLayout->addWidget(pushButton_2);

        lineEdit = new QLineEdit(centralWidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        verticalLayout->addWidget(lineEdit);

        lineEdit_2 = new QLineEdit(centralWidget);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        verticalLayout->addWidget(lineEdit_2);

        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        verticalLayout->addWidget(pushButton);


        verticalLayout_2->addLayout(verticalLayout);


        verticalLayout_3->addLayout(verticalLayout_2);

        pushButton_3 = new QPushButton(centralWidget);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));

        verticalLayout_3->addWidget(pushButton_3);

        ScreenwritingClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(ScreenwritingClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 600, 22));
        ScreenwritingClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(ScreenwritingClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        ScreenwritingClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(ScreenwritingClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        ScreenwritingClass->setStatusBar(statusBar);

        retranslateUi(ScreenwritingClass);

        QMetaObject::connectSlotsByName(ScreenwritingClass);
    } // setupUi

    void retranslateUi(QMainWindow *ScreenwritingClass)
    {
        ScreenwritingClass->setWindowTitle(QCoreApplication::translate("ScreenwritingClass", "Screenwriting", nullptr));
        pushButton_2->setText(QCoreApplication::translate("ScreenwritingClass", "Accept", nullptr));
        pushButton->setText(QCoreApplication::translate("ScreenwritingClass", "Add idea", nullptr));
        pushButton_3->setText(QCoreApplication::translate("ScreenwritingClass", "Develop", nullptr));
    } // retranslateUi

};

namespace Ui {
    class ScreenwritingClass: public Ui_ScreenwritingClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SCREENWRITING_H
