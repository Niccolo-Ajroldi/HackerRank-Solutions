

#include <vector>
#include <math.h>

bool BS(std::vector<int> &vec, val){

	typedef std::vector<int>::size_type s_type;
	s_type l = 0;
	s_type r = vec.size()-1;

	while(l <= r){
		s_type mid = floor((l+r)/2);
		if(val > vec[mid]){
			l = mid+1;
		}
		else if(val < vec[mid]){
			r = mid-1;
		}
		else{
			std::cout << val << " found at position " << mid << std::endl;
			return TRUE
		}
	}
	return FALSE
}

int main(){

	std::vector<int> vec{1,2,4,6,7,8}


	return 0;
}

