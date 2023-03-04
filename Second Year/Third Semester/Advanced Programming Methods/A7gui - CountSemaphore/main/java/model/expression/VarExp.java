package model.expression;

import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.type.Type;
import model.value.Value;

public class VarExp implements Exp {
    String key;

    public VarExp(String key) {
        this.key = key;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws MyException {
        return symTable.lookUp(key);
    }

    @Override
    public Exp deepCopy() {
        return new VarExp(key);
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv.lookUp(key);
    }

    @Override
    public String toString() {
        return key;
    }
}