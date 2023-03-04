package model.other;

import exception.MyException;
import model.value.Value;

import java.util.HashMap;
import java.util.Set;

public class MyHeap implements MyIHeap {
    HashMap<Integer, Value> heap;
    Integer freeLocation;

    public MyHeap() {
        heap = new HashMap<>();
        freeLocation = 1;
    }

    public Integer getFreeValue() {
        return freeLocation;
    }

    public HashMap<Integer, Value> getContent() {
        return heap;
    }

    public void setContent(HashMap<Integer, Value> newMap) {
        this.heap = newMap;
    }

    public Integer add(Value value) {
        heap.put(freeLocation, value);
        Integer toReturn = freeLocation;
        freeLocation = newValue();
        return toReturn;
    }

    private Integer newValue() {
        freeLocation += 1;
        while (freeLocation == 0 || heap.containsKey(freeLocation))
            freeLocation += 1;
        return freeLocation;
    }

    public void update(Integer position, Value value) throws MyException {
        if (!heap.containsKey(position))
            throw new MyException(String.format("%d is not present in the heap!", position));
        heap.put(position, value);
    }

    public Value get(Integer position) throws MyException {
        if (!heap.containsKey(position))
            throw new MyException(String.format("%d is not present in the heap!", position));
        return heap.get(position);
    }

    public boolean containsKey(Integer position) {
        return this.heap.containsKey(position);
    }

    public void remove(Integer key) throws MyException {
        if (!containsKey(key))
            throw new MyException(key + "id not defined.");
        freeLocation = key;
        this.heap.remove(key);
    }

    public Set<Integer> keySet() {
        return heap.keySet();
    }

    public String toString() {
        return this.heap.toString();
    }
}
