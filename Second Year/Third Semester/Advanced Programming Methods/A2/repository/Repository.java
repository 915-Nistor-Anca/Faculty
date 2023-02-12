package repository;

import model.IStmt;
import model.PrgState;

import java.util.LinkedList;
import java.util.List;

public class Repository implements IRepository{
    private List<PrgState> repo;
    public Repository(PrgState state){
        repo = new LinkedList<>();
        repo.add(state);
    }
    public PrgState getCurrentState(){
        return repo.get(0);
    }
}
