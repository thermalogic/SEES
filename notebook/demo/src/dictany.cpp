#include <string>
#include <iostream>
#include <unordered_map>
#include <any>

using namespace std;

int main()
{
   unordered_map<string, any> student = {{"name", "zhangshan"}, {"age", 20}};
   cout << any_cast<const char *>(student["name"]) << endl;
   cout << any_cast<int>(student["age"]) << endl;
   return 0;
}
