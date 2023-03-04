package model.statement;

import exception.MyException;
import model.expression.Exp;
import model.other.MyIDictionary;
import model.programstate.PrgState;
import model.type.BoolType;
import model.type.Type;

public class DoWhileStmt implements IStmt{
    IStmt stmt;
    Exp exp;

    public DoWhileStmt(IStmt stmt, Exp exp){
        this.stmt = stmt;
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        IStmt s = new CompStmt(stmt, new WhileStmt(exp, stmt));
        state.getExeStack().push(s);
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new DoWhileStmt(stmt.deepCopy(), exp.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeExpression = exp.typecheck(typeEnv);
        if (typeExpression.equals(new BoolType())) {
            stmt.typecheck(typeEnv.deepCopy());
            return typeEnv;
        } else
            throw new MyException("Condition in the do while statement must be bool!");

    }

    public String toString() {
        return String.format("do {%s} while (%s)", stmt, exp);
    }
}
