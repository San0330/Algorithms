#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// naive approach: O(n^2)
vector<int> compute_z(string s){
   int n = s.size();
   int j;

   // create a empty vector with all 0 elements
   vector<int> z(n);

   // i points to the string starting for index 1
   for(int i = 1; i < n; i++){

       // j points to the start of prefix
       j = 0;

        while(i+j < n && s[j] == s[i+j]){

            // increment until prefix of string matches to
            // subset of string from index i
            // store the number of matched counts
            z[i]++;
            j++;

            // note: here we can replace j with z[i] to reduce memory use
        }
   }

   return z;
}

// efficient approach: O(n)
vector<int> compute_z2(string s){
   int n = s.size();

   // create a empty vector with all 0 elements
   vector<int> z(n);

    // left and right indicates the start and end of matched section/window
   int left = 0,right = 0;

   // i points to the string starting for index 1
   for(int i = 1; i < n; i++){

       // initialize j, with precalculated value from z[]
       // if i is inside the previous matched window
        if(i <= right){
            // corresponding ith (i-left)th element on prefix gives the matched value
            // but at position i, its value could to too large
            // so count from index i to rightmost index of window can be used
            // whichever is minimum

            z[i] = min(right - i + 1, z[i-left]);
        }

        // search if any other prefix matches
        while(i+z[i] < n && s[z[i]] == s[i+z[i]])
            z[i]++;

        // update value of left & right for matched segment
        if(i+z[i]-1 > right)
           left = i, right = i + z[i] - 1;
   }

   return z;
}

int main() {
    string s, pat;
    cout << "Enter pattern and string:\n";

    cin >> pat >> s;

    // using naive approach
    vector<int> z = compute_z(pat+"$"+s);
    // $ is the seprator, seprator shouldn't be any character present in
    // pattern or string

    for(int val : z)
        cout << val << " ";
    cout << endl;

    // using efficient approach
    vector<int> z2 = compute_z2(pat+"$"+s);

    for(int val : z2)
        cout << val << " ";
    cout << endl;

    return 0;
}

