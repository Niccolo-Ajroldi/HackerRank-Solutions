#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int partition(std::vector<int> &v, int start, int end){
    int pivot = v[end-1];
    int i = start;
    for(int j=start; j<end; ++j){
        if(v[j] < pivot){
            std::swap(v[i],v[j]);
            i++;
        }
    }
    // reallocate pivot
    std::swap(v[i], v[end-1]);
    
    // print
    for(auto x: v){
        std::cout << x << " ";
    }
    std::cout << std::endl;
    
    return i;
}

void QuickSort_rec(std::vector<int> &v, int start, int end){
    if(end==start){
        return;
    }
    int pivot_idx = partition(v, start, end);
    
    // left
    if(pivot_idx - start > 1){
        QuickSort_rec(v, start, pivot_idx);
    }
    // right
    if(end - pivot_idx -1 > 1){
        QuickSort_rec(v, pivot_idx+1, end);        
    }
}

void QuickSort(std::vector<int> &v){
    QuickSort_rec(v, 0, v.size());
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    std::cin >> n;
    std::vector<int> vec(n);
    for(int i=0; i<n; i++){
        std::cin >> vec[i];
    }
    QuickSort(vec);
    
    return 0;
}
