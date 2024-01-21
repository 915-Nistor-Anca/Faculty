
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Polynomial {
    private List<Integer> coefficients;
    private final int degree;

    public Polynomial(List<Integer> coefficients) {
        this.coefficients = coefficients;
        this.degree = coefficients.size() - 1;
    }

    private void createRandomCoefficients(int degree) {
        coefficients = new ArrayList<>();
        var r = new Random();
        for (int i = 0; i <= degree; i++) {
            int randomInt = r.nextInt(10);
            int sign = r.nextBoolean() ? 1 : -1;
            int coefficient = randomInt * sign;
            while (coefficient == 0 && i == degree) { //leading coefficient is not zero
                randomInt = r.nextInt(10);
                sign = r.nextBoolean() ? 1 : -1;
                coefficient = randomInt * sign;
            }
            coefficients.add(coefficient);
        }
    }

    public Polynomial(int degree) {
        this.degree = degree;
        createRandomCoefficients(degree);
    }

    public List<Integer> getCoefficients() {
        return coefficients;
    }

    public int getDegree() {
        return degree;
    }

    @Override
    public String toString() {
        var result = "";
        if (coefficients.get(degree) != 0) {
            result += coefficients.get(degree) + "x^" + degree;
        }
        for (var i = degree - 1; i > 0; --i) {
            if (coefficients.get(i) != 0) {
                if (coefficients.get(i) > 0) {
                    result += " + ";
                }
                else result += " ";
                result += coefficients.get(i) + "x^" + i;
            }
        }
        if (coefficients.get(0) != 0) {
            if (coefficients.get(0) > 0) {
                result += " + ";
            }
            result += coefficients.get(0);
        }
        return result.toString();
    }
}