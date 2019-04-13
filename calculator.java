import java.util.Scanner;
import javax.swing.JOptionPane;

public class javaCalculator 
{

    public static void main(String[] args) 
    {
        int numA;
        int numB;
        String operation;


        Scanner input = new Scanner(System.in);

        System.out.println("please enter the first number");
        numA = input.nextInt();

        System.out.println("please enter the second number");
        numB = input.nextInt();

        Scanner op = new Scanner(System.in);

        System.out.println("Please enter operation");
        operation = op.next();

        if (operation == "+");
        {
            System.out.println("your answer is" + (numA + numB));
        }
        if  (operation == "-");
        {
            System.out.println("your answer is" + (numA - numB));
        }

        if (operation == "/");
        {
            System.out.println("your answer is" + (numA / numB));
        }
        if (operation == "*")
        {
            System.out.println("your answer is" + (numA * numB));
        }


    }
}