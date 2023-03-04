package model.expression;

import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.type.IntType;
import model.type.Type;
import model.value.Value;

public class MULExp implements Exp{
    Exp exp1;
    Exp exp2;

    public MULExp(Exp exp1, Exp exp2){
        this.exp1 = exp1;
        this.exp2 = exp2;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws MyException {
        Exp e = new ArithExp("-", new ArithExp("*", exp1, exp2),
                new ArithExp("+", exp1, exp2));
        return e.eval(symTable, heap);
    }

    @Override
    public Exp deepCopy() {
        return new MULExp(exp1.deepCopy(), exp2.deepCopy());
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type type1 = exp1.typecheck(typeEnv);
        Type type2 = exp2.typecheck(typeEnv);
        if (type1.equals(new IntType()) && type2.equals(new IntType()))
            return new IntType();
        else throw new MyException("Exp1 and exp2 in MUL must be int!");
    }

    public String toString() {
        return String.format("MUL(%s, %s)", exp1, exp2);
    }
}
