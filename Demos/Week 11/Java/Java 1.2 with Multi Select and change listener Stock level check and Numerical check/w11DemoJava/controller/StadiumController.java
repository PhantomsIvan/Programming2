package controller;

import javafx.collections.*;
import javafx.event.*;
import javafx.fxml.*;
import javafx.scene.text.*;
import javafx.scene.control.*;
import javafx.stage.*;
import javafx.beans.property.*;
import java.io.*;
import au.edu.uts.ap.javafx.*;
import model.*;

public class StadiumController extends Controller<Stadium> {
    @FXML
    private TableView<Group> groupsTv;

    @FXML
    Button openBtn;

    public final Stadium getStadium() {
        return model;
    }

    private Group getGroup() {
        return groupsTv.getSelectionModel().getSelectedItem();
    }

    @FXML
    private void initialize() {
        openBtn.setDisable(true);
        groupsTv.getSelectionModel().selectedItemProperty().addListener((observable, oldTxt, newTxt) -> {
            openBtn.setDisable(newTxt == null);
        });
        // to implement multiple selection
        groupsTv.getSelectionModel().setSelectionMode(SelectionMode.MULTIPLE);
    }

    @FXML
    private void handleOpen(ActionEvent event) throws Exception {
        // to implement multiple selection
        // 1 create a list of selected items "Oversable list"
        // 2 iterate through the list and show the stage

        ObservableList<Group> selectedGroups = groupsTv.getSelectionModel().getSelectedItems();

        if (!selectedGroups.isEmpty()) {
            for (Group g : selectedGroups) {
                ViewLoader.showStage(g, "/view/group.fxml", "Group", new Stage());
            }
        }

        // ViewLoader.showStage(getGroup(), "/view/group.fxml", "Stadium", new Stage());
    }

}
