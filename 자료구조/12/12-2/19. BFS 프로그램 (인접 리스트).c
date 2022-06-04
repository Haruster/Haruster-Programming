// BFS 프로그램 (인접 리스트)

void bfs_list(GraphType* g, int v) {

    GraphNode* w;

    QueueType q;

    init(&q);   // 큐 초기화

    visited[v] = TRUE;  // 정점 v 방문 표시

    printf("%d 방문 -> ", v);

    enqueue(&q, v);     // 시작 정점을 큐에 저장

    while (!is_empty(&q)) {

        v = dequeue(&q);    // 큐에 저장된 정점 선택

        for ( w= g->adj_list[v]; w = w->link) { // 인접 정점 탐색
        
            if(!visited[w->vertex]) {   // 미방문 정점 탐색

                visited[w->vertex] = TRUE;  // 방문 표시

                printf("%d 방문 -> ", w->vertex);

                enqueue(&q, w->vertex); // 정점을 큐에 삽입
 
            }
        
        }

    }



}