import java.util.*;
class Main{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        
        for(int i=0;i<t;i++)
        {
            String s=sc.next();
            StringBuilder str=new StringBuilder(s);
            for(int k=1;str.length()>=k;k++)
            {
                 System.out.print(str.substring(0,k).charAt(0));
                 if(k!=1)
                     System.out.print(str.substring(0,k).charAt(k-1));
                 str.delete(0,k);
            }
            System.out.println();
        }
    }
}
