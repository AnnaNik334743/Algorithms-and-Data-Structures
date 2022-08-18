#include <iostream>

using namespace std;

int main()
{
    unsigned long long n, m, s=2, t=2;
    cin >> n >> m;
    for (int k=2; k<=n; ++k)
    {
        t = (t * 2 * k) % m;
        s = (s + t) % m;
    }
    cout << s << endl;
}
