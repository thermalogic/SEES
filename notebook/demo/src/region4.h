
#pragma once

#ifdef BUILD_DLL

    #ifdef WIN32
      #define DLLPORT __declspec(dllexport) __stdcall 
    #else
      #define DLLPORT 
    #endif

#else

#define DLLPORT 

#endif

DLLPORT __stdcall double pSat(double T);
DLLPORT __stdcall double TSat(double p);
