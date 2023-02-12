package model;

import exception.MyException;

public class CompStmt implements IStmt{
    IStmt first;
    IStmt snd;

    public CompStmt(IStmt f, IStmt s) {
        this.first = f;
        this.snd = s;
    }

    public String toString(){
        return "(" + first.toString() + "|" + snd.toString() + ")";
    }
    public PrgState execute(PrgState state) throws MyException{
        MyIStack<IStmt> stk = state.getStk();
        stk.push(snd);
        stk.push(first);

        return state;
    }
    public IStmt deepCopy(){
        return new CompStmt(first.deepCopy(), snd.deepCopy());
    }
}
