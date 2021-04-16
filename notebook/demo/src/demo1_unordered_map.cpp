
#include <iostream>
#include <string>
#include <unordered_map>
 
int main()
{
    std::unordered_map<std::string, int> months;
    months["january"] = 31;
    months["february"] = 28;
    months["march"] = 31;
    std::cout << "february  -> " << months["february"] << std::endl;
    return 0;
}
