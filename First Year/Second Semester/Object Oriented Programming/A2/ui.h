#pragma once
#include "service.h"

typedef struct
{
    Service* s;
}UI;

UI* create_ui(Service* s);
void destroy_ui(UI* ui);
void start_ui(UI* ui);