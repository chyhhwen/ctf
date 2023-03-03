import java.util.Scanner;

public class Main
{
    public Main()
    {
        int size = 23;
        int math = 41;
        Scanner input = new Scanner(System.in);
        int put[] = new int[size];
        char ans[] = new char[size];
        for(int i=0;i<size;i++)
        {
            put[i] = input.nextInt();
            if(put[i] % math < 26)
            {
                ans[i] = (char)((put[i] % math)+65);
            }
            else if(put[i] % math < 36)
            {
                ans[i] = (char)((put[i] % math)+22);
            }
            else
            {
                ans[i] = '_';
            }
        }
        for(int i=0;i<size;i++)
        {
            System.out.print(ans[i]);
        }
    }
    public static void main(String[] args)
    {
        new Main();
    }
}