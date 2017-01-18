#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main() {
    while (true) {
        // input
        int v, e; cin >> v >> e;
        if (v == 0 and e == 0) break;;
        vector<map<int,char> > g(v);
        for (int i = 0; i < e; ++ i) {
            int v, w; char c; cin >> v >> w >> c;
            g[v][w] = c;
        }
        // output
        cout << "-1" << endl;
    }
    return 0;
}
