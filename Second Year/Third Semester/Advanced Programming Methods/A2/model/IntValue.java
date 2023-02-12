package model;

public class IntValue implements Value{
    int val;
    IntValue(int v){
        val = v;
    }
    int getVal(){
        return val;
    }
    public String toString(){

    }
    public Type getType(){
        return new IntType();
    }

    public Value deepCopy() {
        return new IntValue(val);
    }
}
