#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <algorithm>
#include <iterator>

std::vector<std::string> kgrams(std::string, int);
std::vector<int> measure(std::vector<std::string>, int);

main()
{
	std::string input = "pizza";
	auto lol = measure(kgrams(input, 2), 2);

}

std::vector<std::string> kgrams(std::string input, int len)
{
	std::vector<std::string> result;
	//This function splits the word into k-grams. Like abc to (a, ab, bc, c)

	if (input.length() < len)
		len = input.length();

	for(int i = 1; i != len; i++)
		result.push_back(input.substr(0, i)); // Add starting combinations

	for(int i = 0; i != input.length() - len; i++)
		result.push_back(input.substr(i, len)); // Add k-grams

	for(int i = len; i != 0; i --)
		result.push_back(input.substr(input.length() - i, i)); // Add ending combinations

	return result;
}

std::vector<int> measure(std::vector<std::string> input, int anchor = 2)
{
	int len = input.size();
	std::vector<int> points = {1, input.size()};
	std::vector<int> anchor_one, anchor_two;

	for(int i = 1; i <= len; i++)
	{
		anchor_one.push_back(std::abs(points[0] - i));
		anchor_two.push_back(std::abs(points[1] - i));
	}
	std::cout << "\nAnchor One\n";
	for(auto& i :anchor_one) std::cout << i << " ";
	std::cout << "\nAnchor Two\n";
	for(auto& i :anchor_two) std::cout << i << " ";

	return anchor_one;
}
