import java.text.*;
import javafx.beans.property.*;
import javafx.beans.binding.Bindings;

public class Group {
    private String name;
    private int capacity;
    private double price;
    private IntegerProperty sold = new SimpleIntegerProperty();
    private DoubleProperty income = new SimpleDoubleProperty();
    private IntegerProperty left = new SimpleIntegerProperty();

    public Group(String name, int capacity, double price) {
        this.name = name;
        this.capacity = capacity;
        this.price = price;
        sold.set(0);

        // Bind the income to sold * price
        income.bind(sold.multiply(price));
        // Bind left to capacity - sold
        left.bind(Bindings.subtract(capacity, sold));
    }

    public final String getName() {
        return name;
    }

    public final int getCapacity() {
        return capacity;
    }

    public final double getPrice() {
        return price;
    }

    public final ReadOnlyIntegerProperty soldProperty() {
        return sold;
    }

    public final int getSold() {
        return sold.get();
    }

    public final ReadOnlyDoubleProperty incomeProperty() {
        return income;
    }

    public final double getIncome() {
        return income.get();
    }

    public final ReadOnlyIntegerProperty leftProperty() {
        return left;
    }

    public final int getLeft() {
        return left.get();
    }

    public void sell(int number) {
        sold.set(sold.get() + number);
    }

    @Override
    public String toString() {
        return getLeft() + " " + name + " seats @ $" + formatted(price);
    }

    private String formatted(double value) {
        DecimalFormat df = new DecimalFormat("#.00");
        return df.format(value);
    }
}
