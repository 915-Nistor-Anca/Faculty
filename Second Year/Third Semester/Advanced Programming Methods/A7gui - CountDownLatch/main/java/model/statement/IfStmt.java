package model.statement;

import exception.MyException;
import model.programstate.PrgState;
import model.expression.Exp;
import model.other.MyIDictionary;
import model.other.MyIStack;
import model.type.BoolType;
import model.type.Type;
import model.value.BoolValue;
import model.value.Value;

public class IfStmt implements IStmt {
    Exp exp;
    IStmt thenS;
    IStmt elseS;

    public IfStmt(Exp expression, IStmt thenStatement, IStmt elseStatement) {
        this.exp = expression;
        this.thenS = thenStatement;
        this.elseS = elseStatement;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        Value result = this.exp.eval(state.getSymTable(), state.getHeap());
        if (result instanceof BoolValue boolResult) {
            IStmt statement;
            if (boolResult.getValue()) {
                statement = thenS;
            } else {
                statement = elseS;
            }

            MyIStack<IStmt> stack = state.getStk();
            stack.push(statement);
            state.setStk(stack);
            return null;
        } else {
            throw new MyException("Please provide a boolean expression in an if statement.");
        }
    }

    @Override
    public IStmt deepCopy() {
        return new IfStmt(exp.deepCopy(), thenS.deepCopy(), elseS.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typexp=exp.typecheck(typeEnv);
        if (typexp.equals(new BoolType())) {
            thenS.typecheck(typeEnv.deepCopy());
            elseS.typecheck(typeEnv.deepCopy());
            return typeEnv;
        }
        else
            throw new MyException("The condition of IF has not the type bool");
    }

    @Override
    public String toString() {
        return String.format("if(%s){%s}else{%s}", exp.toString(), thenS.toString(), elseS.toString());
    }
}