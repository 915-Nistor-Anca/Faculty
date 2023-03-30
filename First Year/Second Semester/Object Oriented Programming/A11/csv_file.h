#pragma once
#include "adoption_list.h"
#include <string>
//using namespace std;

class CSVFile : public AdoptionList {
private:
    std::string text_file;
public:
    CSVFile(const std::string& file_name);
    ~CSVFile();
    CSVFile(const CSVFile& txt);
    void add_dog(const Dog& d) override;
    void delete_dog(const std::string& name) override;
    void save_file() override;
    std::string get_file_name() override;
};