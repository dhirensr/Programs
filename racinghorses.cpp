#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
long s[5001];
int n,t,i;
long int c;
int main(void)
{
	scanf("%d",&t);
	while(t--)
	{
c=99999999;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	scanf("%ld",&s[i]);
	sort(s,s+n);
	for(i=1;i<n;i++)
		if(s[i]-s[i-1]<=c)
		{
			c=s[i]-s[i-1];
		}
		printf("%ld\n",c);
	}
	return 0;
}