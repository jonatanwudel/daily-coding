import java.util.Random;
import javax.swing.JOptionPane;
public class GuessingGame {

	public static void main(String[] args) {
		Random random = new Random();
		int userAnswer = 0;
		int computerNumber = random.nextInt(100) + 1;
		int count = 1;
		System.out.println("Devloper mode, compouter number is: " + computerNumber);
		
		while (userAnswer != computerNumber) {
			String response = JOptionPane.showInputDialog(null, "Guess number between 1 and 100");
			userAnswer = Integer.parseInt(response);
			JOptionPane.showMessageDialog(null, checkGuess(userAnswer, computerNumber, count));
			count++;
			
		}
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
