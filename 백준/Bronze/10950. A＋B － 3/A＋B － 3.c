#include <stdio.h>
int main()
{
	int num1,num2,a;
	scanf("%d",&a);
	for (int i = 0; i < a; i++)
	{
		scanf("%d %d",&num1,&num2);
		printf("%d\n",num1 + num2);
	}
}
