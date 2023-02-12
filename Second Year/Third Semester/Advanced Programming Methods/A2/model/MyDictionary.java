package model;

import exception.MyException;

import java.util.HashMap;
import java.util.Map;

public class MyDictionary <K,V> implements MyIDictionary<K,V>{
    private Map<K,V> map;
    public MyDictionary(){
        map = new HashMap<>();
    }
    public void put(K key, V value){
        map.put(key, value);
    }

    public V LookUp(K key) throws MyException {
        V v = map.get(key);
        if (v == null){
            throw new MyException("Id not declared.");
        }
        return v;
    }

    public boolean isVarDef(K key){
        return this.map.containsKey(key);
    }

    public void update(K key, V value) throws MyException {
        if (!this.map.containsKey(key)){
            throw new MyException("Id not declared.");
        }
        this.put(key, value);
    }

    @Override
    public String toString(){
        return this.map.toString();
    }
}
