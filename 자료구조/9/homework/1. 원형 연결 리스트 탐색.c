#include <stdio.h>
#include <stdlib.h>

typedef int element;

typedef struct CListType {

    element data;

    struct CListType* link;

} CListType;

void insert_first(CListType** phead, CListType* node) {

    if (*phead == NULL) {

        *phead = node;

        node->link = node;

    }

    else {

        node->link = (*phead)->link;

        (*phead)->link = node;

    }

}

void insert_last(CListType** phead, CListType* node) {

    if (*phead == NULL) {

        *phead = node;

        node->link = node;

    }

    else {

        node->link = (*phead)->link;

        (*phead)->link = node;

        *phead = node;

    }

}

CListType* create_node(element data) {

    CListType* new_node;

    new_node = (CListType*)malloc(sizeof(CListType));
    new_node->data = data;
    new_node->link = NULL;

    return new_node;

}

CListType* search(CListType* L, element data) {

    CListType* p = L;

    do {

        if (p->data == data) {

            return p;

        }

        p = p->link;

    } while(p != L);

    return NULL;

}