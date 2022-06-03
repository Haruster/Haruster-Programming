// DFS 프로그램(인접 리스트 버전)

int visited[MAX_VERTICES];

// 인접 리스트로 표현된 그래프에 대한 깊이 우선 탐색

void dfs_list(GraphType* g, int v) {

    GraphNode* w;

    visited[v] = TRUE;  // 정점 v의 방문 표시

    printf("정점 %d -> ", v);   // 방문한 점정 출력

    for (w = g->adj_list[v]; w; w = w->link) {   // 인접 정점 탐색  

        if (!visited[w->vertex]) {

            dfs_list(g, w->vertex); // 정점 w에서 DFS 새로 시작

        }

}