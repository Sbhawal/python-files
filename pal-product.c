#include<stdio.h>


int isPalindrome(int number) {
   int temp = number;
   int rev = 0;
   while(number > 0){
      rev = 10 * rev + number % 10; 
      number/=10;
   }
   if(rev == temp)
      return 1;
   return 0;
}


int main()
{
	int sol()
	{
	static int p,q,r,t;
	for(p=990;p>99;p-=11)
	{
		for(q=999;q>99;q--)
		{
			t=p*q;
			if(r<t && isPalindrome(t))
			{
				r=t;
				break;
			}
			else if(t<r)
				break; 
		}
	}
	return r;
	}

	printf("%d\n",sol() );

}