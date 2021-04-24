
#include <iostream>
#include <string>
#include <tuple>
#include <unordered_map>
 
using namespace std;
typedef tuple<string,string,string,float> tupTag;
 
int main()
{  
    unordered_map<int, tupTag> tags;
    tags[600] =(tupTag){"CompressorIPortM","压缩机入口质量流量","kg/s",0.08 };
    cout << "Tag 600:  " <<get<0>(tags[600]) <<"\t"<< get<1>(tags[600])
         << "\t"<<get<2>(tags[600])<< "\t"<<get<3>(tags[600])<<endl;
    return 0;
}
