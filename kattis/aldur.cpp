/*
read input
read input of loop
figure out the minimum
print
*/
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int youngest;
    cin >> youngest;

    for (int i = 1; i < n; i++) {
        int age;
        cin >> age;

        if (age < youngest) {
            youngest = age;
        }
    }

    cout << youngest << '\n';
    return 0;
}