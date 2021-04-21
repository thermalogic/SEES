
#include <iostream>
#include <string>
#include <tuple>
#include <unordered_map>
 
using namespace std;
typedef tuple<string,string,float> tupTag;
 
int main()
{  
    unordered_map<int, tupTag> tags;
    tags[108600] =(tupTag){"CompressorIPortM","压缩机入口质量流量",0.08 };
    cout << "108600:  " <<get<0>(tags[108600]) <<"\t"<< get<1>(tags[108600])<< "\t"<<get<2>(tags[108600])<<endl;
    return 0;
}
