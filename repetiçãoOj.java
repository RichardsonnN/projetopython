public class repetiçãoOj extends Thread{
    @Override
    public void run() {
        for (int contador1 = 1; contador1 <= 10; contador1 ++){
            System.out.println(contador1);
        }
        for (int contador2 = 1; contador2 <= 10; contador2 ++){
            System.out.println(contador2);
        }
    super.start();
    }
}

/*    public static void main (String[] args ){





        for (int italo = 1; italo <= 10; italo ++){
            System.out.println(italo);
        }
        for (int contador = 1; contador <= 10; contador++){
            System.out.println(contador);
        }
    }
    
}*/
