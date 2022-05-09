// 반복적인 순회 : 스택을 이용한 중위 순회

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct TreeNode {

    int data;

    struct TreeNode *left, *right;

} TreeNode;

#define SIZE 100

int top = -1;

TreeNode *stack[SIZE];

void push(TreeNode *p) {

    if (top < SIZE - 1) {

        stack[++top] = p;

    }

}   

TreeNode *pop() {

    TreeNode *p = NULL;

    if (top >= 0) {

        p = stack[top--];

    }

    return p;

}

void inorder_iter(TreeNode *root) {

    while (1) {

        for (; root; root = root->left) {

            push(root);

        }

        root = pop();

        if (!root) break;

        printf("[%d]", root->data);

        root = root->right;

    }

}

//              15
//        4             20
//    1             16      25


TreeNode n1 = {1, NULL, NULL};
TreeNode n2 = {4, &n1, NULL};
TreeNode n3 = {16, NULL, NULL};
TreeNode n4 = {25, NULL, NULL};
TreeNode n5 = {20, &n3, &n4};
TreeNode n6 = {15, &n2, &n5};
TreeNode *root = &n6;

int main(void) {

    printf("중위 순회 = ");

    inorder_iter(root);

    printf("\n");

    return 0;

}