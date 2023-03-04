package controller;

import exception.MyException;
import model.programstate.PrgState;
import model.value.RefValue;
import model.value.Value;
import repository.IRepository;

import java.io.IOException;
import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Pair {
    final PrgState first;
    final MyException second;

    public Pair(PrgState first, MyException second) {
        this.first = first;
        this.second = second;
    }
}

public class Controller {
    IRepository repository;
    boolean displayWithSteps = false;
    ExecutorService executor;

    public void setDisplayWithSteps(boolean value) {
        this.displayWithSteps = value;
    }

    public Controller(IRepository repository) {
        this.repository = repository;
    }

    //public PrgState oneStep(PrgState state) throws MyException {
    //    MyIStack<IStmt> stack = state.getStk();
    //    if (stack.isEmpty())
    //        throw new MyException("Program state stack is empty.");
    //    IStmt currentStatement = stack.pop();
    //    state.setStk(stack);
    //    return currentStatement.execute(state);
    //}

    Map<Integer, Value> safeGarbageCollector(List<Integer> symTableAddr, List<Integer> heap_addr, HashMap<Integer,Value> heap){
        return heap.entrySet().stream()
                .filter(e->(symTableAddr.contains(e.getKey()) || heap_addr.contains(e.getKey())))
                        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }


    List<Integer> getAddrFromSymTable(Collection<Value> symTableValues){
        return symTableValues.stream()
                .filter(v-> v instanceof RefValue)
                .map(v-> {RefValue v1 = (RefValue)v; return v1.getAddr();})
                .collect(Collectors.toList());
    }

    public List<Integer> getAddrFromHeap(Collection<Value> heapValues) {
        return heapValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue) v; return v1.getAddr();})
                .collect(Collectors.toList());
    }

    //public void allSteps() throws MyException, IOException {
    //    PrgState program = this.repository.getCurrentState();
    //    this.repository.logPrgStateExec();
    //    display();
    //    while(!program.getStk().isEmpty()) {
    //        oneStep(program);
    //        this.repository.logPrgStateExec();

    //        program.getHeap().setContent(
    //                (HashMap<Integer, Value>) unsafeGarbageCollector(
    //                    getAddrFromSymTable(program.getSymTable().getContent().values()),
    //                    getAddrFromHeap(program.getHeap().getContent().values()),
    //                    program.getHeap().getContent())
    //        );

    //        display();
    //    }
    // }

    private void display(PrgState programState) {
        if (displayWithSteps) {
            System.out.println(programState.toString());
        }
    }

    public List<PrgState> removeCompletedPrg(List<PrgState> inPrgList){
        return inPrgList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());
    }

    public void oneStepForAllPrg(List<PrgState> programStates) throws InterruptedException, MyException {
        programStates.forEach(programState -> {
            try {
                repository.logPrgStateExec(programState);
                display(programState);
            } catch (MyException e) {
                System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
        List<Callable<PrgState>> callList = programStates.stream()
                .map((PrgState p) -> (Callable<PrgState>) (p::oneStep))
                .collect(Collectors.toList());

        List<Pair> newProgramList;
        newProgramList = executor.invokeAll(callList).stream()
                .map(future -> {
                    try {
                        return new Pair(future.get(), null);
                    } catch (InterruptedException | ExecutionException e) {
                        if (e.getCause() instanceof MyException)
                            return new Pair(null, (MyException) e.getCause());
                        System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
                        return null;
                    }
                }).filter(Objects::nonNull)
                .filter(pair -> pair.first != null || pair.second != null)
                .collect(Collectors.toList());

        for (Pair error: newProgramList)
            if (error.second != null)
                throw error.second;
        programStates.addAll(newProgramList.stream().map(pair -> pair.first).collect(Collectors.toList()));

        programStates.forEach(programState -> {
            try {
                repository.logPrgStateExec(programState);
            } catch (IOException | MyException e) {
                System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
            }
        });
        repository.setPrgList(programStates);
    }


    public void conservativeGarbageCollector(List<PrgState> programStates) {
        List<Integer> symTableAddresses = Objects.requireNonNull(programStates.stream()
                        .map(p -> getAddrFromSymTable(p.getSymTable().values()))
                        .map(Collection::stream)
                        .reduce(Stream::concat).orElse(null))
                .collect(Collectors.toList());
        programStates.forEach(p -> {
            p.getHeap().setContent((HashMap<Integer, Value>) safeGarbageCollector(symTableAddresses, getAddrFromHeap(p.getHeap().getContent().values()), p.getHeap().getContent()));
        });
    }

    public void oneStep() throws InterruptedException, MyException {
        executor = Executors.newFixedThreadPool(2);
        List<PrgState> programStates = removeCompletedPrg(repository.getPrgList());
        oneStepForAllPrg(programStates);
        conservativeGarbageCollector(programStates);
        executor.shutdownNow();
    }

    public void allStep() throws InterruptedException, MyException {
        executor = Executors.newFixedThreadPool(2);
        //remove the completed programs
        List<PrgState> prgList=removeCompletedPrg(repository.getPrgList());
        while(prgList.size() > 0){
            conservativeGarbageCollector(prgList);
            oneStepForAllPrg(prgList);
            //remove the completed programs
            prgList=removeCompletedPrg(repository.getPrgList());
        }
        executor.shutdownNow();
        //HERE the repository still contains at least one Completed Prg
        // and its List<PrgState> is not empty. Note that oneStepForAllPrg calls the method
        //setPrgList of repository in order to change the repository

        // update the repository state
        repository.setPrgList(prgList);
    }

    public List<PrgState> getPrgStates(){
        return this.repository.getPrgList();
    }

    public void setPrgStates(List<PrgState> programStates) {
        this.repository.setPrgList(programStates);
    }

}
