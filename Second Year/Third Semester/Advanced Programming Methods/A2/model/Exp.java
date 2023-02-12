package model;

import exception.MyException;

import java.beans.Expression;

public interface Exp {
    Value eval(MyIDictionary<String, Value> tbl) throws MyException;
    Exp deepCopy();
}
