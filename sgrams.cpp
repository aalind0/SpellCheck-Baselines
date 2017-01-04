// Implementation of skip-grams

#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> sgrams(std::string, int);

main(){
	std::string input;
	std::cout << "Enter the string\n";
	std::cin >> input;
	std::vector<std::string> output = sgrams(input, 1);
}

std::vector<std::string> sgrams(std::string input, int skip)
{
	std::vector<std::string> result;
	//This function splits the word into s-grams. Like abcd with s=1 to (ac, bd)

	for(int i = 0; i != input.length() - skip - 1; i++)
	{
		// result.push_back(input.substr(i, i + 1) + input.substr(i + skip, i + skip + 1));
		std::cout << input.substr(i, skip) + input.substr(i + skip + 1, skip) << std::endl;
	}
	return result;
}
