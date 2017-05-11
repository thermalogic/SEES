
#ifdef BUILD_DLL
#define DLLPORT __declspec(dllexport)
#else
#define DLLPORT __declspec(dllimport)
#endif

DLLPORT __stdcall double fadd(double a,double b);
DLLPORT __stdcall double fmul(double a, double b);