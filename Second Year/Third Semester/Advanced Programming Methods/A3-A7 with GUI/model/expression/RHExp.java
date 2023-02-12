package model.expression;

import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.type.RefType;
import model.type.Type;
import model.value.RefValue;
import model.value.Value;

public class RHExp implements Exp{
    Exp expression;

    public RHExp(Exp exp){
        this.expression = exp;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws MyException {
        Value value = expression.eval(symTable, heap);
        if (value instanceof RefValue) {
            RefValue refValue = (RefValue) value;
            if (heap.containsKey(refValue.getAddr()))
                return heap.get(refValue.getAddr());
            else
                throw new MyException("The address is not defined on the heap!");
        } else
            throw new MyException(String.format("%s not of RefType", value));

    }

    @Override
    public Exp deepCopy() {
        return new RHExp(expression.deepCopy());
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
            Type typ=expression.typecheck(typeEnv);
            if (typ instanceof RefType) {
                RefType reft =(RefType) typ;
                return reft.getInner();
            } else
                throw new MyException("the rH argument is not a Ref Type");
    }


    public String toString() {
        return String.format("ReadHeap(%s)", expression);
    }
}

