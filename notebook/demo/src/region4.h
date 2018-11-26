
#pragma once

#ifdef __cplusplus
extern "C" {
#endif

#ifdef BUILD_DLL

    #ifdef WIN32
        #define DLLPORT __declspec(dllexport) __stdcall 
    #else
        #define DLLPORT 
    #endif    

#else

    #ifdef WIN32
        #define DLLPORT __declspec(dllimport) __stdcall   
    #else
        #define DLLPORT 
    #endif    

#endif

DLLPORT  double pSat(double T);
DLLPORT  double TSat(double p);
        
#ifdef __cplusplus
	}
#endif        
