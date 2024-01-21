import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Polynomial implements Serializable {
    private List<Integer> coefficients;

    public Polynomial(List<Integer> coefficients) {
        this.coefficients = coefficients;
    }

    public Polynomial(int size) {
        this.coefficients = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            this.coefficients.add(0);
        }
    }

    public void createRandomCoefficients() {
        Random random = new Random();
        for (int i = 0; i <= getDegree(); i++) {
            var coefficient = random.nextInt(10) * (random.nextBoolean() ? 1 : -1);
            while (coefficient == 0 && i == this.coefficients.size() - 1) {
                coefficient = random.nextInt(10) * (random.nextBoolean() ? 1 : -1);
            }
            this.coefficients.set(i, coefficient);
        }
    }

    public int getDegree() {
        return this.coefficients.size() - 1;
    }

    public int getSize() {
        return this.coefficients.size();
    }

    public List<Integer> getCoefficients() {
        return this.coefficients;
    }

    @Override
    public String toString() {
        var result = "";
        int degree = getDegree();
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