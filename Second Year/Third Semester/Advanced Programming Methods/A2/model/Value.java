package model;

public interface Value {
    Type getType();
    Value deepCopy();
}
