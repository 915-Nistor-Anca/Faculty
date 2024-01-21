import java.util.concurrent.*;

public class KaratsubaAlgorithmParallelForm {
    private static final int number_of_threads = 5;
    private static final int maximum_depth = 4;

    public static Polynomial multiply(Polynomial p1, Polynomial p2, int current_depth) throws InterruptedException, ExecutionException {
        if (current_depth > maximum_depth) {
            return KaratsubaAlgorithmSequencialForm.multiply(p1, p2);
        }

        if (p1.getDegree() < 2 || p2.getDegree() < 2) {
            return KaratsubaAlgorithmSequencialForm.multiply(p1, p2);
        }

        int len = Math.max(p1.getDegree(), p2.getDegree()) / 2;
        Polynomial a = new Polynomial(p1.getCoefficients().subList(0, len));
        Polynomial b = new Polynomial(p1.getCoefficients().subList(len, p1.getCoefficients().size()));
        Polynomial c = new Polynomial(p2.getCoefficients().subList(0, len));
        Polynomial d = new Polynomial(p2.getCoefficients().subList(len, p2.getCoefficients().size()));

        ExecutorService executor = Executors.newFixedThreadPool(number_of_threads);
        Polynomial poly1 = executor.submit(() -> multiply(a, c, current_depth + 1)).get();
        Polynomial poly2 = executor.submit(() -> multiply(PolynomialOperations.add(a, b), PolynomialOperations.add(c, d), current_depth + 1)).get();
        Polynomial poly3 = executor.submit(() -> multiply(b, d, current_depth + 1)).get();

        executor.shutdown();

        executor.awaitTermination(6, TimeUnit.SECONDS);

        Polynomial r1 = PolynomialOperations.addZeros(poly3, 2 * len);
        Polynomial r2 = PolynomialOperations.addZeros(PolynomialOperations.subtract(PolynomialOperations.subtract(poly2, poly3), poly1), len);
        return PolynomialOperations.add(PolynomialOperations.add(r1, r2), poly1);
    }
}
