package model;

import exception.MyException;

public interface MyIDictionary <K,V>{
    void put(K key, V value);
    V LookUp(K key) throws MyException;
    boolean isVarDef(K key);
    void update(K key, V value) throws MyException;


}
