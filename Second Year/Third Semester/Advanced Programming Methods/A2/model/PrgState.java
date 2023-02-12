package model;


public class PrgState {
    MyIStack<IStmt> stk;
    MyIDictionary<String, Value> symtbl;
    MyIList<Value> out;
    PrgState(MyIStack<IStmt> stk, MyIDictionary<String,Value> symtbl, MyIList<Value> out, IStmt ogPrg){
        this.stk = stk;
        this.symtbl = symtbl;
        this.out = out;
        stk.push(ogPrg);
    }

    public String toString(){
        return "ExeStack: " + stk.getReversed() + "\nSymTable:" + symtbl + "\nOutput:" + out;
    }
    public MyIStack<IStmt> getStk(){
        return this.stk;
    }
    public MyIDictionary<String, Value> getSymTable(){
        return this.symtbl;
    }
    public void setStk(MyIStack)
}
