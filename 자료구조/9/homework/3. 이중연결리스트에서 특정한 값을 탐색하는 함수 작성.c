DlistNode* search(DlistNode* L, element data) {

    DlistNode* p;

    for (p = L->rlink; p!= L; p->rlink) {

        if (p->data == data) {

            return p;

        }

    }   

    return NULL;

}