package model;

import java.util.ArrayList;
import java.util.List;

public class MyList <T> implements MyIList<T>{
    private List<T> out;
    public MyList(){
        this.out = new ArrayList<T>();
    }
    public void add(T elem){
        out.add(elem);
    }

    @Override
    public String toString() {
        return out.toString();
    }
}
