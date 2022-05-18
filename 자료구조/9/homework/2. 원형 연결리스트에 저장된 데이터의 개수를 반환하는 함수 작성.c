int get_size(CListType* L) {

    CListType* p = L;

    int count = 0;

    do {

        count++;

        p = p->link;

    } while (p != L);

    return count;

}