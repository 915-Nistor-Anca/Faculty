package viewer;

import controller.Controller;
import model.Eggplant;
import model.IVegetable;
import model.Pepper;
import model.Tomato;
import repository.IRepository;
import repository.Repository;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        IVegetable v1 = new Tomato((float) 0.3);
        IVegetable v2 = new Pepper((float) 0.15);
        IVegetable v3 = new Eggplant((float) 0.43);
        IVegetable v4 = new Pepper((float) 0.5);
        IVegetable v5 = new Tomato((float) 0.8);

        IRepository repo = new Repository(15);
        Controller controller = new Controller(repo);

        controller.add(v1);
        controller.add(v2);
        controller.add(v3);
        controller.add(v4);
        controller.add(v5);
        while (true) {
            controller.printMenu();
            Scanner obj = new Scanner(System.in);
            int option = Integer.parseInt(obj.nextLine()) ;
            if (option == 0) break;
            if (option == 1) {
                System.out.println("What is the type of the vegetable? Enter:");
                String vegType = obj.nextLine();
                if (vegType.compareTo("tomato") == 0 || vegType.compareTo("Tomato") == 0) {
                    System.out.println("How much does the tomato weight? Enter:");
                    float w = obj.nextFloat();
                    IVegetable v = new Tomato(w);
                    controller.add(v);
                    System.out.println("Vegetable added!\n");
                    controller.printAll((float) 0.01);
                }
                else if (vegType.compareTo("pepper") == 0 || vegType.compareTo("Pepper") == 0) {
                    System.out.println("How much does the pepper weight? Enter:");
                    float w = obj.nextFloat();
                    IVegetable v = new Pepper(w);
                    controller.add(v);
                    System.out.println("Vegetable added!\n");
                    controller.printAll((float) 0.01);
                }
                else if (vegType.compareTo("eggplant") == 0 || vegType.compareTo("Eggplant") == 0) {
                    System.out.println("How much does the eggplant weight? Enter:");
                    float w = obj.nextFloat();
                    IVegetable v = new Eggplant(w);
                    controller.add(v);
                    System.out.println("Vegetable added!\n");
                    controller.printAll((float) 0.01);
                }
                else {
                    System.out.println("This cannot be added!\n");
                }
            }
            else if (option == 3){
                System.out.println("What is the weight? Enter:");
                float w = obj.nextFloat();
                controller.printAll(w);
            }
            else if (option == 2){
                controller.printAll((float) 0.01);
                System.out.println("\nWhich vegetable would you like to delete? Enter:");
                int i = obj.nextInt();
                controller.delete(i);
                System.out.println("Vegetable deleted!\n");
                controller.printAll((float) 0.01);
            }
        }
    }
}