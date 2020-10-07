//link:http://noi-test.zzstep.com/contest/0x00%E3%80%8C%E5%9F%BA%E6%9C%AC%E7%AE%97%E6%B3%95%E3%80%8D%E4%BE%8B%E9%A2%98/0102%2064%E4%BD%8D%E6%95%B4%E6%95%B0%E4%B9%98%E6%B3%95
#include <iostream>
using namespace std;

int main() {
    int64_t a, b, p;
    cin >> a >> b >> p;
    int64_t ans = 0;
    while (b) {
        if (b & 1)
            ans = (ans + a) % p;
        a = a * 2 % p;
        b >>= 1;
    }
    cout << ans << endl;

    return 0;
}