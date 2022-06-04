// BFS 프로그램(인접행렬)

void bfs_mat(GraphType* g, int v) {

    int w;

    QueueType q;

    queue_init(&q); // 큐 초기화

    visited[v] = TRUE;  // 정점 v 방문 표시

    printf("%d 방문 -> ", v);

    enqueue(&q, v); // 시작 정점을 큐에 저장

    while (!is_empty(&q)) { // 큐에 정점 추출

        v = dequeue(&q);

        for (w = 0; w < g->n; w++) {    // 인접 정점 탐색
        
            if (g->adj_mat[v][w] && !visited[w]) {

                visited[w] = TRUE;  // 방문 표시

                printf("%d 방문 -> ", w);

                enqueue(&q, w); // 방문한 정점을 큐에 저장

            }
        
        }

    }

}

int main(void) {

    GraphType *g;

    g = (GraphType *)malloc(sizeof(GraphType));

    graph_init(g);

    for (int i = 0; i < 6; i++) {

        insert_vertex(g, i);

    }

    insert_edge(g, 0, 2);
    insert_edge(g, 2, 1);
    insert_edge(g, 2, 3);
    insert_edge(g, 0, 4);
    insert_edge(g, 4, 5);
    insert_edge(g, 1, 5);

    printf("너비 우선 탐색\n");

    bfs_mat(g, 0);

    printf("\n");

    free(g);

    return 0;

}