import java.util.Scanner; // Importe a classe Scanner do pacote util do Java

public class LerDados{
    
    public static void main ( String[] args ){
        
        Scanner teclado = new Scanner(System.in); // Inicialize uma variável do tipo Scanner
        int inteiro;
        String texto;
        float real;
        double real2;

        // Recebendo um inteiro
        System.out.println(" Para receber um inteiro, você utiliza o nextInt():");
        inteiro = Integer.parseInt(teclado.nextLine());
        System.out.println(" Você digitou: "+inteiro);  

        // Recebendo uma string
        System.out.println(" Para receber um texto, você utiliza o next(), ou nextLine(); o primeiro corresponde a uma única palavra:");
        texto = teclado.nextLine();
        System.out.println(" Você digitou: "+texto);
        
        // Recebendo Double ou float
        System.out.println(" Para receber um double ou float, você utiliza o nextDouble() ou nextFloat():");
        real = Float.parseFloat(teclado.nextFloat());
        System.out.println(" Você digitou: "+real);
        
        teclado.close();

        /*
        float numF = sc.nextFloat();
        int num1 = sc.nextInt();
        byte byte1 = sc.nextByte();
        long lg1 = sc.nextLong();
        boolean b1 = sc.nextBoolean();
        double num2 = sc.nextDouble();
        String nome = sc.nextLine();
        */
    }
}
