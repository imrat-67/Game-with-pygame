#include <iostream>
#include <cstdlib>

int main() {

    // Compile the code using g++
    int cr = std::system("g++ code02.cpp -o code02");

    if (cr != 0) {
        std::cerr << "Compilation failed\n";
        return 1; 
    }

    // Execute the compiled code with input/output redirection
    int er = std::system("./code02 < input.txt > output2.txt");  // Use './' to run the executable

    if (er != 0) {
        std::cerr << "Execution failed\n";
        return 1; 
    }

    return 0;
}
