package model.statement;

import exception.MyException;
import javafx.util.Pair;
import model.expression.Exp;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.other.MyISemaphoreTable;
import model.programstate.PrgState;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.ArrayList;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class CreateSemaphoreStmt implements IStmt{
    String var;
    Exp exp;
    Lock lock = new ReentrantLock();

    public CreateSemaphoreStmt(String var, Exp expression) {
        this.var = var;
        this.exp = expression;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIHeap heap = state.getHeap();
        MyISemaphoreTable semaphoreTable = state.getSemaphoreTable();
        IntValue nr = (IntValue) (exp.eval(symTable, heap));
        int number = nr.getValue();
        int freeAddress = semaphoreTable.getFreeAddress();
        semaphoreTable.put(freeAddress, new Pair<>(number, new ArrayList<>()));
        if (symTable.isDefined(var) && symTable.lookUp(var).getType().equals(new IntType()))
            symTable.update(var, new IntValue(freeAddress));
        else
            throw new MyException(String.format("Error for variable %s: not defined/does not have int type!", var));
        lock.unlock();
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new CreateSemaphoreStmt(var, exp.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookUp(var).equals(new IntType())) {
            if (exp.typecheck(typeEnv).equals(new IntType()))
                return typeEnv;
            else
                throw new MyException("Expression is not of int type!");
        } else {
            throw new MyException(String.format("%s is not of type int!", var));
        }
    }

    public String toString() {
        return String.format("createSemaphore(%s, %s)", var, exp);
    }
}
