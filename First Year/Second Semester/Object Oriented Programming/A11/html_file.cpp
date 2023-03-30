#include "html_file.h"
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

HtmlFile::HtmlFile(const std::string& file_name) {
    this->text_file = file_name;
    this->save_file();
}

HtmlFile::~HtmlFile() {

}

HtmlFile::HtmlFile(const HtmlFile& txt) {
    this->text_file = txt.text_file;
}

void HtmlFile::add_dog(const Dog& d)
{
    AdoptionList::add_dog(d);
    this->save_file();
}

void HtmlFile::delete_dog(const string& name)
{
    AdoptionList::delete_dog(name);
    this->save_file();
}

void HtmlFile::save_file()
{
    std::ofstream file;
    file.open(this->text_file);
    file << "<!DOCTYPE html>\n";
    file << "<html>\n";
    file << "<head>\n";
    file << "\t<title>Adoption list</title>\n";
    file << "</head>\n";
    file << "<body>\n";
    file << "<table border=\"1\">\n";
    file << "\t<tr>\n";
    file << "\t\t<td>Breed</td>\n";
    file << "\t\t<td>Name</td>\n";
    file << "\t\t<td>Age</td>\n";
    file << "\t\t<td>Photograph</td>\n";
    file << "\t</tr>\n";


    /*file << "\t<tr>\n";
    file << "\t\t<td>" << "x" << "</td>\n";
    file << "\t\t<td>" << "fs" << "</td>\n";
    file << "\t\t<td>" << "42" << "</td>\n";
    file << "\t\t<td><a href=\"" << "fs" << "\">Link</a></td>\n";
    file << "\t</tr>\n";*/

    for (auto& dog : dogs) {
        file << "\t<tr>\n";
        file << "\t\t<td>" << dog.get_breed() << "</td>\n";
        file << "\t\t<td>" << dog.get_name() << "</td>\n";
        file << "\t\t<td>" << dog.get_age() << "</td>\n";
        file << "\t\t<td><a href=\"" << dog.get_photograph() << "\">Link</a></td>\n";
        file << "\t</tr>\n";
    }
    file << "</table>\n";
    file << "</body>\n";
    file << "</html>";
    file.close();
}

string HtmlFile::get_file_name()
{
    return this->text_file;
}
