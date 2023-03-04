package model.statement;

import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyILockTable;
import model.programstate.PrgState;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockStmt implements IStmt{
    String var;
    Lock lock = new ReentrantLock();

    public LockStmt(String var) {
        this.var = var;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyILockTable lockTable = state.getLockTable();
        if (symTable.isDefined(var)) {
            if (symTable.lookUp(var).getType().equals(new IntType())) {
                IntValue fi = (IntValue) symTable.lookUp(var);
                int foundIndex = fi.getValue();
                if (lockTable.containsKey(foundIndex)) {
                    if (lockTable.get(foundIndex) == -1) {
                        lockTable.update(foundIndex, state.getId());
                        state.setLockTable(lockTable);
                    } else {
                        state.getExeStack().push(this);
                    }
                } else {
                    throw new MyException("Index is not in the lock table!");
                }
            } else {
                throw new MyException("Var is not of type int!");
            }
        } else {
            throw new MyException("Variable not defined!");
        }
        lock.unlock();
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new LockStmt(var);
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookUp(var).equals(new IntType())) {
            return typeEnv;
        } else {
            throw new MyException("Var is not of int type!");
        }
    }

    public String toString() {
        return String.format("lock(%s)", var);
    }
}
