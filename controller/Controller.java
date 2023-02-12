package controller;

import model.IVegetable;
import repository.IRepository;

public class Controller {
    private IRepository repo;
    public Controller(IRepository repo) {this.repo = repo;}
    public void add(IVegetable vegetable) {repo.add(vegetable);}
    public void printAll(float weight){
        IVegetable[] vegetables = this.repo.getAll();
        int i =  0;
        for (IVegetable v: vegetables)
        {
            if (v != null && v.solve(weight))
                System.out.println(i + "." + v.toString());
            i++;
        }
    }

    public void delete(int index){
        this.repo.delete(index);
    }

    public void printMenu(){
        System.out.println("\nChoose an option:");
        System.out.println(
                "0) Exit.\n" +
                "1) Add a vegetable.\n" +
                "2) Delete a vegetable.\n" +
                "3) Display the vegetables which weight more than a given value.\n" +
                "Option:");
    }
}
