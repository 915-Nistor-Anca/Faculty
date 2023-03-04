package model.statement;

import exception.MyException;
import model.programstate.PrgState;
import model.expression.Exp;
import model.other.MyIDictionary;
import model.other.MyIList;
import model.type.Type;
import model.value.Value;

public class PrintStmt implements IStmt {
    Exp exp;

    public PrintStmt(Exp expression) {
        this.exp = expression;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIList<Value> out = state.getOut();
        out.add(exp.eval(state.getSymTable(), state.getHeap()));
        state.setOut(out);
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new PrintStmt(exp.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        exp.typecheck(typeEnv);
        return typeEnv;
    }

    @Override
    public String toString() {
        return String.format("Print(%s)", exp.toString());
    }
}