
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class PolynomialOperations {
    public static Polynomial add(Polynomial p1, Polynomial p2) {
        int minimum_degree = Math.min(p1.getDegree(), p2.getDegree());
        int maximum_degree = Math.max(p1.getDegree(), p2.getDegree());
        List<Integer> result_added_coefficients = new ArrayList<>(maximum_degree + 1);

        for (int i = 0; i <= minimum_degree; i++) {
            result_added_coefficients.add(p1.getCoefficients().get(i) + p2.getCoefficients().get(i));
        }

        if (minimum_degree != maximum_degree) {
            if (maximum_degree == p1.getDegree()) {
                for (int i = minimum_degree + 1; i <= maximum_degree; i++) {
                    result_added_coefficients.add(p1.getCoefficients().get(i));
                }
            } else {
                for (int i = minimum_degree + 1; i <= maximum_degree; i++) {
                    result_added_coefficients.add(p2.getCoefficients().get(i));
                }
            }
        }
        return new Polynomial(result_added_coefficients);
    }

    public static Polynomial subtract(Polynomial p1, Polynomial p2) {
        int minimum_degree = Math.min(p1.getDegree(), p2.getDegree());
        int maximum_degree = Math.max(p1.getDegree(), p2.getDegree());
        List<Integer> result_substracted_coefficients = new ArrayList<>(maximum_degree + 1);

        for (int i = 0; i <= minimum_degree; i++) {
            result_substracted_coefficients.add(p1.getCoefficients().get(i) - p2.getCoefficients().get(i));
        }

        if (minimum_degree != maximum_degree) {
            if (maximum_degree == p1.getDegree()) {
                for (int i = minimum_degree + 1; i <= maximum_degree; i++) {
                    result_substracted_coefficients.add(p1.getCoefficients().get(i));
                }
            } else {
                for (int i = minimum_degree + 1; i <= maximum_degree; i++) {
                    result_substracted_coefficients.add(-p2.getCoefficients().get(i));
                }
            }
        }

        int i = result_substracted_coefficients.size() - 1;
        if (i > 0 && result_substracted_coefficients.get(i) == 0) {
            result_substracted_coefficients.remove(i);
        }
        return new Polynomial(result_substracted_coefficients);
    }

    public static Polynomial addZeros(Polynomial p, int offset) {
        List<Integer> coefficients = IntStream.range(0, offset).mapToObj(i -> 0).collect(Collectors.toList());
        coefficients.addAll(p.getCoefficients());
        return new Polynomial(coefficients);
    }
}