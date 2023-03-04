package model.statement;

import exception.MyException;
import model.programstate.PrgState;
import model.expression.Exp;
import model.other.MyIDictionary;
import model.type.StringType;
import model.type.Type;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenRFile implements IStmt{
    private Exp exp;

    public OpenRFile(Exp exp){
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        Value value = exp.eval(state.getSymTable(), state.getHeap());
        if (value.getType().equals(new StringType())) {
            StringValue fileName = (StringValue) value;
            MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
            if (!fileTable.isDefined(fileName.getValue())) {
                BufferedReader br;
                try {
                    br = new BufferedReader(new FileReader(fileName.getValue()));
                } catch (FileNotFoundException e) {
                    throw new MyException(String.format("%s could not be opened", fileName.getValue()));
                }
                fileTable.put(fileName.getValue(), br);
                state.setFileTable(fileTable);
            } else {
                throw new MyException(String.format("%s is already opened", fileName.getValue()));
            }
        } else {
            throw new MyException(String.format("%s does not evaluate to StringType", exp.toString()));
        }
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new OpenRFile(exp.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (exp.typecheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new MyException("OpenReadFile requires a string expression.");
    }

    @Override
    public String toString() {
        return String.format("OpenRFile(%s)", exp.toString());
    }
}
