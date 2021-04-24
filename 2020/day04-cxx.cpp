#include <iostream>
#include <vector>
#include <fstream>

/* Name: AoC 2020 Day 4
 * Author: Brendon Hutchins
 * Date: 04/12/20
 * Version: 1.0
 * --- Day 4: Passport Processing ---
 */

/* Schema outline
 *
INDEX
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm
 *
 */

class passport{
public:
    bool passportValid;
    std::string eyeColour;
    int pid;
    int expiery;
    std::string hairColour;
    int birthYear;
    int issueYear;
    int countryID;
    int height;
};


void parsingFunction(std::vector<std::string> &importedData){
////hcl:#6b5442 ecl:brn iyr:2019
//    std::string s = "scott>=tiger";
//    std::string delimiter = ">=";
//    std::string token = s.substr(0, s.find(delimiter)); // token is "scott"


std::string headingDelimiter = ":";
std::string extractedLine = importedData[0];
// find position so we can increment.
std::cout << " delimeter at:  " << extractedLine.find(headingDelimiter) << "  " << std::endl; // index postion of delimiter

std::string headingKey = extractedLine.substr(0, extractedLine.find(headingDelimiter));

//std::cout << "function called: " << headingKey; // extracted heading key.
std::cout << "extracting value " << extractedLine.substr(extractedLine.find(headingDelimiter), extractedLine.find((" ")));

// switch heading key and assign correct values to object.

}

int main() {
    // Globals
    std::vector<std::string> importedData;
    std::vector<passport> passportCollection;
    std::string inputFile = "./input/input04.txt";
    std::ifstream inFile(inputFile);
    int validPassportCount = 0;
    // passport attributes
    bool passportValid;
    std::string eyeColour_g;
    int pid_g;
    int expiery_g;
    std::string hairColour_g;
    int birthYear_g;
    int issueYear_g;
    int countryID_g;
    int height_g;

    // Import Data
    if (inFile.is_open()){
        std::string line;
        while(std::getline(inFile, line)){
            //std::cout << line << std::endl;
            importedData.push_back(line);
        }
    }

    // 1. Extract line
    // 2. Find heading, extract value and assign to object attribute
    // 3. Perform validity check, update object attribute and update 'validPassportCount' value.
    // 4. Push object back into vector

    for (int i = 0 ; i < importedData.size(); i++){
        passport NewPassport;
        NewPassport.eyeColour;
        NewPassport.pid;
        NewPassport.expiery;
        NewPassport.hairColour;
        NewPassport.birthYear;
        NewPassport.issueYear;
        NewPassport.countryID;
        NewPassport.height;

        // Checks
//        if ()

        // Checks before set
        NewPassport.passportValid;
        passportCollection.push_back(NewPassport);
    }

    std::cout << "First index output: " << importedData[0] << std::endl;
    parsingFunction(importedData);

    return 0;
}
