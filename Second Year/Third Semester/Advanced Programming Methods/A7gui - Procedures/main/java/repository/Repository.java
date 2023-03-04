package repository;
import exception.MyException;
import model.programstate.PrgState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Repository implements IRepository{
    private List<PrgState> programStates;
    private int currentPosition;

    private String logFilePath;


    public Repository(PrgState programState, String logFilePath){
        this.programStates = new ArrayList<>();
        this.currentPosition = 0;
        this.addProgram(programState);

        this.logFilePath = logFilePath;
    }

    @Override
    public void addProgram(PrgState program) {
        this.programStates.add(program);
    }

    //@Override
    //public PrgState getCurrentState() {
    //    return this.programStates.get(this.currentPosition);
    //}

    @Override
    public void logPrgStateExec(PrgState p) throws MyException, IOException {
        PrintWriter logFile;
        logFile= new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        logFile.println(p.prgStateToString());
        logFile.close();
    }

    @Override
    public List<PrgState> getPrgList(){
        return this.programStates;
    }

    @Override
    public void setPrgList(List<PrgState> list){
        this.programStates = list;
    }

}