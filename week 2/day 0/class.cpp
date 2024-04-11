#include <iostream>
using namespace std;
class A{
  public:
  // int a;
  A()
  {
    cout<<"HI\n";
  }
};

int main() 
{
    // A(); //* it will invoke constructor of class
    A a,b;
    cout<<&a;
    cout<<endl<<&b;
    return 0;
}