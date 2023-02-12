package view;

import controller.Controller;
import exception.MyException;

public class RunExample extends Command {
    private Controller ctr;

    public RunExample(String key, String desc, Controller ctr) {
        super(key, desc);
        this.ctr = ctr;
    }

    @Override
    public void execute() {
        try {
            ctr.allStep();
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        } catch (MyException e) {
            throw new RuntimeException(e);
        }
    }
}

