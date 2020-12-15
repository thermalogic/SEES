#pragma once

#ifdef __cplusplus
extern "C" {
#endif

#ifdef BUILD_DLL

    #ifdef WIN32
        #define PORT __declspec(dllexport) double __stdcall 
    #else
        #define PORT double
    #endif    

#else

    #ifdef WIN32
        #define PORT __declspec(dllimport) double __stdcall   
    #else
        #define PORT double
    #endif    

#endif

PORT pSat(double t);
        
#ifdef __cplusplus
	}
#endif        
