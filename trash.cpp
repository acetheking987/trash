#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char *argv[]) {
    string code = "";
    int index = -1;
    int array[200] = {0};
    if (argc == 1) {
        cout << "Usage: trash -f [file] ..." << endl;
        cout << "       trash [code] ..." << endl;
        return 0;
    } else {
        if (argv[1] == "-f") {
            ifstream file (argv[2]);
            if (!file.is_open()) {
                cout << "Error: file not found" << endl;
                return 1;
            } else {
                string line;
                std::stringstream sf;
                while ( getline (file,line) )
                {
                    sfline;
                }
                file.close();
            }
        } else {
            code = argv[1];
        }
    }
    string codeArray[code.length()] = code.split(";");
    while (index < code.length()) {
        index++;
        if (codeArray[index] == "") {
            continue;
        } else if (code[index][0] == '+') {
            array[stoi(codeArray[index][1:])]++;
        } else if (codeArray[index][0] == "-") {
            array[stoi(codeArray[index][1:])]--;
        } else if (codeArray[index][0] == "=") {
            array[stoi(codeArray[index][1:].split(":")[0])] = array[stoi(codeArray[index][1:].split(":")[1])];
        } else if (codeArray[index][0] == "p") {
            cout << array[stoi(codeArray[index][1:])];
        } else if (codeArray[index][0] == ">") {
            cin >> array[stoi(codeArray[index][1:])];
        } else if (codeArray[index][0] == "c") {
            int unicode = array[stoi(codeArray[index][1:])];
            cout << (char)unicode;
        } else if (codeArray[index][0] == "i") {
            if (array[stoi(codeArray[index][1:].split(":")[0])] == stoi(codeArray[index][1:].split(":")[1])) {
                index = stoi(codeArray[index][1:].split(":")[2]);
            }
        } else if (codeArray[index][0] == "g") {
            index = stoi(codeArray[index][1:]) - 1;
        } else if (codeArray[index][0] == "n") {
            cout << endl;
        } else {
            cout << "Error: unknown command" << endl;
            return 1;
        }
    }      
}
