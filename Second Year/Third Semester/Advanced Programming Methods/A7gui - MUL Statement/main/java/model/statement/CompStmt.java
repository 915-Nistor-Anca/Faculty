package model.statement;

import exception.MyException;
import model.programstate.PrgState;
import model.other.MyIDictionary;
import model.other.MyIStack;
import model.type.Type;

public class CompStmt implements IStmt {
    IStmt first;
    IStmt snd;

    public CompStmt(IStmt firstStatement, IStmt secondStatement) {
        this.first = firstStatement;
        this.snd = secondStatement;
    }

    @Override
    public PrgState execute(PrgState state){
        MyIStack<IStmt> stk = state.getStk();
        stk.push(snd);
        stk.push(first);
        state.setStk(stk);
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new CompStmt(first.deepCopy(), snd.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        //MyIDictionary<String,Type> typEnv1 = first.typecheck(typeEnv);
        //MyIDictionary<String,Type> typEnv2 = snd.typecheck(typEnv1);
        //return typEnv2;
        return snd.typecheck(first.typecheck(typeEnv));
    }

    @Override
    public String toString() {
        return String.format("(%s|%s)", first.toString(), snd.toString());
    }
}