#include "csv_file.h"
#include <iostream>
#include <fstream>

CSVFile::CSVFile(const std::string& text_file) {
    this->text_file = text_file;
    this->save_file();
}

CSVFile::~CSVFile() {

}


CSVFile::CSVFile(const CSVFile& txt) {
    this->text_file = txt.text_file;
}

void CSVFile::add_dog(const Dog& d)
{
    AdoptionList::add_dog(d);
    this->save_file();
}

void CSVFile::delete_dog(const std::string& name)
{
    AdoptionList::delete_dog(name);
    this->save_file();
}

void CSVFile::save_file()
{
    std::ofstream file;
    file.open(this->text_file);
    for (auto& dog : dogs)
        file << dog.get_breed() << ',' << dog.get_name() << ',' << dog.get_age() << ',' << dog.get_photograph() << std::endl;
    file.close();
}

std::string CSVFile::get_file_name()
{
    return this->text_file;
}
