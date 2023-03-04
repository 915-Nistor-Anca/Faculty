package model.statement;

import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyILatchTable;
import model.programstate.PrgState;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class AwaitStmt implements IStmt{
    String var;
    Lock lock = new ReentrantLock();

    public AwaitStmt(String var) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyILatchTable latchTable = state.getLatchTable();
        if (symTable.isDefined(var)) {
            IntValue fi = (IntValue) symTable.lookUp(var);
            int foundIndex = fi.getValue();
            if (latchTable.containsKey(foundIndex)) {
                if (latchTable.get(foundIndex) != 0) {
                    state.getExeStack().push(this);
                }
            } else {
                throw new MyException("Index not found in the latch table!");
            }
        } else {
            throw new MyException("Variable not defined!");
        }
        lock.unlock();
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new AwaitStmt(var);
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookUp(var).equals(new IntType()))
            return typeEnv;
        else
            throw new MyException(String.format("%s is not of int type!", var));
    }

    public String toString() {
        return String.format("await(%s)", var);
    }
}
