#include "couriercompany.h"

couriercompany::couriercompany(service& s,QWidget *parent)
	: QMainWindow(parent), s(s)
{
	ui.setupUi(this);
	this->setWindowTitle("DeliverNow");
	showPackages();
	s.addObserver(this);
	connectSignalsAndSlots();
}

couriercompany::~couriercompany()
{}

void couriercompany::showPackages()
{
	this->ui.listWidget->clear();
	for (package p : s.getPackages()) {

		QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(p.getRecipient() + '|' + p.getAddress() + '|' + p.getLocation() + '|' + to_string(p.getDeliveryStatus())));
		if (p.getDeliveryStatus() == 1) item->setBackground(QBrush(Qt::green));
		this->ui.listWidget->addItem(item);
	}
}

void couriercompany::addPackage()
{
	string recipient = this->ui.lineEdit->text().toStdString();
	string address = this->ui.lineEdit_2->text().toStdString();
	string location = this->ui.lineEdit_3->text().toStdString();

	package p(recipient, address, location, 0);
	s.addPackage(p);
	showPackages();
}

void couriercompany::connectSignalsAndSlots()
{
	QObject::connect(this->ui.pushButton, &QPushButton::clicked, this, &couriercompany::addPackage);
}

void couriercompany::update()
{
	showPackages();
}
