package model;

import java.util.Random;

import static java.lang.Math.round;

public class Eggplant implements IVegetable {
    private float weight;
    public Eggplant(float weight) {this.weight = weight;}
    public String toString() { return "Eggplant, weight = " + this.weight;}

    public boolean solve(float weight){
        if (this.weight > weight) return true;
        return false;
    }
}
