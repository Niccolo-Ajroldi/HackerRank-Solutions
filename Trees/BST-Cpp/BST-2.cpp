#include <iostream>
#include <vector>

class Node{
public:
	int data;
	Node * left;
	Node * right;
	Node(int d){
		data = d;
		left = NULL;
		right = NULL;
	}
	void print(void){
		std::cout << data << std::endl;
	}
};

void preOrder(Node* root){
	if(root==NULL){
		return;
	}
	else{
		root->print();
		preOrder(root->left);
		preOrder(root->right);
	}
}

Node* insert_rec(Node* root, int val){
	if(root == NULL){
		Node * new_node = new Node(val);
		root = new_node;
		return root;
	}
	if(val == root->data){
		return root;
	}
	else if(val < root->data){
		root->left = insert_rec(root->left, val);
	}
	else if(val > root->data){
		root->right = insert_rec(root->right, val);
	}
	return root;
}

class BST{
public:
	Node* root;
	BST();
	void print(void){
		preOrder(root);
	}
	void insert(int val){
		root = insert_rec(root, val);
	}
};

BST::BST(){
	root = NULL;
}

int main()
{
	BST bst;
	std::vector<int> vec{7,3,9,2,4,7};
	for(auto v: vec){
		bst.insert(v);
	}
	bst.print();

	return 0;
}
