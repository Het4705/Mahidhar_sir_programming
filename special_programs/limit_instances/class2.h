#include <iostream>
class parent{
    private:
    static int count;
    public:
    parent()
    {
        if (count>=1)
        {
            std::cout<<"no more than 1 child is allowed\n";
            return;
        }
        else{
            std::cout<<"object is made\n";
            count++;
        }
    }
    int someData;
};
int parent::count=0;


