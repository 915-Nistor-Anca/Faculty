package model;

import exception.MyException;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class MyStack <T> implements MyIStack<T>{
    private Stack<T> stk;
    public MyStack(){
        stk = new Stack<T>();
    }
    public void push(T elem){
        stk.push(elem);
    }

    public T pop() throws MyException {
        if (stk.isEmpty())
            throw new MyException("Empty stack!");
        return stk.pop();
    }

    public boolean isEmpty(){ return stk.empty();}

    public List<T> getReversed() {
        List<T> l = new ArrayList<T>(stk);
        Collections.reverse(l);
        return l;
    }

}
