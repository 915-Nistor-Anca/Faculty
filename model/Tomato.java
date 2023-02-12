package model;

public class Tomato implements IVegetable {
    private float weight;
    public Tomato(float weight) {this.weight = weight;}
    public String toString() { return "Tomato, weight = " + this.weight;}

    public boolean solve(float weight){
        if (this.weight > weight) return true;
        return false;
    }
}
