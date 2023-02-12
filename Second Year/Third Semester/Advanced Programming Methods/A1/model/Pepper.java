package model;

public class Pepper implements IVegetable {
    private float weight;
    public Pepper(float weight) {this.weight = weight;}
    public String toString() { return "Pepper, weight = " + this.weight;}

    public boolean solve(float weight){
        if (this.weight > weight) return true;
        return false;
    }
}
