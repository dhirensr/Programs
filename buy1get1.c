#include<string.h>
#include<stdio.h>

char s[201];
int cost;
int main(void)
{
	int t,i;
	scanf("%d",&t);
	while(t--)
	{
		int check[125]={0};
	cost=0;
	   scanf("%s",&s);
	   for(i=0;i<strlen(s);i++)
	   {

	    if(check[s[i]]==0)
	    {cost++;
	    check[s[i]]=1;
	    }
	    else
	    check[s[i]]=0;
	   }
	 printf("%d \n",cost);
	}
	return 0;
}