import java.util.Scanner;

public class reverse
{
    public reverse()
    {
        int size = 23;
        int mod = 41;
        int put[] = new int[size];
        char ans[] = new char[size];
        Scanner input = new Scanner(System.in);
        for(int i=0;i<size;i++)
        {
            put[i] = input.nextInt();
        }
        for(int i=0;i<size;i++)
        {
            for(int j=1;j<=mod;j++)
            {
                if(put[i]*j%mod == 1)
                {
                    if(j < 27)
                    {
                        ans[i] = (char) (j + 64);
                    }
                    else if(j < 37)
                    {
                        ans[i] = (char) (j + 21);
                    }
                    else
                    {
                        ans[i] = '_';
                    }
                }
            }
        }
        for(int i=0;i<size;i++)
        {
            System.out.print(ans[i]);
        }
    }
    public static void main(String[] args)
    {
        new reverse();
    }
}