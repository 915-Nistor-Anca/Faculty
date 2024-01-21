import mpi.MPI;

public class Main {
    static final int polynomial_size = 100;
    static final String implementation = "karatsuba";

    public static void master(Polynomial p1, Polynomial p2, int processes) {
        long time1 = System.nanoTime();
        int length = p1.getSize() / (processes - 1);
        int start;
        int end = 0;
        for (int i = 1; i < processes; i++) {
            start = end;
            end = start + length;
            if (i == processes - 1) {
                end = p1.getSize();
            }
            MPI.COMM_WORLD.Send(new Object[]{p1}, 0, 1, MPI.OBJECT, i, 0);
            MPI.COMM_WORLD.Send(new Object[]{p2}, 0, 1, MPI.OBJECT, i, 0);
            MPI.COMM_WORLD.Send(new int[]{start}, 0, 1, MPI.INT, i, 0);
            MPI.COMM_WORLD.Send(new int[]{end}, 0, 1, MPI.INT, i, 0);
        }
        Object[] results = new Object[processes - 1];
        for (int i = 1; i < processes; i++) {
            MPI.COMM_WORLD.Recv(results, i - 1, 1, MPI.OBJECT, i, 0);
        }
        Polynomial result = PolynomialOperations.getResult(results);
        long time2 = System.nanoTime();
        double duration = (time2 - time1) / 1000000000.0;
        System.out.println("The implementation is "+ implementation + ".\n");
        System.out.println("It took " + duration + " seconds to do the multiplication.");
        System.out.println("p1 * p2 =" + result.toString());
    }

    public static void regularWorker(int me) {
        Object[] p1 = new Object[2];
        Object[] p2 = new Object[2];
        int[] start = new int[1];
        int[] end = new int[1];

        MPI.COMM_WORLD.Recv(p1, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(p2, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(start, 0, 1, MPI.INT, 0, 0);
        MPI.COMM_WORLD.Recv(end, 0, 1, MPI.INT, 0, 0);

        Polynomial pol1 = (Polynomial) p1[0];
        Polynomial pol2 = (Polynomial) p2[0];

        Polynomial result = PolynomialOperations.multiplySequence(pol1, pol2, start[0], end[0]);
        MPI.COMM_WORLD.Send(new Object[]{result}, 0, 1, MPI.OBJECT, 0, 0);
    }

    public static void karatsubaWorker(int me) {
        Object[] p1 = new Object[2];
        Object[] p2 = new Object[2];
        int[] start = new int[1];
        int[] end = new int[1];

        MPI.COMM_WORLD.Recv(p1, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(p2, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(start, 0, 1, MPI.INT, 0, 0);
        MPI.COMM_WORLD.Recv(end, 0, 1, MPI.INT, 0, 0);

        Polynomial pol1 = (Polynomial) p1[0];
        Polynomial pol2 = (Polynomial) p2[0];

        for (int i = 0; i < start[0]; i++) {
            pol1.getCoefficients().set(i, 0);
        }
        for (int j = end[0]; j < pol1.getCoefficients().size(); j++) {
            pol1.getCoefficients().set(j, 0);
        }

        Polynomial result = PolynomialOperations.KaratsubaSequential(pol1, pol2);
        MPI.COMM_WORLD.Send(new Object[]{result}, 0, 1, MPI.OBJECT, 0, 0);
    }

    public static void main(String[] args) {
        MPI.Init(args);
        int me = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        if (me == 0) {
            System.out.println("Master process: \n");
            Polynomial p1 = new Polynomial(polynomial_size);
            p1.createRandomCoefficients();
            Polynomial p2 = new Polynomial(polynomial_size);
            p2.createRandomCoefficients();

            System.out.println("FIRST POLYNOMIAL = " + p1);
            System.out.println("SECOND POLYNOMIAL = " + p2 + "\n");

            master(p1, p2, size);
        } else {
            if (implementation.equalsIgnoreCase("regular")) {
                regularWorker(me);
            }
            else if (implementation.equalsIgnoreCase("karatsuba")) {
                karatsubaWorker(me);
            }
        }
        MPI.Finalize();
    }
}