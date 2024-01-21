package MPIImplementation;

import java.util.HashMap;
import java.util.Map;

public class Colours {
    private int number_of_colours;
    private Map<Integer,String> colours;

    public Colours(int n){
        this.number_of_colours = n;

        colours = new HashMap<>();
        for (int code=0; code< n ; code++){
            colours.put(code, "");
        }
    }

    public void addColor( int code, String color){
        colours.put(code, color);
    }

    public int getNumberOfColours() { return number_of_colours; }

    public String visualCheck(int[] codes, Graph graph_to_colour){
        String text = "The edges of the graph represented by the colours of the nodes:\n";
        for(int i =0;i < codes.length;i++){
            text += "Node " + i + " has the colour " + colours.get(codes[i]).toUpperCase() + ".\n";
            text += "For node " + i + ", the edges are: ";
            for (var n: graph_to_colour.getNodesFromEdges(i)){
                text += "(" + colours.get(codes[i]).toUpperCase() + ", " + colours.get(codes[n]).toUpperCase() + ") ";
            }
            text += "\n\n";
        }
        return text;
    }

}