package model.other;

import exception.MyException;
import model.value.Value;

import java.util.HashMap;
import java.util.Set;

public interface MyIHeap {
    Integer getFreeValue();
    HashMap<Integer, Value> getContent();
    void setContent(HashMap<Integer, Value> newMap);
    Integer add(Value value);
    void update(Integer position, Value value) throws MyException;
    Value get(Integer position) throws MyException;
    boolean containsKey(Integer position);
    void remove(Integer key) throws MyException;
    Set<Integer> keySet();
}
