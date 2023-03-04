package com.example.a7gui;

import controller.Controller;
import exception.MyException;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleObjectProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import model.other.MyIDictionary;
import model.other.MyIHeap;
import model.other.MyISemaphoreTable;
import model.programstate.PrgState;
import model.statement.IStmt;
import model.value.Value;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


public class MainWindowController {
    private Controller controller;

    @FXML
    private TextField NrPrgStatesTextField;

    @FXML
    private TableView<Pair<Integer, Value>> HeapTableView;

    @FXML
    private TableColumn<Pair<Integer, Value>, Integer> HTAddressTableColumn;

    @FXML
    private TableColumn<Pair<Integer, Value>, String> HTValueTableColumn;

    @FXML
    private ListView<String> OutListView;

    @FXML
    private ListView<String> FileTableListView;

    @FXML
    private ListView<Integer> PrgStateIdentifiersListView;

    @FXML
    private TableView<Pair<String, Value>> SymTableView;

    @FXML
    private TableColumn<Pair<String, Value>, String> STVarNameTableColumn;

    @FXML
    private TableColumn<Pair<String, Value>, String> STValueTableColumn;

    @FXML
    private ListView<String> ExeStackListView;

    @FXML
    private Button RunOneStepButton;

    @FXML
    private TableView<Map.Entry<Integer, javafx.util.Pair<Integer, List<Integer>>>> SemaphoreTable;

    @FXML
    private TableColumn<Map.Entry<Integer, javafx.util.Pair<Integer, List<Integer>>>, Integer> IndexColumn;

    @FXML
    private TableColumn<Map.Entry<Integer, javafx.util.Pair<Integer, List<Integer>>>, Integer> ValueColumn;

    @FXML
    private TableColumn<Map.Entry<Integer, javafx.util.Pair<Integer, List<Integer>>>, List<Integer>> ListColumn;


    public void setController(Controller controller) {
        this.controller = controller;
        populate();
    }

    @FXML
    public void initialize() {
        PrgStateIdentifiersListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
        HTAddressTableColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().first).asObject());
        HTValueTableColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));
        STVarNameTableColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().first));
        STValueTableColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));

        IndexColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        ValueColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getValue().getKey()).asObject());
        ListColumn.setCellValueFactory(p -> new SimpleObjectProperty<>(p.getValue().getValue().getValue()));

    }

    private PrgState getCurrentProgramState() {
        if (controller.getPrgStates().size() == 0)
            return null;
        else {
            int currentId = PrgStateIdentifiersListView.getSelectionModel().getSelectedIndex();
            if (currentId == -1)
                return controller.getPrgStates().get(0);
            else
                return controller.getPrgStates().get(currentId);
        }
    }

    private void populate() {
        populateHeapTableView();
        populateOutputListView();
        populateFileTableListView();
        populateProgramStateIdentifiersListView();
        populateSymbolTableView();
        populateExecutionStackListView();

        populateSemaphoreTableView();
    }

    private void populateSemaphoreTableView() {
        PrgState programState = getCurrentProgramState();
        MyISemaphoreTable semaphoreTable = Objects.requireNonNull(programState).getSemaphoreTable();
        List<Map.Entry<Integer, javafx.util.Pair<Integer, List<Integer>>>> semaphoreList = new ArrayList<>();
        for (Map.Entry<Integer, javafx.util.Pair<Integer, List<Integer>>> entry: semaphoreTable.getSemaphoreTable().entrySet()) {
            semaphoreList.add(entry);
        }
        SemaphoreTable.setItems(FXCollections.observableArrayList(semaphoreList));
        SemaphoreTable.refresh();
    }

    @FXML
    private void changeProgramState(MouseEvent event) {
        populateExecutionStackListView();
        populateSymbolTableView();
    }

    private void populateNumberOfProgramStatesTextField() {
        List<PrgState> programStates = controller.getPrgStates();
        NrPrgStatesTextField.setText(String.valueOf(programStates.size()));
    }

    private void populateHeapTableView() {
        PrgState programState = getCurrentProgramState();
        MyIHeap heap = Objects.requireNonNull(programState).getHeap();
        ArrayList<Pair<Integer, Value>> heapEntries = new ArrayList<>();
        for(Map.Entry<Integer, Value> entry: heap.getContent().entrySet()) {
            heapEntries.add(new Pair<>(entry.getKey(), entry.getValue()));
        }
        HeapTableView.setItems(FXCollections.observableArrayList(heapEntries));
    }

    private void populateOutputListView() {
        PrgState programState = getCurrentProgramState();
        List<String> output = new ArrayList<>();
        List<Value> outputList = Objects.requireNonNull(programState).getOut().getList();
        int index;
        for (index = 0; index < outputList.size(); index++){
            output.add(outputList.get(index).toString());
        }
        OutListView.setItems(FXCollections.observableArrayList(output));
    }

    private void populateFileTableListView() {
        PrgState programState = getCurrentProgramState();
        List<String> files = new ArrayList<>(Objects.requireNonNull(programState).getFileTable().getContent().keySet());
        FileTableListView.setItems(FXCollections.observableList(files));
    }

    private void populateProgramStateIdentifiersListView() {
        List<PrgState> programStates = controller.getPrgStates();
        List<Integer> idList = programStates.stream().map(PrgState::getId).collect(Collectors.toList());
        PrgStateIdentifiersListView.setItems(FXCollections.observableList(idList));
        populateNumberOfProgramStatesTextField();
    }

    private void populateSymbolTableView() {
        PrgState programState = getCurrentProgramState();
        MyIDictionary<String, Value> symbolTable = Objects.requireNonNull(programState).getSymTable();
        ArrayList<Pair<String, Value>> symbolTableEntries = new ArrayList<>();
        for (Map.Entry<String, Value> entry: symbolTable.getContent().entrySet()) {
            symbolTableEntries.add(new Pair<>(entry.getKey(), entry.getValue()));
        }
        SymTableView.setItems(FXCollections.observableArrayList(symbolTableEntries));
    }

    private void populateExecutionStackListView() {
        PrgState programState = getCurrentProgramState();
        List<String> executionStackToString = new ArrayList<>();
        if (programState != null)
            for (IStmt statement: programState.getExeStack().getReversed()) {
                executionStackToString.add(statement.toString());
            }
        ExeStackListView.setItems(FXCollections.observableList(executionStackToString));
    }

    @FXML
    private void runOneStep(MouseEvent mouseEvent) {
        if (controller != null) {
            try {
                List<PrgState> programStates = Objects.requireNonNull(controller.getPrgStates());
                if (programStates.size() > 0) {
                    controller.oneStep();
                    populate();
                    programStates = controller.removeCompletedPrg(controller.getPrgStates());
                    controller.setPrgStates(programStates);
                    populateProgramStateIdentifiersListView();
                } else {
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setTitle("Error!");
                    alert.setHeaderText("An error has occured!");
                    alert.setContentText("There is nothing left to execute!");
                    alert.showAndWait();
                }
            } catch (MyException | InterruptedException e) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Execution error!");
                alert.setHeaderText("An execution error has occured!");
                alert.setContentText(e.getMessage());
                alert.showAndWait();
            }
        } else {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error!");
            alert.setHeaderText("An error has occured!");
            alert.setContentText("No program selected!");
            alert.showAndWait();
        }
    }
}