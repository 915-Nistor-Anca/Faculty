package com.example.a7gui;


import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.util.Objects;

public class Main extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader selectProgramLoader = new FXMLLoader();
        selectProgramLoader.setLocation(Main.class.getResource("SelectProgramWindow.fxml"));
        Parent selectProgramRoot = selectProgramLoader.load();
        Scene selectProgramScene = new Scene(selectProgramRoot, 800, 400);
        SelectProgramWindowController selectProgramWindowController = selectProgramLoader.getController();
        primaryStage.setScene(selectProgramScene);


        FXMLLoader mainProgramLoader = new FXMLLoader();
        mainProgramLoader.setLocation(Main.class.getResource("MainWindow.fxml"));
        Parent mainWindowRoot = mainProgramLoader.load();
        Scene mainWindowScene = new Scene(mainWindowRoot, 860, 600);
        MainWindowController mainWindowController = mainProgramLoader.getController();
        //
        selectProgramWindowController.setMainWindowController(mainWindowController);
        //
        Stage secondaryStage = new Stage();
        secondaryStage.setScene(mainWindowScene);

        //
        secondaryStage.show();
        primaryStage.show();
    }

}