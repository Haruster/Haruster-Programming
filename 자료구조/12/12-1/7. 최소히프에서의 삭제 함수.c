// 히프 트리에서의 삭제 함수

element delete_min_heap(HeapType* h) {

    int parent, child;

    element item, temp;

    item = h->heap[1];
    temp = h->heap[(h->heap_size)--];

    parent = 1;

    child = 2;

    while (child <= h->heap_size) {

        // 현재 노드의 자식노드 중 더 작은 자식노드를 찾는다.
        if ((child < h->heap_size) && (h->heap[child].key) > h->heap[child + 1].key) {

            child++;

        }

        if (temp.key < h->heap[child].key) break;

        // 한 단계 아래로 이동
        h->heap[parent] = h->heap[chlid];

        parent = child;

        child += 2;

    }

    h->heap[parent] = temp;

    return item;

}