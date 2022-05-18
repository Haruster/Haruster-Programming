#include <stdio.h>
#include <stdlib.h>

typedef int element;

typedef struct TreeNode {

    element key;

    struct TreeNode *left, *right;

} TreeNode;

TreeNode *new_node(int item) {

    TreeNode *temp = (TreeNode *)malloc(sizeof(TreeNode));

    temp->key = item;
    temp->left = temp->right = NULL;

    return temp;

}   

// 노드 삽입 함수

TreeNode *insert_node(TreeNode *node, int key) {

    // 트리가 공백이면 새로운 노드를 반환한다. 

    if(node == NULL) return new_node(key);

    // 그렇지 않으면 순환적으로 트리를 내려간다.

    if(key < node->key) {

        node->left = insert_node(node->left, key);

    }

    else if (key > node->key) {

        node->right = insert_node(node->right, key);

    }

    // 변경된 루트 포인터를 반환한다.

    return node;

}

// 최소값 찾기

TreeNode *min_value_node(TreeNode *node) {

    TreeNode *current = node;

    // 맨 왼쪽 단말 노드를 찾으러 내려간다.

    while(current->left != NULL) {

        currnet = current->left;

    }

    return current;

}

// 중위 순회

void inorder(TreeNode *root) {

    if(root) {

        inorder(root->left);    // 왼쪽 서브 트리 순회

        printf("[%d] ", root->key);

        inorder(root->right);   // 오른쪽 서브 트리 순회

    }

}

// 순환적인 탐색 함수

TreeNode *search(TreeNode *node, int key) {

    if (node == NULL) return NULL;

    if(key == node->key) return node;

    else if(key < node->key) {

        return search(node->left, key);

    }

    else {

        return search(node->right, key);

    }

}

int main(void) {

    TreeNode *root = NULL;
    TreeNode *tmp = NULL;

    root = insert_node(root, 30);
    root = insert_node(root, 20);
    root = insert_node(root, 10);
    root = insert_node(root, 40);
    root = insert_node(root, 50);
    root = insert_node(root, 60);

    printf("이진 탐색 트리 중위 순회 결과 \n");

    inorder(root);

    printf("\n\n");


    if(search(root, 30) != NULL) {

        printf("이진 탐색 트리에서 30을 발견함 \n");

    }

    else {

        printf("이진 탐색 트리에서 30을 발견하지 못함");

    }

    system("PAUSE");

    return 0;

}