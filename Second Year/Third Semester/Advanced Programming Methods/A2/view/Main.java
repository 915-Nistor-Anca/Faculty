package view;

import controller.Controller;
import model.*;
import repository.IRepository;
import repository.Repository;

public class Main {
    public static void main(String[] args) {
        IStmt ex1 = ;
        MyIStack<IStmt> stack1 = new MyStack<>();
        MyIDictionary<String, Value> symTable1 = new MyDictionary<>();
        MyIList<Value> out1 = new MyList<>();
        PrgState prgState1 = new PrgState(stack1, symTable1, out1, ex1);
        IRepository repo = new Repository(prgState1);
        Controller ctrl = new Controller(repo);
        ctrl.allStep();
    }
}