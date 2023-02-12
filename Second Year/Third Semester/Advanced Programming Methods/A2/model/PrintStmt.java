package model;

import exception.MyException;

public class PrintStmt implements IStmt{
    Exp exp;
    public PrintStmt(Exp e){
        this.exp = e;
    }
    public String toString(){
        return "Print(" + exp.toString() + ")";
    }
    public PrgState execute(PrgState state) throws MyException{

        return state;
    }

    public IStmt deepCopy(){
        return new PrintStmt(exp.deepCopy());
    }
}
