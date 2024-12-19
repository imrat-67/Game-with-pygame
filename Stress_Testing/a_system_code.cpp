#include <cstdlib>
#include <iostream>
#include <string>

void run(const std::string& s){
    const char* cppFileName = s.c_str();  // Use c_str() instead of data() for string to char* conversion.

    // Extract file name without extension
    std::string val;
    int i=0;
    while (s[i] != '.') {
        val += s[i];
        i++;
    }

    // Compile command for Linux (g++ will generate 'a.out' as default executable name)
    std::string compileCommand = "g++ -o a.out " + std::string(cppFileName);
    int compileResult = system(compileCommand.c_str());

    if (compileResult == 0) {
        std::cout << val << " running" << std::endl;
        // Run the compiled executable (use a.out for Linux)
        const char* runCommand = "./a.out";  // Linux uses './' to run executables in the current directory
        int runResult = system(runCommand);

        if (runResult == 0) {
            std::cout << val << " executed successfully." << std::endl;
        } else {
            std::cerr << "Execution failed for " << val << "." << std::endl;
        }
    } else {
        std::cerr << "Compilation failed for " << val << "." << std::endl;
    }
}

int main() {
    int n = 100;  // Total number of iterations
    for (int i = 0; i < n; i++) {
        std::cout << "Checking " << i + 1 << ": " << std::endl;
        run("Test_case_gen.cpp");
        run("first_code_executer.cpp");
        run("second_code_executer.cpp");
        run("checker.cpp");
        std::cout << std::endl;
    }
}
