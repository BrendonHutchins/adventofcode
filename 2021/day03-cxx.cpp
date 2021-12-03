// ==============================
// Name: AoC Day 03
// Author: Brendon Hutchins
// Date: 03/12/21
// Version: 1.0
// ==============================
//
// ==============================
// Comments:
// Part A
// Provided a list of binary numbers len[12] (simple 5). From this list of numbers you can calculate parameter/s from derived values. First para is Power Consumption, which is comprised of the product of derived values gammaRate && epsilonRate.
// gammaRate is defined by the expression => most common bit (1 || 0) in each column (col-major). Concatenated together will produce the full binary value of the gammaRate.
//  epsilonRate is the same as above, except the inverse (least common bit). Due to binary polarity, we can just flip the bits. Print product of decimal values.
//
// Part B
//
//
//
//  ==============================

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <tuple>
#include <cmath>


// Globals
std::vector<std::string> importedData;
std::string inputFilePath = "./input/input03.txt";
//std::string inputFilePath = "./input/input_simple03.txt";
std::ifstream inFileObject(inputFilePath);

// CHANGE ME
int importedDataLength = 12; // 5 or 12 // might replace name - idx-length or something.
int idx = 0;

std::tuple<std::string, float> searchFunction(std::vector<std::string>& importedData, int importedDataLength, int idx){
    std::vector<std::string>::iterator IT1;
    std::string gammaRate;
    int positiveCount = 0;
while (idx != importedDataLength){
    for(IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
        std::string extractedIdx;
        extractedIdx = ((*IT1)[idx]);
        if(extractedIdx == "1"){
            positiveCount++;
        }
    }
    idx++;

    if (positiveCount > (importedData.size() - positiveCount)){gammaRate.append("1");}
    else{gammaRate.append("0");
    };
    positiveCount = 0;
        }
    std::tuple<std::string, float> gammaRateEpsilonRate;
    gammaRateEpsilonRate = std::make_tuple(gammaRate, 1.0);
    return gammaRateEpsilonRate;
}

int main() {
// Read and import data
if (inFileObject.is_open()){
    std::string line;
    while(std::getline(inFileObject, line)){
        importedData.push_back(line);
    }
    std::tuple<std::string, float> gammaRateEpsilonRate = searchFunction(importedData, importedDataLength, idx);
    // flip
    std::bitset<12> gammaEpsilonRateBitset(std::get<0> (gammaRateEpsilonRate));
    gammaEpsilonRateBitset.flip();

    // TODO convert binary


// Print Output
std::cout << "gamma: " << std::get<0> (gammaRateEpsilonRate) << std::endl;
std::cout << "gamma inverse: " << gammaEpsilonRateBitset << std::endl;

}
    return 0;
}
