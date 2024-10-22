import javafx.stage.*;
// import javafx.scene.*;
// import javafx.scene.control.*;
// import javafx.scene.layout.*;
// import javafx.scene.text.*;
// import javafx.geometry.*;
// import javafx.fxml.*;
import au.edu.uts.ap.javafx.*;
import model.Stadium;
import javafx.application.Application;

public class StadiumApplication extends Application {
	public static void main(String[] args) {
		launch(args);
	}

	@Override
	public void start(Stage stage) throws Exception {
		Stadium stadium = new Stadium(); // create model
		ViewLoader.showStage(stadium, "/view/stadium.fxml", "Stadium", stage); // pass model and other parameters to
																				// ViewLoader
		// includes initial stage and absolute refference to view
	}
}
