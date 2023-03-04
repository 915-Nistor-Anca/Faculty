package model.other;

import exception.MyException;
import javafx.util.Pair;

import java.util.HashMap;
import java.util.List;

public class MySemaphoreTable implements MyISemaphoreTable{
    private HashMap<Integer, Pair<Integer, List<Integer>>> semaphoreTable;
    private int freeLocation = 0;

    public MySemaphoreTable() {
        this.semaphoreTable = new HashMap<>();
    }

    @Override
    public void put(int key, Pair<Integer, List<Integer>> value) throws MyException {
        if (!semaphoreTable.containsKey(key)) {
            semaphoreTable.put(key, value);
        } else {
            throw new MyException(String.format("Semaphore table already contains the key %d!", key));
        }
    }

    @Override
    public Pair<Integer, List<Integer>> get(int key) throws MyException {
        if (semaphoreTable.containsKey(key)) {
            return semaphoreTable.get(key);
        } else {
            throw new MyException(String.format("Semaphore table doesn't contain the key %d!", key));
        }
    }

    @Override
    public boolean containsKey(int key) {
        return semaphoreTable.containsKey(key);
    }

    @Override
    public int getFreeAddress() {
        freeLocation++;
        return freeLocation;
    }

    @Override
    public void setFreeAddress(int freeAddress) {
        this.freeLocation = freeAddress;
    }

    @Override
    public void update(int key, Pair<Integer, List<Integer>> value) throws MyException {
        if (semaphoreTable.containsKey(key)) {
            semaphoreTable.replace(key, value);
        } else {
            throw new MyException(String.format("Semaphore table doesn't contain key %d!", key));
        }
    }

    @Override
    public HashMap<Integer, Pair<Integer, List<Integer>>> getSemaphoreTable() {
        return semaphoreTable;
    }

    @Override
    public void setSemaphoreTable(HashMap<Integer, Pair<Integer, List<Integer>>> newSemaphoreTable) {
        this.semaphoreTable = newSemaphoreTable;
    }

    public String toString() {
        return semaphoreTable.toString();
    }
}
