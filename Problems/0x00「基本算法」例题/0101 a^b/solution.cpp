//link:http://noi-test.zzstep.com/contest/0x00%E3%80%8C%E5%9F%BA%E6%9C%AC%E7%AE%97%E6%B3%95%E3%80%8D%E4%BE%8B%E9%A2%98/0101%20a%5Eb
#include <iostream>
using namespace std;

int main() {
    int32_t a, b, p;
    cin >> a >> b >> p;
    int32_t ans = 1 % p;
    a %= p;
    while (b) {
        if (b & 1)
            ans = static_cast<int64_t>(ans) * a % p;
        a = static_cast<int64_t>(a) * a % p;
        b >>= 1;
    }
    cout << ans << endl;

    return 0;
}