
#include <iostream>
using namespace std;

int main()
{
    int M, D, S;
    cin >> M >> D;
    S = (M * 2 + D) % 3;
    if (S == 0) {
        cout << "0\n";
    } else if (S == 1) {
        cout << "1\n";
    } else {
        cout << "2\n";
    }
    return 0;
}