package diceRollEmulator;
import java.util.Scanner;
import java.util.Random;

public class diceRollEmulator {
	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		Random random = new Random();
		
		System.out.println("Enter number of dice: ");
		int diceNumber = scanner.nextInt();
		
		System.out.println("You rolled: ");
		int totalNumber = 0;
		int randomNumber = 0;
		
		for (int i = 0; i < diceNumber; i++) {
			randomNumber = random.nextInt(6) + 1;
			totalNumber = totalNumber + randomNumber;
			System.out.println(randomNumber);
		}
		
		System.out.println("Total: " + totalNumber);
		scanner.close();
		
	}

}
