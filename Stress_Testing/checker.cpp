#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cstdlib>  // For exit()

using namespace std;

int main() {
    int il, ol, v;
    il = 9, ol = 1;
    ifstream expected_output("output2.txt"); // Replace with the actual expected output file
    ifstream your_output("output1.txt"); // Replace with the actual output file

    vector<string> expected, your;
    string line;

    while (getline(expected_output, line))
        expected.push_back(line);

    while (getline(your_output, line))
        your.push_back(line);

    if (expected.size() != your.size()) {
        cout << "Output mismatch: Different number of lines." << endl;
        exit(0);  // Stop the program if the sizes do not match
    }

    for (int i = 0; i < expected.size(); i++) {
        if (expected[i] != your[i]) {
            cout << endl;
            cout << "Output mismatch at testcase " << (i + ol) / ol << ": " << endl;
            
            // Process input corresponding to the failing testcase
            freopen("input.txt", "r", stdin);  // Open input.txt for reading
            string sline;
            getline(cin, sline);  // Read the first line of the input file
            v = (i + ol) / ol;

            for (int j = 1; j < v; j++) {
                for (int l = 0; l < il; l++) {
                    getline(cin, sline);
                }
            }

            cout << "Input: " << endl;
            for (int l = 0; l < il; l++) {
                getline(cin, sline);
                cout << sline << endl;
            }

            // Display the expected and your output
            cout << "Expected: " << endl;
            for (int j = 0; j < ol; j++) cout << expected[(v - 1) * ol + j] << endl;
            cout << "Your output: " << endl;
            for (int j = 0; j < ol; j++) cout << your[(v - 1) * ol + j] << endl;

            exit(0);  // Stop the program if a mismatch is found
        }
    }

    cout << "Output matches!" << endl;
    return 0;
}
