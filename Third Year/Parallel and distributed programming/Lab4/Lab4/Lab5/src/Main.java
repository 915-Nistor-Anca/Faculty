import java.util.concurrent.ExecutionException;

public class Main {
    private static String form = "parallel";
    private static String algorithm = "karatsuba";

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        Polynomial p1 = new Polynomial(5);
        System.out.println("FIRST POLYNOMIAL = " + p1);
        Polynomial p2 = new Polynomial(3);
        System.out.println("SECOND POLYNOMIAL = " + p2);
        long time1 = System.nanoTime();


        Polynomial result;
        if (form.equals("sequencial")) {
            if (algorithm.equals("regular")) {
                result = RegularAlgorithmSequencialForm.multiply(p1, p2);
            } else {
                result = KaratsubaAlgorithmSequencialForm.multiply(p1, p2);
            }
        }
        else {
            if (algorithm.equals("regular")) {
                result = RegularAlgorithmParallelForm.multiply(p1, p2);
            } else {
                result = KaratsubaAlgorithmParallelForm.multiply(p1, p2, 1);
            }
        }
        System.out.println("p1 * p2 =" + result);


        long time2 = System.nanoTime();
        double duration = ((double) time2 - (double) time1) / 1_000_000_000.0;
        System.out.println("It took " + duration + " seconds to do the multiplication.");
    }
}