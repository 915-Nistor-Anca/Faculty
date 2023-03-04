package model.statement;

import exception.MyException;
import model.programstate.PrgState;
import model.expression.Exp;
import model.other.MyIDictionary;
import model.type.IntType;
import model.type.StringType;
import model.type.Type;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFile implements IStmt{
    private Exp exp;
    private String var_name;

    public ReadFile(Exp exp, String var_name){
        this.exp = exp;
        this.var_name = var_name;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();

        if (symTable.isDefined(var_name)) {
            Value value = symTable.lookUp(var_name);
            if (value.getType().equals(new IntType())) {
                value = exp.eval(symTable, state.getHeap());
                if (value.getType().equals(new StringType())) {
                    StringValue castValue = (StringValue) value;
                    if (fileTable.isDefined(castValue.getValue())) {
                        BufferedReader br = fileTable.lookUp(castValue.getValue());
                        try {
                            String line = br.readLine();
                            if (line == null)
                                line = "0";
                            symTable.put(var_name, new IntValue(Integer.parseInt(line)));
                        } catch (IOException e) {
                            throw new MyException(String.format("Could not read from file %s", castValue));
                        }
                    } else {
                        throw new MyException(String.format("The file table does not contain %s", castValue));
                    }
                } else {
                    throw new MyException(String.format("%s does not evaluate to StringType", value));
                }
            } else {
                throw new MyException(String.format("%s is not of type IntType", value));
            }
        } else {
            throw new MyException(String.format("%s is not present in the symTable.", var_name));
        }
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new ReadFile(exp.deepCopy(), var_name);
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (exp.typecheck(typeEnv).equals(new StringType()))
            if (typeEnv.lookUp(var_name).equals(new IntType()))
                return typeEnv;
            else
                throw new MyException("ReadFile requires an int as its variable parameter.");
        else
            throw new MyException("ReadFile requires a string as es expression parameter.");
    }

    @Override
    public String toString() {
        return String.format("ReadFile(%s, %s)", exp.toString(), var_name);
    }
}

