package model.statement;

import exception.MyException;
import model.programstate.PrgState;
import model.other.MyDictionary;
import model.other.MyIDictionary;
import model.other.MyIStack;
import model.other.MyStack;
import model.type.Type;
import model.value.Value;

import java.util.Map;

public class ForkStmt implements IStmt{

    IStmt statement;

    public ForkStmt(IStmt stmt){
        this.statement = stmt;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stack = new MyStack<>();
        stack.push(statement);

        MyIDictionary<String, Value> symtbl = new MyDictionary<>();
        for (Map.Entry<String, Value> entry: state.getSymTable().getContent().entrySet()){
            symtbl.put(entry.getKey(), entry.getValue().deepCopy());
        }

        return new PrgState(stack, symtbl, state.getOut(),state.getFileTable(), state.getHeap(), state.getSemaphoreTable());
    }

    @Override
    public IStmt deepCopy() {
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        statement.typecheck(typeEnv.deepCopy());
        return typeEnv;
    }

    public String toString() {
        return String.format("Fork(%s)", statement.toString());
    }
}
