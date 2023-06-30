#pragma once

#include <QMainWindow>
#include "ui_couriercompany.h"
#include "service.h"

class couriercompany : public QMainWindow, public observer
{
	Q_OBJECT

public:
	couriercompany(service& s, QWidget *parent = nullptr);
	~couriercompany();
	void showPackages();
	void addPackage();
	void connectSignalsAndSlots();
	void update() override;

private:
	Ui::couriercompanyClass ui;
	service& s;

};
