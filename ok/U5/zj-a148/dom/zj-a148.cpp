
#include <iostream>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        int x, sum = 0;
        for (int i = 0; i < n; i++) {
            cin >> x;
            sum += x;
        }
        if (sum > 59 * n) {
            cout << "0\n";
        } else {
            cout << "1\n";
        }
    }
    return 0;
}