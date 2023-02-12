package model;

import java.beans.Expression;

public class ArithExp implements Exp{
    Exp e1;
    Exp e2;
    int op;

    public ArithExp(Exp e1, Exp e2, int op) {
        this.e1 = e1;
        this.e2 = e2;
        this.op = op;
    }

    public Expression deepCopy() {
        return new ArithExp(e1.deepCopy(), e2.deepCopy(), op);
    }
}
