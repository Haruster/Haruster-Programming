#include <stdio.h>
#include <stdlib.h>
#define MAX_ELEMENT 200
typedef struct {
	int key;
} element;
typedef struct {
	element heap[MAX_ELEMENT];
	int heap_size;
} HeapType;


// ª˝º∫ «‘ºˆ
HeapType* create()
{
	return (HeapType*)malloc(sizeof(HeapType));
}
// √ ±‚»≠ «‘ºˆ
void init(HeapType* h)
{
	h->heap_size = 0;
}
// «ˆ¿Á ø‰º“¿« ∞≥ºˆ∞° heap_size¿Œ »˜«¡ hø° item¿ª ª¿‘«—¥Ÿ.
// ª¿‘ «‘ºˆ
void insert_max_heap(HeapType* h, element item)
{

    int i;
    
    i = ++(h->heap_size);
    
    // 트리를 거슬러 올라가면서 부모 노드와 비교하는 과정이다.
    
    while ((i != 1) && (item.key > h->heap[i / 2].key)) {
        
        h->heap[i] = h->heap[i/2];
        
        i /= 2;
        
    }
    
    h->heap[i] = item; // 새로운 노드를 삽입한다.

}
// ªË¡¶ «‘ºˆ
element delete_max_heap(HeapType* h)
{
    
    int parent, child;

    element item, temp;

    
    item = h->heap[1];
    
    temp = h->heap[(h->heap_size)--];
    
    parent = 1;
    
    child = 2;
    
    
    while (child <= h->heap_size) {
        
        // 현재 노드의 자식 노드 중 더 큰 자식 노드를 찾는다.
        
        if((child < h->heap_size) && (h->heap_size) && (h->heap[child].key < h->heap[child + 1].key)) {
            
            child++;
            
        }
        
        if (temp.key >= h->heap[child].key) break;
        
        // 한 단계 아래로 이동
        
        h->heap[parent] = h->heap[child];
        
        parent = child;
        
        child *= 2;
        
    }
    
    h->heap[parent] = temp;
    
    return item;
	
}

int main(void)
{
	element e1 = { 10 }, e2 = { 5 }, e3 = { 30 };
	element e4, e5, e6;
	HeapType* heap;

	heap = create(); 	// »˜«¡ ª˝º∫
	init(heap);	// √ ±‚»≠

				// ª¿‘
	insert_max_heap(heap, e1);
	insert_max_heap(heap, e2);
	insert_max_heap(heap, e3);

	// ªË¡¶
	e4 = delete_max_heap(heap);
	printf("< %d > ", e4.key);
	e5 = delete_max_heap(heap);
	printf("< %d > ", e5.key);
	e6 = delete_max_heap(heap);
	printf("< %d > \n", e6.key);

	free(heap);
	
	//system("PAUSE");
	return 0;
}
