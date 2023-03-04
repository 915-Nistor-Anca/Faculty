package model.statement;

import exception.MyException;
import model.programstate.PrgState;
import model.other.MyIDictionary;
import model.type.Type;

public interface IStmt {
    PrgState execute(PrgState state) throws MyException;
    IStmt deepCopy();

    MyIDictionary<String,Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException;
}