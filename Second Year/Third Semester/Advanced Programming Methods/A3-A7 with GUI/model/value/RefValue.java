package model.value;

import model.type.RefType;
import model.type.Type;

public class RefValue implements Value{
    int address;
    Type locationType;

    public RefValue(int addr, Type locT) {
        this.address = addr;
        this.locationType = locT;
    }

    public int getAddr() {
        return address;
    }
    public Type getType() {
        return new RefType(locationType);
    }

    public Type getLocationType() {
        return locationType;
    }

    @Override
    public Value deepCopy() {
        return new RefValue(address, locationType);
    }

    public String toString() {
        return String.format("(%d, %s)", address, locationType);
    }
}
