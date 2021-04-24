#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {
    /* Name: AoC 2020 Day 1
     * Author: Brendon Hutchins
     * Date: 01/12/20
     * Version: 1.0
     * --- Day 1: Report Repair ---
     */

    // Globals
    std::vector<int> importedData;
    std::string inputFile = "./input/input01.txt";
    //std::string inputFile = "./input/input_simple01.txt";
    std::ifstream inFile(inputFile);

    // Import Data
    if (inFile.is_open()){
        std::string line;
        while(std::getline(inFile, line)){
            importedData.push_back(stoi(line));
        }
    }

   std::vector<int>::iterator IT1, IT2, IT3;
// part a
    for (IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
        for (IT2 = IT1; IT2 < importedData.end(); IT2++){
            if (*IT1 + *IT2 == 2020){
                std::cout << "part a: " << *IT1 * *IT2 << std::endl;
            }
        }
    }

// part b
    for (IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
        for (IT2 = IT1; IT2 < importedData.end(); IT2++){
            for (IT3 = IT2; IT3 < importedData.end(); IT3++){
                if (*IT1 + *IT2 + *IT3 == 2020){
                    std::cout << "part b: " << *IT1 * *IT2 * *IT3 << std::endl;
                }
            }
        }
    }
    return 0;
}