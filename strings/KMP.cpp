#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void computeLPS(string pattern, int *lpsArray) {

    int n = pattern.size();

    int i = 1, j = 0;

    while (i < n) {

        if (pattern[i] == pattern[j]) {
            j++;
            lpsArray[i] = j;
            i++;
        } else {
            if (j == 0) {
                lpsArray[i] = 0;
                i++;
            } else {
                j = lpsArray[j - 1];
            }
        }
    }
}

void kmp(string text, string pattern) {

    int t_n = text.size();
    int p_n = pattern.size();

    if (p_n > t_n) {
        cout << "no match" << endl;
        return;
    }

    int lpsArray[p_n];

    computeLPS(pattern, lpsArray);

    int p_i = 0;
    int t_i = 0;

    while (t_i < t_n) {
        if (text[t_i] == pattern[p_i]) {
            t_i++;
            p_i++;
        }

        if (p_i == p_n) {
            cout << "matched at " << t_i << endl;
            p_i = lpsArray[p_i - 1];
        } else {
            if (p_i == 0) {
                t_i++;
            } else {
                p_i = lpsArray[p_i - 1];
            }
        }
    }
}

int main() {
    string text = "ABABDABACDABABCABAB";
    string pattern = "ABABCABAB";

    kmp(text, pattern);

    return 0;
}
