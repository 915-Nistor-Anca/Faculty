package model;

import exception.MyException;

public class AssignStmt implements IStmt{
    String id;
    Exp exp;
    public AssignStmt(String id, Exp exp){
        this.id = id;
        this.exp = exp;
    }
    public String toString(){
        return id + " = " + exp.toString();
    }
    public PrgState execute(PrgState state) throws MyException{

        MyIDictionary<String,Value> symTbl= state.getSymTable();
        if (symTbl.isVarDef(id)){
            Value val = exp.eval(symTbl);
            Type typId = (symTbl.LookUp(id)).getType();
            if (val.getType().equals(typId)) symTbl.update(id, val);
            else throw new MyException("Declared type of variable " + id + " and type of the assigned expression do not match.");
        }
        else throw new MyException("The used variable "  + id +  " was not declared before.");

        state.setSymTable(symTbl);
        return state;
    }

    public IStmt deepCopy(){
        return new AssignStmt(id, exp.deepCopy());
    }
}
