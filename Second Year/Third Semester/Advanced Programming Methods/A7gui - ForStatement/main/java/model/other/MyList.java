package model.other;


import exception.MyException;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements MyIList<T>{
    List<T> list;

    public MyList() {
        this.list = new ArrayList<>();
    }

    @Override
    public void add(T elem) {
        this.list.add(elem);
    }

    @Override
    public T pop() throws MyException {
        if (list.isEmpty())
            throw new MyException("The list is empty!");
        return this.list.remove(0);
    }


    @Override
    public String toString() {
        return this.list.toString();
    }

    @Override
    public List<T> getList(){
        return this.list;
    }

}