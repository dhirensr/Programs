#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int n,c;
	 int x[100001];

	 int f(int d)
{
int cp=1;
	long int a=x[0];

for(int i=1;i<n;i++){
if(x[i]-a>=d){
cp++;

if(cp==d)
return 1;
a=x[i];
}

}
return 0;
}
	 int Binsearch()
{
	int start =0;
	int end=x[n-1];


while(start<end)
{
int mid= (start+end)/2;
	if(f(mid)==1)
	start=mid+1;
	else
	end=mid;

}
return start-1;
}



int main(void )
{
	int t;

	scanf("%d",&t);
	while(t--);
	{
	scanf("%d %d",&n,&c);
	for(int i=0;i<n;i++)
	scanf("%d",&x[i]);

	sort(x,x+n);

printf("%d \n",Binsearch());


   } 
  
}


