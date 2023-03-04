package model.other;
import exception.MyException;

import java.util.List;

public interface MyIStack<T> {
    T pop() throws MyException;
    void push(T element);
    T peek();
    boolean isEmpty();
    List<T> getReversed();
}