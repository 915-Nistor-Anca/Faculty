package model.expression;
import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.type.Type;
import model.value.Value;

public class ValueExp implements Exp {
    Value value;

    public ValueExp(Value value) {
        this.value = value;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) {
        return this.value;
    }

    @Override
    public Exp deepCopy() {
        return new ValueExp(value);
    }

    @Override
    public String toString() {
        return this.value.toString();
    }

    @Override
    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException {
        return value.getType();
    }
}