#include <iostream>
#include <vector>
using namespace std;

int n;
int main()
{
	int a;
	int what;
	int r = 0;
	cin >> n;
	vector<int> num;
	for (int i = 0; i < n; i++) {
		cin >> a;
		num.push_back(a);
	}
	cin >> what;
	for (int i = 0; i < n; i++) {
		if (num[i] == what)
			r++;
	}
	cout << r;
}
