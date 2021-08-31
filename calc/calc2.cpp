#include <iostream>

using namespace std;

int main(){
    char op;
    double num1,num2;

    cout << "Enter the Operator (+,-,*,/):";
    cin >> op;

    cout << "Enter two numbers one by one:";
    cin >> num1 >> num2;
    if (num2 == 0.0)
        cout << "Learn meth then come back";
    switch(op){

        case '+':
            cout << num1 << "+" << num2 << "=" << (num1 + num2);
            break;
        case '-':
            cout << num1 << "-" << num2 << "=" << (num1 - num2);
            break;
        case '*':
            cout << num1 << "*" << num2 << "=" << (num1 * num2);
            break;
        case '/':
            if (num2 == 0)
                break;
            else
                cout << num1 << "/" <<  "=" << (num1 / num2);
            
                
        
        
    }
    return 0;
}