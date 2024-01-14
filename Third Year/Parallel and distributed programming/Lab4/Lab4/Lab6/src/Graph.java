import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Graph {
    private List<Integer> nodes;
    private List<List<Integer>> edges;

    public Graph(List<Integer> nodes, List<List<Integer>> edges) {
        this.nodes = nodes;
        this.edges = edges;
    }

    public Graph(int number_of_nodes) {
        this.nodes = new ArrayList<>();
        for (int i = 0; i < number_of_nodes; i++) {
            this.nodes.add(i);
        }
        createEdges();
    }

    private void createEdges() {
        edges = new ArrayList<>();
        for (var node: nodes) {
            edges.add(new ArrayList<>());
        }

        Random random = new Random();
        var size = Math.pow(nodes.size(), 2);
        for (int i = 0; i < size / 2; i++) {
            var node1 = random.nextInt(nodes.size());
            var node2 = random.nextInt(nodes.size());
            addEdge(node1, node2);
        }
    }

    private void addEdge(int start_node, int end_node) {
        if ((start_node == end_node)||(edges.get(start_node).contains(end_node))) return;
        edges.get(start_node).add(end_node);
    }

    public List<Integer> getNodesFromEdges(int node) {
        return edges.get(node);
    }

    public int size() {
        return nodes.size();
    }

    @Override
    public String toString() {
        String text =  "The nodes are: " + nodes + ".\n";
        for (var node: nodes){
            text += "For node " + node + ", the edges are: ";
            for (var n: edges.get(node)){
                text += "(" + node + ", " + n + ") ";
            }
            text += "\n";
        }
        return text;
    }
}