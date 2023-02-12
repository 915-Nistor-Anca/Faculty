package model.expression;

import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.type.BoolType;
import model.type.IntType;
import model.type.Type;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.Value;

public class RelExp implements Exp{
    Exp expression1;
    Exp expression2;
    String operator;

    public RelExp(String operator, Exp expression1, Exp expression2) {
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.operator = operator;
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type type1, type2;
        type1 = expression1.typecheck(typeEnv);
        type2 = expression2.typecheck(typeEnv);
        if (type1.equals(new IntType())) {
            if (type2.equals(new IntType())) {
                return new BoolType();
            } else
                throw new MyException("Second operand is not an integer.");
        } else
            throw new MyException("First operand is not an integer.");

    }

    @Override
    public Value eval(MyIDictionary<String, Value> table, MyIHeap heap) throws MyException {
        Value value1, value2;
        value1 = this.expression1.eval(table, heap);
        if (value1.getType().equals(new IntType())) {
            value2 = this.expression2.eval(table, heap);
            if (value2.getType().equals(new IntType())) {
                IntValue val1 = (IntValue) value1;
                IntValue val2 = (IntValue) value2;
                int n1, n2;
                n1 = val1.getValue();
                n2 = val2.getValue();
                if (this.operator.equals("<"))
                    return new BoolValue(n1 < n2);
                else if (this.operator.equals("<="))
                    return new BoolValue(n1 <= n2);
                else if (this.operator.equals("=="))
                    return new BoolValue(n1 == n2);
                else if (this.operator.equals("!="))
                    return new BoolValue(n1 != n2);
                else if (this.operator.equals(">"))
                    return new BoolValue(n1 > n2);
                else if (this.operator.equals(">="))
                    return new BoolValue(n1 >= n2);
            } else
                throw new MyException("Second operand is not an integer.");
        } else
            throw new MyException("First operand is not an integer.");
        return null;
    }

    @Override
    public Exp deepCopy() {
        return new RelExp(operator, expression1.deepCopy(), expression2.deepCopy());
    }

    @Override
    public String toString() {
        return this.expression1.toString() + " " + this.operator + " " + this.expression2.toString();
    }
}