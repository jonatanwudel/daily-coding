import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;

public class Main {
    public static void main(String[] args){
        System.out.println("This program, after entering a number, extracts the digits from it and produces the largest possible number");
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        System.out.println("Your new number is " + maxNumber(number));
    }
    static int maxNumber(int number){
        String[] digits = String.valueOf(number).split("");
        Arrays.sort(digits, Collections.reverseOrder());
        return Integer.valueOf(String.join("", digits));
    }
}
