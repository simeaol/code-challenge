#include <bits/stdc++.h>

using namespace std;


int matrix[11][11];
bool visited[11] = {false};
int N = 10;

void DFS(int u, int space) {
    for (int i = 0; i < space; ++i) cout << "*";
    cout << " " << u << endl;
    
    if (visited[u] == true) {
        return;
    }

    visted[u] = true;

    for (int v = 1; v <= N; ++v) {
        if (matrix[u][v] != 0) {
            DFS(v, space+2);
        }
    }
    return;
}

int main() {
    matrix[1][2] = matrix[1][5] = matrix[1][6] = matrix[1][10] = 1;
    matrix[2][3] = matrix[2][4] = 1;
    matrix[5][7] = matrix[5][8] = 1;
    matrix[6][8] = matrix[6][9] = 1;
    matrix[10][9] = 1;

    cout << "main call\n";
    DFS(1, 2);
    return 0;
}