import java.util.Scanner;

public class EventBadgeReport {
    public static void main(String[] args) {
        //Part1
        Scanner scanner = new Scanner(System.in);
        System.out.print("Participant's First Name: ");
        String name = scanner.nextLine();
        
        //Part2
        String copy = new String(name);
        //copy variable stores a the name variable in a String Object.

        //Part3
        int nameLength = name.length();
        String firstLetter = name.substring(0,1);
        String lastLetter = name.substring(nameLength - 1);

        //Part4
        int tableNumber = (int) (Math.random()*6) + 1;

        //Part5
        double badgeSize = Math.sqrt(81) + Math.pow(2, 2);
        int distance = Math.abs(-12);

        //Part6
        String badge = firstLetter + "-" + lastLetter + "-" + tableNumber;
        badge += "|" + name;

        //Part7
        System.out.println("Orig Name >>> " + name);
        System.out.println("Name Length >>> " + nameLength);
        System.out.println("First Letter >>> " + firstLetter);
        System.out.println("Last Letter >>> " + lastLetter);
        
        System.out.println("Table Number >>> " + tableNumber);
        System.out.println("Badge Size >>> " + badgeSize);
        System.out.println("Distance >>> " + distance);
        System.out.println("(Name == Copy) >>> " + name.equals(copy));

        //Part8
        scanner.close();
        
    }
}

// The program is used to print a detailed report about an Event Badge for a particular person.
