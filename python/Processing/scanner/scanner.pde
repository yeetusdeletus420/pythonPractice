import java.util.Scanner;
System.out.println("Your name Jeff? ");
Scanner Name = new Scanner(System.in);


// what the hell happened here ... //


String answer = (Name.nextLine()).toUpperCase();
if (answer == "Y") {
  System.out.println("Your name jeff.");
}
else if (answer == "N") {
  System.out.println("Your name not jeff.");
}
