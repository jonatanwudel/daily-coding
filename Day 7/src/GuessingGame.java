import java.util.Random;
import java.util.Scanner;
public class GuessingGame {

	public static void main(String[] args) {
		Random random = new Random();
		Scanner scanner = new Scanner(System.in);
		int userAnswer = 0;
		int computerNumber = random.nextInt(100) + 1;
		int count = 1;
		System.out.println("Devloper mode, compouter number is: " + computerNumber);
		
		while (userAnswer != computerNumber) {
			System.out.println("Guess number between 1 and 100");
			String response = scanner.next();
			userAnswer = Integer.parseInt(response);
			System.out.println(checkGuess(userAnswer, computerNumber, count));
			count++;
			
		}
		scanner.close();
	}
	
	public static String checkGuess(int userAnswer, int computerNumber, int count) {
		if (userAnswer <= 0 || userAnswer > 100) {
			return "Invalid number";
		}
		else if (userAnswer == computerNumber) {
			return "Good Job this number is correct, try number: " + count;
		}
		else if (userAnswer < computerNumber) {
			return "Your number is too low, try number: " + count;
		}
		else if (userAnswer > computerNumber) {
			return "Your number is too high, try number: " + count;
		}
		else {
			return "Error";
		}
	}
}
