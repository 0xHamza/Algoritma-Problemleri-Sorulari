#include <iostream>

// Yöntem 1: Döngü Kullanarak Çözüm
int method1(int n) {
    int sum = 0;

    for (int i = 1; i < n; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }

    return sum;
}

// Yöntem 2: Matematiksel Formül Kullanarak Çözüm
int method2(int n) {
    int sum = 0;

    int sum3 = (n - 1) / 3 * (3 + (n - 1) / 3 * 3) / 2;
    int sum5 = (n - 1) / 5 * (5 + (n - 1) / 5 * 5) / 2;
    int sum15 = (n - 1) / 15 * (15 + (n - 1) / 15 * 15) / 2;

    sum = sum3 + sum5 - sum15;

    return sum;
}

int main() {
    int n = 1000;
  
    int result1 = method1(n);
    std::cout << "Yöntem 1 Sonucu: " << result1 << std::endl;

    int result2 = method2(n);
    std::cout << "Yöntem 2 Sonucu: " << result2 << std::endl;

    return 0;
}
