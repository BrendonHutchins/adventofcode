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
// Provided a list of binary numbers char len[12] (simple 5). From this list of numbers you can calculate parameters from derived values. First para is Power Consumption, which is comprised of the product of derived values gammaRate && epsilonRate.
// gammaRate is defined by the expression => most common bit (1 || 0) in each column (col-major). Concatenated together will produce the full binary value of the gammaRate.
//  epsilonRate is the same as above, except the inverse (least common bit). Due to binary polarity, we can just flip the bits. Print product of decimal values.
//
// Part B
// From the list of binary numbers calculate the parameter "Life Support System" which is comprised of two different values. 'Oxygen generator rating' and 'Co2 Scrubber Rating'.
// OxygenRating and Co2 Scrubber Rating are both results from an expression applied to a reducing binary input list. The when a single value remains after applying the criteria across each bit, that is the rating value.
// OxygenRating => most common bit (1 || 0) across each column, discard any numbers that do not match the MCB in that position. If equally common, keep 1
// Co2ScrubRating => Inverse of OxygenRating. If equally common, keep 0.
//  ==============================

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <tuple>
#include <cmath>


// Globals
std::vector<std::string> importedData;
//std::string inputFile = "./input/input03.txt";
std::string inputFile = "./input/input_simple03.txt";
std::ifstream inFileObject(inputFile);

// CHANGE ME
int importedDataCharLength = 5; // 5(simple) or 12 (full input)
int idx = 0;

// Part A
std::tuple<std::string, float> searchFunctionPartA(std::vector<std::string>& importedData, int importedDataCharLength, int idx){
    std::vector<std::string>::iterator IT1;
    std::string gammaRate;
    int positiveCount = 0;
while (idx != importedDataCharLength){
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
    gammaRateEpsilonRate = std::make_tuple(gammaRate, 1.0); //only using index 0 for tuple
    return gammaRateEpsilonRate;
}

// Part B1 - Find Oxygen Rating
void searchFunctionPartBOxygen(std::vector<std::string>& importedData, int importedDataLength){
    std::vector<std::string>::iterator IT1;
    int positiveCount = 0;
    int idx = 0;
    int importedDataArrayLength = importedData.size(); // the length is dynamic and is reduced after discarding candidates from the list.

    // calculating the MCB for each col. This is expressed by positive count, from this we can calculate MCB is 1 or 0.
    while (idx != importedDataLength){
        for(IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
            std::string extractedIdx;
            extractedIdx = ((*IT1)[idx]);
            if(extractedIdx == "1"){
                positiveCount++;
            }
        }

        // CASE: MCB - equal
        if(positiveCount == (importedDataArrayLength - positiveCount)){
            for(IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
                std::string extractedIdx;
                extractedIdx = ((*IT1)[idx]);
                if(extractedIdx == "0"){
                    (*IT1) = "nill";
                    importedDataArrayLength--;
                }
            }
        }
        // CASE: MCB - one
        if(positiveCount > (importedDataArrayLength - positiveCount)){
            for(IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
                std::string extractedIdx;
                extractedIdx = ((*IT1)[idx]);
                if(extractedIdx == "0"){
                    (*IT1) = "nill";
                    importedDataArrayLength--;
                }
            }
        }
        // CASE: MCB - zero
        if(positiveCount < (importedDataArrayLength - positiveCount)){
            for(IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
                std::string extractedIdx;
                extractedIdx = ((*IT1)[idx]);
                if(extractedIdx == "1"){
                    (*IT1) = "nill";
                    importedDataArrayLength--;
                }
            }
        }
        idx++;
        positiveCount = 0;
    }
}

// Part B2 - Find CO2 Scrubber Rating
void searchFunctionCO2Scrubber(std::vector<std::string>& importedData, int importedDataLength){
    std::vector<std::string>::iterator IT1;
    int positiveCount = 0;
    int idx = 0;
    int importedDataArrayLength = importedData.size();

    // calculating the MCB for each col. This is expressed by positive count, from this we can calculate MCB is 1 or 0.
    while (idx != importedDataLength){
        for(IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
            std::string extractedIdx;
            extractedIdx = ((*IT1)[idx]);
            if(extractedIdx == "1"){
                positiveCount++;
            }
        }
if(importedDataArrayLength == 1){break;}
        // CASE: MCB - equal
        if(positiveCount == (importedDataArrayLength - positiveCount)){
            for(IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
                std::string extractedIdx2;
                extractedIdx2 = ((*IT1)[idx]);
                if(extractedIdx2 == "1"){
                    (*IT1) = "nill";
                    importedDataArrayLength--;
                    if(importedDataArrayLength == 1){break;}
                }
            }
        }
        // CASE: LCB - one
        else if(positiveCount > (importedDataArrayLength - positiveCount)){
            for(IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
                std::string extractedIdx2;
                extractedIdx2 = ((*IT1)[idx]);
                if(extractedIdx2 == "1"){
                    (*IT1) = "nill";
                    importedDataArrayLength--;
                    if(importedDataArrayLength == 1){break;}
                }
            }
        }
        // CASE: LCB - zero
        else if(positiveCount < (importedDataArrayLength - positiveCount)){
            for(IT1 = importedData.begin(); IT1 < importedData.end(); IT1++){
                std::string extractedIdx2;
                extractedIdx2 = ((*IT1)[idx]);
                if(extractedIdx2 == "0"){
                    (*IT1) = "nill";
                    importedDataArrayLength--;
                    if(importedDataArrayLength == 1){break;}
                }
            }
        }
        idx++;
        positiveCount = 0;
    }
}

int main() {
// Read and import data
if (inFileObject.is_open()){
    std::string line;
    while(std::getline(inFileObject, line)){
        importedData.push_back(line);
    }
    std::tuple<std::string, float> gammaRateEpsilonRate = searchFunctionPartA(importedData, importedDataCharLength, idx);

    // Can only run searchFunction at a time, the other must be commented out (mutate the same array).
    searchFunctionPartBOxygen(importedData, importedDataCharLength);
    //searchFunctionCO2Scrubber(importedData, importedDataCharLength);

    // flip
    std::bitset<5> gammaEpsilonRateBitset(std::get<0> (gammaRateEpsilonRate));
    gammaEpsilonRateBitset.flip();

    // TODO convert binary function

// Print Output
std::cout << "Gamma Rate: " << std::get<0> (gammaRateEpsilonRate) << std::endl;
std::cout << "Epsilon Rate: " << gammaEpsilonRateBitset << std::endl << std::endl;

std::cout << "Printing Oxygen/CO2 Scrubber Array: " << std::endl;
//for(int i = 0; i < importedData.size(); i++){if(importedData[i] != "nill"){std::cout << "OxygenGen/CO2 Srubber Rating: " << importedData[i] << std::endl;}}

    for(int i = 0; i < importedData.size(); i++){std::cout << "OxygenGen/CO2 Srubber Rating: " << importedData[i] << std::endl;}

}
    return 0;
}