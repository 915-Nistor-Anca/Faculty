package model.statement;

import exception.MyException;
import model.expression.Exp;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.other.MyILatchTable;
import model.programstate.PrgState;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class NewLatchStmt implements IStmt{
    String var;
    Exp exp;
    Lock lock = new ReentrantLock();

    public NewLatchStmt(String var, Exp exp){
        this.var = var;
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIHeap heap = state.getHeap();
        MyILatchTable latchTable = state.getLatchTable();
        IntValue nr = (IntValue) (exp.eval(symTable, heap));
        int number = nr.getValue();
        int freeAddress = latchTable.getFreeAddress();
        latchTable.put(freeAddress, number);
        if (symTable.isDefined(var)) {
            symTable.update(var, new IntValue(freeAddress));
        } else {
            throw new MyException(String.format("%s is not defined in the symbol table!", var));
        }
        lock.unlock();
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new NewLatchStmt(var, exp.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookUp(var).equals(new IntType())) {
            if (exp.typecheck(typeEnv).equals(new IntType())) {
                return typeEnv;
            } else {
                throw new MyException("Expression doesn't have the int type!");
            }
        } else {
            throw new MyException(String.format("%s is not of int type!", var));
        }
    }

    public String toString() {
        return String.format("newLatch(%s, %s)", var, exp);
    }
}
