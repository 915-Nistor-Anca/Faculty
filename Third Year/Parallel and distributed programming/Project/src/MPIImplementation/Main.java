package MPIImplementation;

import mpi.MPI;

public class Main {
    public static void main(String[] args) {
        MPI.Init(args);

        int rank = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        Graph graph2 = new Graph(100);;
        Colours colours2 = new Colours(5);
        colours2.addColor(0, "red");
        colours2.addColor(1, "green");
        colours2.addColor(2, "blue");
        colours2.addColor(3, "yellow");
        colours2.addColor(4, "pink");

        if (rank==0){
            System.out.println("This is the main process");

            try{
                long time1 = System.nanoTime();

                System.out.println(GraphColouring.colourGraphMain(size,graph2, colours2));
                long time2 = System.nanoTime();

                double duration = (time2 - time1) / 1000000000.0;
                System.out.println("It took " + duration + " seconds.");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        else {
            System.out.println("The number of the process is "+ rank);

            int colorsNumber = colours2.getNumberOfColours();

            GraphColouring.colourGraphChild(rank, size, graph2, colorsNumber);
        }
        MPI.Finalize();

    }
}
