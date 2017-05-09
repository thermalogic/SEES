
#ifdef BUILD_DLL
#define DLLPORT __declspec(dllexport)
#else
#define DLLPORT __declspec(dllimport)
#endif

DLLPORT int __stdcall iadd(int a,int b);
DLLPORT float __stdcall fmult(float a, float b);