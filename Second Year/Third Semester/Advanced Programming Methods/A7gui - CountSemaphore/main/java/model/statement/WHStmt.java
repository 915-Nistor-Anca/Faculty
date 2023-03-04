package model.statement;

import exception.MyException;
import model.programstate.PrgState;
import model.expression.Exp;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.type.RefType;
import model.type.Type;
import model.value.RefValue;
import model.value.Value;

public class WHStmt implements IStmt{
    String var_name;
    Exp expression;

    public WHStmt(String var_name, Exp expression){
        this.var_name = var_name;
        this.expression = expression;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap heap = state.getHeap();
        if (!symTbl.isDefined(var_name))
            throw new MyException(String.format("%s is not defined", var_name));
        Value v = symTbl.lookUp(var_name);
        if (!(v instanceof RefValue))
            throw new MyException(String.format("%s is not a RefType"));
        RefValue refValue = (RefValue) v;
        Value evaluated = expression.eval(symTbl, heap);
        if (!evaluated.getType().equals(refValue.getLocationType()))
            throw new MyException(String.format("%s not a %s", evaluated, refValue.getLocationType()));
        heap.update(refValue.getAddr(), evaluated);
        state.setHeap(heap);
        return null;

    }

    @Override
    public IStmt deepCopy() {
        return new WHStmt(var_name, expression.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookUp(var_name).equals(new RefType(expression.typecheck(typeEnv))))
            return typeEnv;
        else
            throw new MyException("WriteHeap: right hand side and left hand side have different types.");
    }

    public String toString(){
        return String.format("WriteHeap(%s, %s)", var_name, expression);
    }
}
