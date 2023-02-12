package repository;

import model.IVegetable;

public interface IRepository {
    public void add(IVegetable vegetable);
    public void delete(int index);
    public IVegetable[] getAll();
}
