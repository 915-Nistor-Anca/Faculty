package model.expression;

import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.type.IntType;
import model.type.Type;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.Value;

public class ArithExp implements Exp {
    Exp expression1;
    Exp expression2;
    String operation;

    public ArithExp(String operation, Exp expression1, Exp expression2) {
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.operation = operation;
    }

    public Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws MyException {
        Value value1, value2;
        value1 = this.expression1.eval(symTable, heap);
        if (value1.getType().equals(new IntType())) {
            value2 = this.expression2.eval(symTable, heap);
            if (value2.getType().equals(new IntType())) {
                IntValue int1 = (IntValue) value1;
                IntValue int2 = (IntValue) value2;
                int n1, n2;
                n1 = int1.getValue();
                n2 = int2.getValue();
                if (this.operation.equals("+"))
                    return new IntValue(n1 + n2);
                else if (this.operation.equals("-"))
                    return new IntValue(n1 - n2);
                else if (this.operation.equals("*"))
                    return new IntValue(n1 * n2);
                else if (this.operation.equals("/"))
                    return new BoolValue(n1 != n2);
                    if (n2 == 0)
                        throw new MyException("Division by zero.");
                    else
                        return new IntValue(n1 / n2);
            } else
                throw new MyException("Second operand is not an integer.");
        } else
            throw new MyException("First operand is not an integer.");
    }

    @Override
    public Exp deepCopy() {
        return new ArithExp(operation, expression1.deepCopy(), expression2.deepCopy());
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
            Type typ1, typ2;
            typ1=expression1.typecheck(typeEnv);
            typ2=expression2.typecheck(typeEnv);
            if (typ1.equals(new IntType())) {
                if (typ2.equals(new IntType())) {
                    return new IntType();
                } else
                throw new MyException("second operand is not an integer");
            }else
            throw new MyException("first operand is not an integer");
        }

    @Override
    public String toString() {
        return expression1.toString() + " " + operation + " " + expression2.toString();
    }


}