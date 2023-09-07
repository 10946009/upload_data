
#include <iostream>
using namespace std;

int main() {
    int N;
    while (cin >> N) {
        int sum = 0;
        for (int i = 1; i < N; i++) {
            if (N % i == 0)
                sum += i;
        }
        if (sum > N)
            cout << "1\n";
        else if (sum == N)
            cout << "3\n";
        else
            cout << "2\n";
    }
    return 0;
}