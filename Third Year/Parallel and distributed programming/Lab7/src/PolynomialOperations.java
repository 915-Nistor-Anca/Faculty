import java.util.ArrayList;
import java.util.List;

public class PolynomialOperations {
    public static Polynomial add(Polynomial p1, Polynomial p2) {
        int minDegree = Math.min(p1.getDegree(), p2.getDegree());
        int maxDegree = Math.max(p1.getDegree(), p2.getDegree());
        Polynomial result = new Polynomial(maxDegree + 1);
        for (int i = 0; i <= minDegree; i++) {
            result.getCoefficients().set(i, p1.getCoefficients().get(i) + p2.getCoefficients().get(i));
        }
        Polynomial remaining;
        if (p1.getDegree() > p2.getDegree()) {
            remaining = p1;
        } else {
            remaining = p2;
        }
        for (int i = minDegree + 1; i <= maxDegree; i++) {
            result.getCoefficients().set(i, remaining.getCoefficients().get(i));
        }
        return result;
    }

    public static Polynomial subtract(Polynomial p1, Polynomial p2) {
        int minDegree = Math.min(p1.getDegree(), p2.getDegree());
        int maxDegree = Math.max(p1.getDegree(), p2.getDegree());
        Polynomial result = new Polynomial(maxDegree + 1);
        for (int i = 0; i <= minDegree; i++) {
            result.getCoefficients().set(i, p1.getCoefficients().get(i) - p2.getCoefficients().get(i));
        }
        Polynomial remaining;
        if (p1.getDegree() > p2.getDegree()) {
            remaining = p1;
        } else {
            remaining = p2;
        }
        for (int i = minDegree + 1; i <= maxDegree; i++) {
            result.getCoefficients().set(i, remaining.getCoefficients().get(i));
        }

        int i = result.getCoefficients().size() - 1;
        while (i > 0 && result.getCoefficients().get(i) == 0) {
            result.getCoefficients().remove(i);
            i--;
        }
        return result;
    }

    public static Polynomial addZeros(Polynomial p, int offset) {
        List<Integer> coefficients = new ArrayList<>();
        for (int i = 0; i < offset; i++) {
            coefficients.add(0);
        }
        coefficients.addAll(p.getCoefficients());
        return new Polynomial(coefficients);
    }
    public static Polynomial getResult(Object[] polynomials) {
        int size = ((Polynomial) polynomials[0]).getDegree();
        Polynomial result = new Polynomial(size + 1);
        for (Object polynomial: polynomials) {
            result = add(result, (Polynomial) polynomial);
        }
        return result;
    }

    public static Polynomial multiplySequence(Polynomial p1, Polynomial p2, int start, int end) {
        Polynomial result = new Polynomial(2 * p1.getDegree() + 1);
        for (int i = start; i < end; i++) {
            for (int j = 0; j < p2.getCoefficients().size(); j++) {
                result.getCoefficients().set(i + j, result.getCoefficients().get(i + j) + p1.getCoefficients().get(i) * p2.getCoefficients().get(j));
            }
        }
        return result;
    }

    public static Polynomial regularSequential(Polynomial p1, Polynomial p2) {
        Polynomial result = new Polynomial(p1.getDegree() + p2.getDegree() + 1);
        for (int i = 0; i < p1.getCoefficients().size(); i++) {
            for (int j = 0; j < p2.getCoefficients().size(); j++) {
                result.getCoefficients().set(i + j, result.getCoefficients().get(i + j) + p1.getCoefficients().get(i) * p2.getCoefficients().get(j));
            }
        }
        return result;
    }

    public static Polynomial KaratsubaSequential(Polynomial p1, Polynomial p2) {
        if (p1.getDegree() < 2 || p2.getDegree() < 2) {
            return regularSequential(p1, p2);
        }

        int m = Math.min(p1.getDegree(), p2.getDegree()) / 2;
        Polynomial a = new Polynomial(p1.getCoefficients().subList(0, m));
        Polynomial b = new Polynomial(p1.getCoefficients().subList(m, p1.getSize()));
        Polynomial c = new Polynomial(p2.getCoefficients().subList(0, m));
        Polynomial d = new Polynomial(p2.getCoefficients().subList(m, p2.getSize()));
        Polynomial poly1 = KaratsubaSequential(a, c);
        Polynomial poly2 = KaratsubaSequential(add(a, b), add(c, d));
        Polynomial poly3 = KaratsubaSequential(b, d);
        Polynomial r1 = addZeros(poly3, 2 * m);
        Polynomial r2 = addZeros(subtract(subtract(poly2, poly3), poly1), m);
        return add(add(r1, r2), poly1);
    }
}