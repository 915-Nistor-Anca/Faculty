package model.statement;

import exception.MyException;
import model.expression.Exp;
import model.expression.VarExp;
import model.other.MyIDictionary;
import model.other.MyIStack;
import model.programstate.PrgState;
import model.type.BoolType;
import model.type.Type;

public class CondAssignStmt implements IStmt{
    String v;
    Exp exp1;
    Exp exp2;
    Exp exp3;

    public CondAssignStmt(String v, Exp e1, Exp e2, Exp e3){
        this.v = v;
        this.exp1 = e1;
        this.exp2 = e2;
        this.exp3 = e3;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> exeStk = state.getExeStack();
        IStmt s = new IfStmt(exp1, new AssignStmt(v, exp2), new AssignStmt(v, exp3));
        exeStk.push(s);
        state.setStk(exeStk);
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new CondAssignStmt(v, exp1.deepCopy(), exp2.deepCopy(), exp3.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type vt = new VarExp(v).typecheck(typeEnv);
        Type e1t = exp1.typecheck(typeEnv);
        Type e2t = exp2.typecheck(typeEnv);
        Type e3t = exp3.typecheck(typeEnv);
        if (e1t.equals(new BoolType()) && e2t.equals(vt) && e3t.equals(vt))
            return typeEnv;
        else throw new MyException("The conditional assignment statement is incorrect!");
    }

    public String toString() {
        return String.format("%s=(%s)? %s: %s", v, exp1, exp2, exp3);
    }
}
