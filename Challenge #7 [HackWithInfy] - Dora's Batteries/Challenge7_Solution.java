import java.util.*;
class Main
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
    int t=sc.nextInt();
    while(t!=0)
    {
      int n=sc.nextInt(),a[]=new int[n],sum=0;
      for(int i=0;i<n;i++)
      {
        a[i]=sc.nextInt();
        sum=sum|a[i];
      }
      int prev=0,cur,p=1;
      Arrays.sort(a);
      for(int i=n-1;i>=0;i--)
      {
        cur=prev|a[i];
        if(cur==sum)
        {
          System.out.println(p);
          break;
        }
        else if(prev!=cur)
        {
          p++;
          prev=cur;
        }
      }
        t--;
    }
  }
}
