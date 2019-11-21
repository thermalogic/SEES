#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

int main()
{
   unordered_map<string, int> dishes = {{"eggs",  2}, {"sausage", 1},{ "bacon", 1 }, {"spam", 500}};
   cout << dishes["eggs"] << endl; 
   typedef unordered_map<string,int> dictstrint;
   for(  dictstrint::iterator it= dishes.begin();it!= dishes.end();it++ ){
        cout<<"key = "<<it->first<<" value = "<<it->second<<endl;
   }
   return 0; 
}
