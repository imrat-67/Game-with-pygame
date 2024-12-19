#include <bits/stdc++.h>
using namespace std;


string generateRandomString() {
    string result;
    for (int i = 0; i < 9; ++i) {
        result += '0' + (rand() % 10); 
    }
    return result;
}



vector<string> generateOhNoPattern() {
    vector<string> result;
    for (int i = 0; i < 9; ++i) {
        result.push_back(generateRandomString());
    }
    return result;
}


void generateTestCase(int type) {
    vector<string> testCase;

        testCase = generateOhNoPattern();





    for (const auto& line : testCase) {
        cout << line << endl;
    }
}

int main() {
    srand(time(0)); 

    freopen("input.txt","w",stdout);

    int type = 2;

    generateTestCase(type);

    return 0;
}
