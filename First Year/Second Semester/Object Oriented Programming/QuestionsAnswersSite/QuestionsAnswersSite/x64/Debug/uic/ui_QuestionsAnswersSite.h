/********************************************************************************
** Form generated from reading UI file 'QuestionsAnswersSite.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QUESTIONSANSWERSSITE_H
#define UI_QUESTIONSANSWERSSITE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_QuestionsAnswersSiteClass
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QLineEdit *lineEdit;
    QVBoxLayout *verticalLayout;
    QListWidget *listWidget;
    QListWidget *listWidget_2;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *QuestionsAnswersSiteClass)
    {
        if (QuestionsAnswersSiteClass->objectName().isEmpty())
            QuestionsAnswersSiteClass->setObjectName(QString::fromUtf8("QuestionsAnswersSiteClass"));
        QuestionsAnswersSiteClass->resize(684, 422);
        centralWidget = new QWidget(QuestionsAnswersSiteClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        lineEdit = new QLineEdit(centralWidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        gridLayout->addWidget(lineEdit, 0, 0, 1, 1);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        listWidget = new QListWidget(centralWidget);
        listWidget->setObjectName(QString::fromUtf8("listWidget"));

        verticalLayout->addWidget(listWidget);

        listWidget_2 = new QListWidget(centralWidget);
        listWidget_2->setObjectName(QString::fromUtf8("listWidget_2"));

        verticalLayout->addWidget(listWidget_2);


        gridLayout->addLayout(verticalLayout, 0, 1, 1, 1);

        QuestionsAnswersSiteClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(QuestionsAnswersSiteClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 684, 22));
        QuestionsAnswersSiteClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(QuestionsAnswersSiteClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        QuestionsAnswersSiteClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(QuestionsAnswersSiteClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        QuestionsAnswersSiteClass->setStatusBar(statusBar);

        retranslateUi(QuestionsAnswersSiteClass);

        QMetaObject::connectSlotsByName(QuestionsAnswersSiteClass);
    } // setupUi

    void retranslateUi(QMainWindow *QuestionsAnswersSiteClass)
    {
        QuestionsAnswersSiteClass->setWindowTitle(QCoreApplication::translate("QuestionsAnswersSiteClass", "QuestionsAnswersSite", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QuestionsAnswersSiteClass: public Ui_QuestionsAnswersSiteClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QUESTIONSANSWERSSITE_H
