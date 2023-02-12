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

public class NewStmt implements IStmt{

    String var_name;
    Exp expression;

    public NewStmt(String var_name, Exp expression){
        this.var_name = var_name;
        this.expression = expression;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> sym_tbl = state.getSymTable();
        MyIHeap heap = state.getHeap();
        if (sym_tbl.isDefined(var_name)){
            Value v = sym_tbl.lookUp(var_name);
            if (v.getType() instanceof RefType){
                Value evaluate = expression.eval(sym_tbl, heap);
                Type loc_type = ((RefValue) v).getLocationType();
                if (loc_type.equals(evaluate.getType())){
                    int new_pos = heap.add(evaluate);
                    sym_tbl.put(var_name, new RefValue(new_pos, loc_type));
                    state.setSymTable(sym_tbl);
                    state.setHeap(heap);
                }
                else throw new MyException(String.format("%s is not of %s", var_name, evaluate.getType()));

            }
            else throw new MyException(String.format("%s type is not RefType", var_name));

        }
        else throw new MyException(String.format("%s is not a variable in the SymTable", var_name));
    return null;
    }

    @Override
    public IStmt deepCopy() {
        return new NewStmt(var_name, expression.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typevar = typeEnv.lookUp(var_name);
        Type typexp = expression.typecheck(typeEnv);
        if (typevar.equals(new RefType(typexp)))
            return typeEnv;
        else
            throw new MyException("NEW stmt: right hand side and left hand side have different types ");
    }

    public String toString(){
        return String.format("New(%s, %s)", var_name, expression);
    }
}
