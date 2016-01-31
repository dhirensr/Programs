//CODECHEF PROBLEM


#include<stdio.h>
#include<stdlib.h>

int n,c,t,i,k;
int a[100001];

int main(void)
{
	scanf("%d",&t);
	while(t--)
	{
	scanf("%d",&n);
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
c=0;
	for(i=0;i<n;i++)
	{	
	for(k=i+1;k<n;k++)
	if((a[i]*a[k])%2==0)
	{
	c++;
	}

}
printf("%d \n",c);

}
return 0;
}