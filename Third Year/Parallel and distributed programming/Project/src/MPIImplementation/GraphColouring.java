package MPIImplementation;

import mpi.MPI;

import java.util.Arrays;

public class GraphColouring {
    public static String colourGraphMain(int mpiSize, Graph graph_to_colour, Colours available_colours) throws Exception {

        int colorsNumber = available_colours.getNumberOfColours();
        int[] codes = findSolution(0,graph_to_colour,colorsNumber, new int[graph_to_colour.size()], 0, mpiSize, 0);

        if (codes[0] == -1){
            throw new Exception("There is no solution!");
        }

        return available_colours.visualCheck(codes, graph_to_colour);
    }
    private static int[] findSolution(int node_id, Graph graph_to_colour, int colorsNumber, int[] codes, int mpi_rank, int mpi_size, int power){
        int nodesNumber = graph_to_colour.size();

        if(!colorIsValid(node_id,codes, graph_to_colour)){
            int[] array = new int[nodesNumber];
            Arrays.fill(array, -1);
            return array;
        }

        if(node_id + 1 == graph_to_colour.size()){
            return codes;
        }

        int coefficient = (int) Math.pow(colorsNumber,power);
        int colorCode = 0;
        int destination = mpi_rank + coefficient * (colorCode + 1);

        while (colorCode + 1 < colorsNumber && destination < mpi_size){
            colorCode++;
            destination = mpi_rank+coefficient*(colorCode + 1 );
        }

        int next_node = node_id +1;
        int next_power = power + 1;

        for (int currentColorCode = 1; currentColorCode < colorCode; currentColorCode++){
            destination = mpi_rank + coefficient * currentColorCode;

            int[] data = new int[]{mpi_rank, next_node, next_power};
            MPI.COMM_WORLD.Send(data,0,data.length,MPI.INT,destination,0);

            int[] nextColorCodes = Arrays.copyOf(codes,codes.length);
            nextColorCodes[next_node] = currentColorCode;

            MPI.COMM_WORLD.Send(nextColorCodes, 0, nodesNumber, MPI.INT, destination, 0);
        }

        int[] nextColorCodes = Arrays.copyOf(codes,codes.length);
        nextColorCodes[next_node] = 0;

        int[] result = findSolution(next_node, graph_to_colour, colorsNumber, nextColorCodes, mpi_rank, mpi_size, next_power);
        if(result[0] != -1){
            return result;
        }

        for (int currentColorCode = 1; currentColorCode < colorCode; currentColorCode++){
            destination = mpi_rank + coefficient * currentColorCode;
            result = new int[nodesNumber];

            MPI.COMM_WORLD.Recv(result,0,nodesNumber,MPI.INT,destination,MPI.ANY_TAG);
            if(result[0] != -1){
                return result;
            }
        }

        for (int currentColorCode = colorCode ; currentColorCode < colorsNumber; currentColorCode++){
            nextColorCodes = Arrays.copyOf(codes,codes.length);
            nextColorCodes[next_node] = currentColorCode;

            result = findSolution(next_node, graph_to_colour, colorsNumber, nextColorCodes, mpi_rank, mpi_size, next_power);

            if(result[0] != -1){
                return result;
            }
        }

        return result;

    }

    public static void colourGraphChild(int mpi_rank, int mpi_size, Graph graph, int colorsNumber) {
        int nodesNumber = graph.size();

        int[] data = new int[3];
        MPI.COMM_WORLD.Recv(data, 0, data.length, MPI.INT, MPI.ANY_SOURCE, MPI.ANY_TAG);

        int parent = data[0];
        int nodeId = data[1];
        int power = data[2];

        int[] codes = new int[nodesNumber];
        MPI.COMM_WORLD.Recv(codes, 0, nodesNumber, MPI.INT, MPI.ANY_SOURCE, MPI.ANY_TAG);

        int[] result = findSolution(nodeId, graph, colorsNumber, codes, mpi_rank, mpi_size, power);

        MPI.COMM_WORLD.Send(result, 0, nodesNumber, MPI.INT, parent, 0);

    }

    private static boolean colorIsValid(int node, int[] codes, Graph graph){
        for(int current=0; current < node; current++){
            if((graph.getNodesFromEdges(node).contains(current) || graph.getNodesFromEdges(current).contains(node)) && codes[node] == codes[current]){
                return false;
            }
        }
        return true;
    }
}