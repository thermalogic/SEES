
# Googletest Static Library for MinGW-W64(64)

## Add Googletest include and lib paths for MinGW-W64 

Add `include and lib` paths to the environment variables:

* `CPLUS_INCLUDE_PATH` and `C_INCLUDE_PATH` for include directories 
 
* `LIBRARY_PATH` for library directories: `lib`

## validate the installation

use the following [demo_gtest_main.cpp](./example/demo_gtest_main.cpp) as a simple test example

```cpp
#include <gtest/gtest.h>

TEST(MathTest, TwoPlusTwoEqualsFour)
{
       EXPECT_EQ(2 + 2, 4);
}
```

Bulid：

```bash
g++ -o demo_gtest_main.exe  demo_gtest_main.cpp -lgtest -lgtest_main
```

Run:

```bash
./demo_gtest_main
```
