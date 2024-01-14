import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        Graph graph = new Graph(8);
        System.out.println("RANDOM GRAPH INFORMATION:");
        System.out.println(graph);
        HamiltonianCycle search_for_hamiltonian_cycle = new HamiltonianCycle(graph);

        System.out.println("Start searching for a cycle in the random graph...");
        var starting_time = System.nanoTime();
        search_for_hamiltonian_cycle.startSearching();
        var ending_time = System.nanoTime();
        System.out.println("Time: " + ((double) ending_time - (double) starting_time) / 1_000_000_000.0 + "s");
        System.out.println("Stopped searching for a cycle in the random graph.\n\n\n\n");

        Graph graph_containing_hamiltonian_cycle = new Graph(
                new ArrayList<>(List.of(0, 1, 2, 3, 4)),
                new ArrayList<>(List.of(
                                new ArrayList<>(List.of(1)),
                                new ArrayList<>(List.of(2, 3)),
                                new ArrayList<>(List.of(4)),
                                new ArrayList<>(List.of(0)),
                                new ArrayList<>(List.of(1, 3, 4))))
        );

        System.out.println("GIVEN GRAPH INFORMATION:");
        System.out.println(graph_containing_hamiltonian_cycle);
        System.out.println("Start searching for a cycle in the given graph...");
        starting_time = System.nanoTime();
        search_for_hamiltonian_cycle = new HamiltonianCycle(graph_containing_hamiltonian_cycle);
        search_for_hamiltonian_cycle.startSearching();
        ending_time = System.nanoTime();
        System.out.println("Time: " + ((double) ending_time - (double) starting_time) / 1_000_000_000.0 + "s");
        System.out.println("Stopped searching for a cycle in the given graph.");


    }
}