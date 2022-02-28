
// UTILITIES
#ifndef _MY_CLASS_
#define _MY_CLASS_
#endif
std::size_t

// I/O
#include <iostream>
std::cin  >> vec[i];
std::cout << vec[i];

// MATH
#include <math.h>
floor()
ceil()

// STRINGS
#include <string>
strcmp(s1,s2);

// VECTORS
#include <vector>
std::vector<int> vec; // default constructor (empty container)
std::vector<int> vec(4, my_val); // fill constructor
std::vector<int> vec(vec2.begin(),vec2.end()); // range constructor
std::vector<int> vec(vec2); // copy constructor
std::vector<int> vec{7,3,9,2,4,7}; // initializer list constructor

vec.at(i) = 2 // ok, returns reference
vec[i] = x // error

for(std::vector<int>::iterator it = vec.begin(); it != vec.end(); ++it)
for(auto it = std::begin(v); it != std::end(v); ++it){std::cout << *it << std::endl;}
for(auto v: vec)

// STACK
std::stack<int> s;
s.empty();
s.size(); 
s.top();
s.push();
s.pop();
s1.swap(s2);

// POINTERS
Node * new_node = new Node(value);


// RANDOM
#include <random>
std::default_random_engine generator(seed);
std::uniform_int_distribution<int> distribution(0,9);
std::uniform_real_distribution<double> distribution(0.0,1.0);
std::normal_distribution<double> distribution(mean,std);
int number = distribution(generator); // call

// PAIR
#include <utility>
std::pair<int, char> PAIR1;
PAIR1.first = 100; //reference
PAIR1.second = 'G'; //reference

// C-array matrix
int x[3][4] = {{0,1,2,3}, {4,5,6,7}, {8,9,10,11}};

// SORT O(n*log(n))
#include <algorithm>
std::sort(vec.begin(), vec.begin()+4); 
std::sort(vec.begin(), vec.end());   

bool myfunction (int i,int j) { return (i<j); }
std::sort(vec.begin()+4, vec.end(), myfunction); // using function as comp

struct myclass {
  bool operator() (int i,int j) { return (i<j);}
} myobject;
std::sort(vec.begin(), vec.end(), myobject); // using object as comp

// HEAP
int myints[] = {10,20,30,5,15}; // C-array
std::vector<int> v(myints,myints+5); // vector
std::make_heap (v.begin(),v.end()); // rearrange values
std::pop_heap (v.begin(),v.end()); v.pop_back(); // pop max
v.push_back(99); std::push_heap (v.begin(),v.end()); // push
std::sort_heap (v.begin(),v.end()); // sort the heap

// ASSIGNMENT OPERATOR                                                                                                                                                
template<typename T> Matrix<T>& Matrix<T>::operator=(const Matrix<T>& rhs) {
  if (&rhs == this)
    return *this;
  // do stuff
  return *this;
}
Matrix & operator = (const Matrix & rhs){
	    if (this != &rhs) {
	        matrix = rhs.matrix;
	        size = rhs.size;
	    }
	    return *this;
}

// INHERITANCE
class Parent {
public:
    int a;
};

class Child : public Parent {
public:
    int b;
};

