import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class HamiltonianCycle {
    public Graph graph;

    public HamiltonianCycle(Graph graph) {
        this.graph = graph;
    }

    public void startSearching() {
        ArrayList<Integer> path = new ArrayList<>();

        try {
            path.add(0);
            search(0, path);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private boolean nodeIsInPath(int node, List<Integer> path) {
        return path.contains(node);
    }

    private void search(int current_node, ArrayList<Integer> path) throws Exception {
        if (graph.getNodesFromEdges(current_node).contains(0) && path.size() == graph.size()) {
            System.out.println("Hamiltonian cycle found: " + path);
            return;
        }

        if (path.size() == graph.size()) return;

        for (int node = 0; node < graph.size(); node++) {
            if (graph.getNodesFromEdges(current_node).contains(node) && !nodeIsInPath(node, path)) {
                path.add(node);
                graph.getNodesFromEdges(current_node).remove(Integer.valueOf(node));

                ThreadPoolExecutor thread_pool_executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(5);
                final int node2 = node;
                final Runnable another_search = () -> {
                    try {
                        search(node2, path);
                    } catch (Exception e) {
                        throw new RuntimeException(e.getMessage());
                    }
                };
                thread_pool_executor.execute(another_search);
                thread_pool_executor.shutdown();
                thread_pool_executor.awaitTermination(50, TimeUnit.SECONDS);

                graph.getNodesFromEdges(current_node).add(node);
                path.remove(path.size() - 1);
            }
        }

    }
}