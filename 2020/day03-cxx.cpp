#include <iostream>
#include <vector>
#include <fstream>

/* Name: AoC 2020 Day 3
 * Author: Brendon Hutchins
 * Date: 03/12/20
 * Version: 1.0
 * --- Day 3: Toboggan Trajectory ---
 */

int main() {
    // Globals
    std::vector<std::string> importedData;
    std::string inputFile = "./input/input_simple03.txt";
//    std::string inputFile = "./input/input03.txt";
    std::ifstream inFile(inputFile);
    int treeCount = 0;
    int indexLocation = 3;
    bool seen = false;

    // Import Data
    if (inFile.is_open()){
        std::string line;
        while(std::getline(inFile, line)){
            importedData.push_back(line);
        }
    }

    std::vector<std::string>::iterator IT1;
    std::cout << inputFile << '\n';
    for (IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
        if (seen != true){ IT1++; seen = true;}
        std::string extractedRow = *IT1;

        char position = extractedRow[indexLocation]; // taking the third position from the row to check for tree.
        if (position == '#'){
            treeCount++;
        }

        //if(indexLocation+3 == 30 || indexLocation == 30){indexLocation=0;}
        if(indexLocation >= 30){indexLocation=0; std::cout << "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ" << std::endl;}

        std::cout << extractedRow << std::endl;
        std::cout << indexLocation <<  "    " << position << std::endl;
        indexLocation += 3;
    }
    std::cout << "tree count: " << treeCount << std::endl;
}
