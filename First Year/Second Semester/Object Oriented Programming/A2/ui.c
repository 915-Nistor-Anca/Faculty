#include "ui.h"
#include "service.h"
#include "repository.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

UI* create_ui(Service* s)
{
    UI* ui = (UI*) malloc(sizeof(UI));
    ui->s = s;
    return ui;
}

void destroy_ui(UI* ui)
{
    destroy_service(ui->s);
    free(ui);
}

void readStringWithSpaces(const char* message, int maxStrSize, char str[])
{
    printf(message);
    fgets(str, maxStrSize, stdin);
    size_t size = strlen(str) - 1;
    if (str[size] == '\n')
        str[size] = '\0';
}

int add_material_ui(UI* ui)
{
    char name[50], supplier[50], expiration_date[50];
    int quantity;
    fgetc(stdin);
    readStringWithSpaces("Input the name: ", 50, name);
    readStringWithSpaces("Input the supplier: ", 50, supplier);
    readStringWithSpaces("Input the expiration date: ", 50, expiration_date);
    printf("Input the quantity: ");
    scanf("%d", &quantity);
    return add_material_service(ui->s, name, supplier, quantity, expiration_date);

}

int update_material_ui(UI* ui)
{
    char name[50], supplier[50], expiration_date[50];
    int quantity;
    fgetc(stdin);
    readStringWithSpaces("Enter the old name of the material: ", 50, name);
    readStringWithSpaces("Enter the old supplier: ", 50, supplier);
    readStringWithSpaces("Enter the old expiration_date: ", 50, expiration_date);
    int pos = find_by_name_supplier_exp_date_service(ui->s, name, supplier, expiration_date);
    if (pos == -1) printf("There is no material with such data.\n");
    else
    {
        int res = delete_material_service(ui->s, name, supplier, expiration_date);
        ///fgetc(stdin);
        readStringWithSpaces("Enter the new name of the material: ", 50, name);
        readStringWithSpaces("Enter the new supplier: ", 50, supplier);
        readStringWithSpaces("Enter the new expiration_date: ", 50, supplier);
        printf("Enter the new quantity: ");
        scanf("%d", &quantity);
        return add_material_service(ui->s,name, supplier, quantity, expiration_date);

    }
}

void print_menu()
{
    printf("\n");
    printf("0. Exit application. \n");
    printf("1. Add a material. \n");
    printf("2. Update a material. \n");
    printf("3. Delete a material. \n");
    printf("4. Print all materials. \n");
    printf("5. Print the expired materials, containing a given string. \n");
    printf("6. Display the material from a supplier, in short supply, in ascending order. \n");
    printf("7. Undo. \n");
    printf("8. Redo. \n");
    printf("\n");
}

void print_all_materials(UI* ui)
{
    printf("There are %d materials.\n", get_length(ui->s->repo->elements));
    for (int i = 0; i<  get_length(ui->s->repo->elements); i++)
    {
        printf("name: %s, supplier: %s, quantity: %d, expiration date: %s\n", get_name(get(ui->s->repo->elements, i)), get_supplier(get(ui->s->repo->elements, i)),
               get_quantity(get(ui->s->repo->elements, i)), get_expiration_date(get(ui->s->repo->elements, i)));
    }
}

void start_ui(UI* ui) {
    add_material_service(ui->s, "flour", "profi", 300, "21.03.2022");
    add_material_service(ui->s, "milk", "mega", 250, "18.10.2021");
    add_material_service(ui->s, "eggs", "mega", 170, "12.03.2022");
    add_material_service(ui->s, "vanilla", "lidl", 340, "10.09.2022");
    add_material_service(ui->s, "sugar", "mega", 90, "23.02.2023");
    int ok = 1;
    while (ok == 1) {
        print_menu();
        printf("Enter the command: ");
        int command = 0;
        scanf("%d", &command);
        if (command == 1 || command == 2 || command == 3) {
            destroy_operation_stack(ui->s->redo_stack);
            ui->s->redo_stack = create_operation_stack();
        }
        if (command == 0) ok = 0;
        else if (command == 1) {
            int result = add_material_ui(ui);
            if (result == 1) printf("Material added.\n");
            else if (result == 0) printf("The material was not added.\n");
            else if (result == 2) printf("Material already added. The quantity is added to the existent one.\n");
        } else if (command == 4) print_all_materials(ui);
        else if (command == 3) {
            char name[50], supplier[50], expiration_date[50];
            fgetc(stdin);
            readStringWithSpaces("Enter the name of the material: ", 50, name);
            readStringWithSpaces("Enter the supplier: ", 50, supplier);
            readStringWithSpaces("Enter the expiration date: ", 50, expiration_date);
            int result = delete_material_service(ui->s, name, supplier, expiration_date);
            if (result == 0) printf("The material was not deleted.\n");
            else printf("Material deleted.\n");
        } else if (command == 2) {
            int result = update_material_ui(ui);
            if (result == 1) printf("Material successfully updated.\n");
            else printf("The material was not updated.\n");
            update(ui->s);
        } else if (command == 5) {
            int day, month, year;
            char given_string[50];
            printf("What day is it today? Enter: ");
            scanf("%d", &day);
            printf("What month is it? Enter: ");
            scanf("%d", &month);
            printf("What year is it? Enter: ");
            scanf("%d", &year);
            fgetc(stdin);
            readStringWithSpaces("What string should the material contain? Enter: ", 50, given_string);
            Repository *repo = get_repository(ui->s);
            int k = 0;
            for (int i = 0; i < get_length(ui->s->repo->elements); i++) {
                Material *m = get(repo->elements, i);
                if (is_the_material_expired(m->expiration_date, day, month, year) == 1
                    && strstr(get_name(m), given_string) != NULL) {
                    printf("name: %s, supplier: %s, quantity: %d, expiration date: %s\n",
                           get_name(get(ui->s->repo->elements, i)), get_supplier(get(ui->s->repo->elements, i)),
                           get_quantity(get(ui->s->repo->elements, i)),
                           get_expiration_date(get(ui->s->repo->elements, i)));
                    k++;
                }
            }
            printf("There are %d materials which satisfy the conditions.\n", k);
        } else if (command == 6) {
            printf("Enter the quantity: ");
            int quantity;
            scanf("%d", &quantity);
            char supplier_name[50];
            fgetc(stdin);
            readStringWithSpaces("Enter the supplier's name: ", 50, supplier_name);
            int positions[100], k = 0;
            Repository *repo = get_repository(ui->s);
            for (int i = 0; i < get_length(ui->s->repo->elements); i++) {
                Material *m = get(repo->elements, i);
                if (get_quantity(m) < quantity && strcmp(get_supplier(m), supplier_name) == 0) {
                    positions[k] = i;
                    k++;
                }}
                sort_positions(ui->s, positions, k);
                for (int i = 0; i < k; i++) {
                    printf("name: %s, supplier: %s, quantity: %d, expiration date: %s",
                           get_name(get(ui->s->repo->elements, positions[i])),
                           get_supplier(get(ui->s->repo->elements, positions[i])),
                           get_quantity(get(ui->s->repo->elements, positions[i])),
                           get_expiration_date(get(ui->s->repo->elements, positions[i])));
                    printf("\n");
                }
            }
        else if (command == 7)
        {
            undo(ui->s);
        }
        else if (command == 8)
        {
            redo(ui->s);
        }
        }
    }
