#include <iostream>

using namespace std;

int a;
int main()
{
	cin >> a;
	for (int i = 0; i < a; i++)
	{
		
		for (int j = a - i - 1; j > 0; j--)
		{
			cout << ' ';
		}

		for (int n = 0; n <= i; n++)
		{
			cout << '*';
		}

		cout << '\n';
		
	}

	return 0;
}