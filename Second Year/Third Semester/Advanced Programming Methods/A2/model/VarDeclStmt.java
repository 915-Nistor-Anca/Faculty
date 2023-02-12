package model;

public class VarDeclStmt implements IStmt{
    String name;
    Type typ;

    public VarDeclStmt(String name, Type typ) {
        this.name = name;
        this.typ = typ;
    }

    public IStmt deepCopy(){
        return  new VarDeclStmt(name, typ);
    }
}
