This repository has been merged by [kmyk/online-judge-tools](https://github.com/kmyk/online-judge-tools), so **obsoleted** now.
---

# ICPC testcases splitter

Split ACM/ICPC sytle testcases.

## usage

Give a parser, the testcase file and the output path.

``` sh
    $ python3 split.py ./a.out -i input.txt -o input-{}.txt
```

## example

The testcase file is like this:

```
    4 2
    0 1 A
    1 2 B
    6 6
    0 1 A
    0 2 A
    0 3 B
    0 4 A
    1 2 B
    4 5 C
    0 0
```

This testcase file has 2 testcase,

```
    4 2
    0 1 A
    1 2 B
```

and

```
    6 6
    0 1 A
    0 2 A
    0 3 B
    0 4 A
    1 2 B
    4 5 C
```

This tool splits these testcases into files.

To do this, you must prepare your (correct/incorrect) solution, like:

``` c++
    // a.cpp
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
```

And give it to this tool:

``` sh
    $ g++ a.cpp
    $ python3 split.py ./a.out -i input.txt -o input-{}.txt
```

Then you get testcase files like:

``` sh
    $ ls input-*.txt
    input-1.txt input-2.txt

    $ cat input-1.txt
    4 2
    0 1 A
    1 2 B
```

You may want to use `--time SECOND` and `--footer FOOTER` options.

``` sh
    $ python3 split.py ./a.out -i input.txt -o input-{}.txt --time 0.001 --footer '0 0'

    $ cat input-1.txt
    4 2
    0 1 A
    1 2 B
    0 0
```

Also for the outputs, you can do this with `-1` options if it is simple format. It splits the file line by line.

``` sh
    $ python3 split.py -1 -i output.txt -o output-{}.txt

    $ cat output.txt
    AB 2
    AC 3

    $ cat output-1.txt
    AB 2

    $ cat output-2.txt
    AC 3
```
