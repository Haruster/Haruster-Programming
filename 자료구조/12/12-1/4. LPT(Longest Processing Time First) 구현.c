#define JOBS 7
#define MACHINES 3

int main(void) {

    int jobs[JOBS] = {8, 7, 6, 5, 4, 3, 2, 1};  // 작업은 정렬되어 있다고 가정한다.

    element m = {0, 0};

    HeapType* h;

    h = create();

    init(h);

    // 여기서  avail 값은 기계가 사용 가능하게 되는 시간을 의미한다.

    for (int i = 0; i < MACHINES; i++) {

        m.id = i + 1;
        m.avail = 0;

        insert_min_heap(h, m);

    }

    // 최소 히프에서 기계를 꺼내서 작업을 할당하고 사용 가능 시간을 증가시킨 후에 다시 최소 히프에 추가한다.

    for (int i = 0; i < JOBS; i++) {

        m = delete_min_heap(h);

        printf("JOB %d을 시간 = %d부터 시간 = %d까지 기계 %d번에 할당한다. \n", i, m.avail, m.avail + jobs[i] - 1, m.id);

        m.avail += jobs[i];

        insert_min_heap(h, m);

    }

    return 0;

}