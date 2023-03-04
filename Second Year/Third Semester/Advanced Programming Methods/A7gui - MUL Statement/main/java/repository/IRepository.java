package repository;

import exception.MyException;
import model.programstate.PrgState;

import java.io.IOException;
import java.util.List;

public interface IRepository {
    //PrgState getCurrentState();
    void addProgram(PrgState program);

    void logPrgStateExec(PrgState p) throws MyException, IOException;

    List<PrgState> getPrgList();

    void setPrgList(List<PrgState> list);

}