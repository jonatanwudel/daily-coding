import java.util.Scanner;
public class FibonacciSeries {
    static public void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Hi, this is Fibonacci Series program.");
        System.out.println("How many number of the Fibonacci series do you want to display? ");
        int seriesLength = scanner.nextInt();
        fibonacci(seriesLength);
    }
    static void fibonacci(int seriesLength){
        int x = 0;
        int y = 1;
        for (int i = 1; i <= seriesLength; i++){
            System.out.print(x + " ,");
            int sum = x + y;
            x = y;
            y = sum;
        }

    }
}
