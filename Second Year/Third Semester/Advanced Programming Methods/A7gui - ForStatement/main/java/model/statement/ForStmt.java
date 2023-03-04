package model.statement;

import exception.MyException;
import model.expression.Exp;
import model.expression.RelExp;
import model.expression.VarExp;
import model.other.MyIDictionary;
import model.other.MyIStack;
import model.programstate.PrgState;
import model.type.IntType;
import model.type.Type;

public class ForStmt implements IStmt{

    String v;
    Exp exp1;
    Exp exp2;
    Exp exp3;
    IStmt stmt;

    public ForStmt(String v, Exp exp1, Exp exp2, Exp exp3, IStmt stmt){
        this.v = v;
        this.exp1 = exp1;
        this.exp2 = exp2;
        this.exp3 = exp3;
        this.stmt = stmt;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> exeStk = state.getExeStack();
        IStmt s = new CompStmt(new AssignStmt("v", exp1), new WhileStmt(new RelExp("<",
                new VarExp("v"), exp2), new CompStmt(stmt, new AssignStmt("v", exp3))));
        exeStk.push(s);
        state.setStk(exeStk);
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new ForStmt(v, exp1.deepCopy(), exp2.deepCopy(), exp3.deepCopy(), stmt.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t1 = exp1.typecheck(typeEnv);
        Type t2 = exp2.typecheck(typeEnv);
        Type t3 = exp3.typecheck(typeEnv);

        if (t1.equals(new IntType()) && t2.equals(new IntType()) && t3.equals(new IntType())) return typeEnv;
        else throw new MyException("Not everything has the type Int in the ForStmt!");
    }

    @Override
    public String toString() {
        return String.format("for(%s=%s; %s<%s; %s=%s) {%s}", v, exp1, v, exp2, v, exp3, stmt);
    }
}
