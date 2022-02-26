
#include <algorithm>
#include <vector>
#include <iostream>

class Matrix{
public:
	typedef std::vector<int>::size_type size_type;
	typedef bool value_type;
	typedef std::vector<value_type> vector_type;
	typedef std::vector<vector_type> matrix_type;

	matrix_type matrix;
	size_type size;
	size_type n_rows;
	size_type n_cols;

	Matrix(size_type n_rows, size_type n_cols);
	Matrix(const Matrix & rhs);
    
	void print(void);
	
	Matrix & operator = (const Matrix & rhs){
	    if (this != &rhs) {
	        matrix = rhs.matrix;
	        size = rhs.size;
	        n_rows = rhs.n_rows;
	        n_cols = rhs.n_cols;
	    }
	    return *this;
	}

};


Matrix::Matrix(Matrix::size_type n_rows, Matrix::size_type n_cols){
	matrix = matrix_type(n_rows, vector_type(n_cols, false));
	size = n_cols*n_rows;
	n_rows = n_rows;
	n_cols = n_cols;
}

Matrix::Matrix(const Matrix & rhs){
    matrix = rhs.matrix;
    size = rhs.size;
	n_rows = rhs.n_rows;
	n_cols = rhs.n_cols;
}

void Matrix::print(void){
	for(auto vec: matrix){
		for(auto val: vec){
			std::cout << val << "\t";
		}
		std::cout << std::endl;
	}

}

void mark_island(int i, int j, Matrix &m){
    
    int n_rows = m.n_rows;
    int n_cols = m.n_cols;
    
    // if this is not a valid index
    if(i<0 || (i>n_rows-1) || j<0 || (j>n_cols-1)){
        return;
    }
    
    if(!m.matrix[i][j]){
        return;
    }
    
    m.matrix[i][j] = false;
    
    mark_island(i-1, j, m);
    mark_island(i+1, j, m);
    mark_island(i, j-1, m);
    mark_island(i, j+1, m);
}

int count_islands(Matrix& m){
    
    int n_rows = m.n_rows;
    int n_cols = m.n_cols;
    
    unsigned count = 0;
    
    for(int i=0; i<n_rows; ++i){
        for(int j=0; j<n_cols; ++j){
            // se sono in un isola
            if(m.matrix[i][j]){
                std::cout << "OOOO" << std::endl;
                count += 1;
                mark_island(i, j, m);
            }
        }
    }
    
    return count;
    
}

int main(){

	Matrix m(5,4);
	
	int matrix[5][4] = {{true , false, true , false},
              		   {true , false, true , true },
              		   {false, false, true , false},
              		   {false, false, false, true },
              		   {true , false, true , false}};

    for(int i=0; i<5; ++i){
        for(int j=0; j<4; ++j){
        	m.matrix[i][j] = matrix[i][j];
        }
    }
    
    m.print();
    
    std::cout << "Cout=" << count_islands(m) << std::endl;
    
    m.print();

	return 0;
}

