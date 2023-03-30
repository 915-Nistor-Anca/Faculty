#pragma once
#include "adoption_list.h"
//using namespace std;

class HtmlFile : public AdoptionList {
private:
    std::string text_file;
public:
    HtmlFile(const std::string& file_name);
    ~HtmlFile();
    HtmlFile(const HtmlFile& txt);
    void add_dog(const Dog& d) override;
    void delete_dog(const std::string& name) override;
    void save_file() override;
    std::string get_file_name() override;
};