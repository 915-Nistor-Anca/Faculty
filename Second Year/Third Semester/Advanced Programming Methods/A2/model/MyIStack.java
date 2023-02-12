package model;

import exception.MyException;

import java.util.List;

public interface MyIStack <T>{
    void push(T elem);
    T pop() throws MyException;
    boolean isEmpty();
    List<T> getReversed();
}
