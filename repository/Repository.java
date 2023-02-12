package repository;

import model.IVegetable;

public class Repository implements IRepository {
    private IVegetable[] vegetables;
    private int size;

    public Repository(int maxsize){
        this.vegetables = new IVegetable[maxsize];
        this.size = 0;
    }

    public void add(IVegetable vegetable){
        try {
            this.vegetables[this.size] = vegetable;
            this.size++;
        } catch (Exception e){
            System.out.println(e.toString());
        }
    }

    public void delete(int index){
        IVegetable[] new_list = new IVegetable[this.size];
        int i = 0, n = 0;
        for (IVegetable v: this.vegetables)
        {
            if (i > this.size) break;
            if (i != index){
                new_list[n] = v;
                n++;
            }
            i++;
        }
        this.vegetables = new_list;
        this.size = n - 1;
    }

    public IVegetable[] getAll() {return this.vegetables;}
}
