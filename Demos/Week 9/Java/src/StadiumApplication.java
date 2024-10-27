import javafx.stage.*;
import javafx.scene.*;
// import javafx.scene.control.*;
// import javafx.scene.layout.*;
// import javafx.scene.text.*;
// import javafx.geometry.*;
import javafx.fxml.*;
import javafx.application.*;

public class StadiumApplication extends Application {
	public static void main(String[] args) {
		launch(args);
	}

	@Override
	public void start(Stage stage) throws Exception {
		FXMLLoader loader = new FXMLLoader(getClass().getResource("stadium.fxml"));
		Parent root = loader.load();
		stage.setScene(new Scene(root));
		stage.show();
	}
}