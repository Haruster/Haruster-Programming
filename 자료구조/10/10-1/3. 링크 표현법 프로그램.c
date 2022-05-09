// 링크 표현법 프로그램

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct TreeNode {

    int data;

    struct TreeNode *left, *right;

} TreeNode;

//  n1
//  /   |
//  n2  n3

void main() {

    TreeNode *n1, *n2, *n3;

    n1 = (TreeNode *)malloc(sizeof(TreeNode));
    n2 = (TreeNode *)malloc(sizeof(TreeNode));
    n3 = (TreeNode *)malloc(sizeof(TreeNode));

    n1->data 10;    // 첫 번째 노드
    n1->left = n2;
    n1->right = n3;

    n2->data = 20;  // 두 번째 노드
    n2->left = NULL;
    n2->right = NULL;

    n3->data = 30;  // 세 번째 노드
    n3->left = NULL;
    n3->right = NULL;

    free(n1);
    free(n2);
    free(n3);

    return 0;

}