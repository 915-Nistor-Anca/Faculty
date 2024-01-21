package ThreadImplementation;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Graph graph = new Graph(100);
        System.out.println("GRAPH INFORMATION:");
        System.out.println(graph);

        List<String> colours = new ArrayList<>();
        colours.add("pink");
        colours.add("red");
        colours.add("green");
        colours.add("blue");
        colours.add("yellow");
        colours.add("orange");
        colours.add("purple");
        System.out.println("The list of colours is " + colours + ".\n");

        long time1 = System.nanoTime();

        GraphColouring graph_colouring = new GraphColouring(graph, colours);
        graph_colouring.colourGraph(10);

        long time2 = System.nanoTime();
        double duration = (time2 - time1) / 1000000000.0;
        System.out.println("It took " + duration + " seconds.");
        System.out.println(graph_colouring);
        System.out.println(graph_colouring.visualCheck());


    }
}