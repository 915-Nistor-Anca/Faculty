package model.expression;

import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.type.Type;
import model.value.Value;

public interface Exp {
    Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws MyException;
    Exp deepCopy();

    Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException;
}