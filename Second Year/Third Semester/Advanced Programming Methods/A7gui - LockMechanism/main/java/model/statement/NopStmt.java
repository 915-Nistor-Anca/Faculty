package model.statement;

import exception.MyException;
import model.other.MyIDictionary;
import model.programstate.PrgState;
import model.type.Type;

public class NopStmt implements IStmt{
    @Override
    public PrgState execute(PrgState state) throws MyException {
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new NopStmt();
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    public String toString() {
        return "nop";
    }
}
