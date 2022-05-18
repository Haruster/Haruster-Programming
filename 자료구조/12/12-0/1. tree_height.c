#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct TreeNode {

    int data;

    struct TreeNode *left, *right;

} TreeNode;

//          15
//      4           20
//    1         16      25

TreeNode n1 = {1, NULL, NULL};
TreeNode n2 = {4, &n1, NULL};
TreeNode n3 = {16, NULL, NULL};
TreeNode n4 = {25, NULL, NULL};
TreeNode n5 = {20, &n3, &n4};
TreeNode n6 = {15, &n2, &n5};

TreeNode *root = &n6;


// 중위 순회

void inorder(TreeNode *root) {

    if (root != NULL) {

        inorder(root->left);    // 왼쪽 서브트리 순회

        printf("[%d] ", root->data);    // 노드 방문

        inorder(root->right);   // 오른쪽 서브 트리 순회

    }

}

// 전위 순회

void preorder(TreeNode *root) {

    if (root != NULL) {

        printf("[%d\ ", root->data);    // 노드 방문

        preorder(root->left);   // 왼족 서브트리 순회

        preorder(root->right);  // 오른족 서브 트리 순회

    }

}

// 후위 순위

void postorder(TreeNode *root) {

    if(root != NULL) {



    }

}