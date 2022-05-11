#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct TreeNode {

    int data;

    struct TreeNode *left, *right;

} TreeNode;

//      n1
//     /  |
//   n2   n3

void main() {

    TreeNode *n1, *n2, *n3;

    n1 = (TreeNode *)malloc(sizeof(TreeNode));
    n2 = (TreeNode *)malloc(sizeof(TreeNode));
    n3 = (TreeNode *)malloc(sizeof(TreeNode));



}