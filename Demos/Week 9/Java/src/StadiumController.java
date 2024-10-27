
// import javafx.beans.property.SimpleStringProperty;
// import javafx.beans.property.StringProperty;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class StadiumController {
    private Stadium stadium = new Stadium();

    public final Stadium getStadium() {
        return stadium;
    }

    @FXML
    private TextField sellTf;

    // Method to set the sell amount in the TextField
    private void setAmount(int amount) {
        sellTf.setText("" + amount);
    }

    // Method to handle the sell action
    @FXML
    public void handleSell() {
        int amount = Integer.parseInt(sellTf.getText());
        stadium.getGroup().sell(amount);
        setAmount(0); // Clear the input after the sell action
    }
}
