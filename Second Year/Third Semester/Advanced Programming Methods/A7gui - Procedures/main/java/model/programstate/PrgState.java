package model.programstate;

import exception.MyException;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.other.MyIList;
import model.other.MyIStack;
import model.statement.IStmt;
import model.value.Value;

import java.io.BufferedReader;
import java.util.List;

public class PrgState {
    MyIStack<IStmt> stk;
    MyIDictionary<String, Value> symtbl;
    MyIList<Value> out;
    MyIDictionary<String, BufferedReader> fileTable;
    MyIHeap heap;
    int id;
    static int last_id = 0;

    public PrgState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value> out, IStmt ogPrg, MyIDictionary<String, BufferedReader> fileTable, MyIHeap heap){
        this.stk = stk;
        this.symtbl = symtbl;
        this.out = out;
        this.fileTable = fileTable;
        stk.push(ogPrg);
        this.heap = heap;
        this.id = setId();
    }

    public synchronized int setId(){
        last_id++;
        return last_id;
    }

    public int getId() {
        return this.id;
    }

    public MyIStack<IStmt> getExeStack() {
        return stk;
    }

    public PrgState(MyIStack<IStmt> stack, MyIDictionary<String,Value> symTable, MyIList<Value> out, MyIDictionary<String, BufferedReader> fileTable, MyIHeap heap) {
        this.stk = stack;
        this.symtbl = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.id = setId();
    }

    public MyIStack<IStmt> getStk(){
        return this.stk;
    }
    public MyIDictionary<String, Value> getSymTable(){
        return this.symtbl;
    }
    public MyIList<Value> getOut(){
        return this.out;
    }

    public void setStk(MyIStack<IStmt> newStk){
        this.stk = newStk;
    }
    public void setSymTable(MyIDictionary<String, Value> newsymtbl){
        this.symtbl = newsymtbl;
    }
    public void setOut(MyIList<Value> newout) {this.out = newout;}

    public String toString() {
        return "Id:" + id + "\nExecution stack: \n" + stk.getReversed() + "\nSymbol table: \n" + symtbl.toString() + "\nOutput list: \n" + out.toString() + "\nFile table:\n" + fileTable.toString() + "\nHeap memory:\n" + heap.toString() + "\n";
    }

    public void setHeap(MyIHeap newHeap) {
        this.heap = newHeap;
    }

    public MyIHeap getHeap() {
        return heap;
    }

    public String exeStackToString() {
        StringBuilder exeStackStringBuilder = new StringBuilder();
        List<IStmt> stack = stk.getReversed();
        for (IStmt statement: stack) {
            exeStackStringBuilder.append(statement.toString()).append("\n");
        }
        return exeStackStringBuilder.toString();
    }

    public String symTableToString() throws MyException {
        StringBuilder symTableStringBuilder = new StringBuilder();
        for (String key: symtbl.keySet()) {
            symTableStringBuilder.append(String.format("%s -> %s\n", key, symtbl.lookUp(key).toString()));
        }
        return symTableStringBuilder.toString();
    }

    public String outToString() {
        StringBuilder outStringBuilder = new StringBuilder();
        for (Value elem: out.getList()) {
            outStringBuilder.append(String.format("%s\n", elem.toString()));
        }
        return outStringBuilder.toString();
    }

    public String fileTableToString() {
        StringBuilder fileTableStringBuilder = new StringBuilder();
        for (String key: fileTable.keySet()) {
            fileTableStringBuilder.append(String.format("%s\n", key));
        }
        return fileTableStringBuilder.toString();
    }

    public String heapToString() throws MyException {
        StringBuilder heapStringBuilder = new StringBuilder();
        for (int key: heap.keySet()) {
            heapStringBuilder.append(String.format("%d -> %s\n", key, heap.get(key)));
        }
        return heapStringBuilder.toString();
    }

    public String prgStateToString() throws MyException {
        return "Id:" + id + "\nExeStack: \n" + exeStackToString() + "SymTable: \n" + symTableToString() + "Out: \n" + outToString() + "FileTable:\n" + fileTableToString() + "Heap memory:\n" + heapToString() ;
    }

    public MyIDictionary<String, BufferedReader> getFileTable() {
        return this.fileTable;
    }

    public void setFileTable(MyIDictionary<String, BufferedReader> newFileTable) {
        this.fileTable = newFileTable;
    }

    public boolean isNotCompleted(){
        return !stk.isEmpty();
    }

    public PrgState oneStep() throws MyException{
        if(stk.isEmpty()) throw new MyException("prgstate stack is empty");
        IStmt crtStmt = stk.pop();
        return crtStmt.execute(this);
    }


}


