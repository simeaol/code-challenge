#include <bits/stdc++.h>

using namespace std;

int preffix[5011][5011];
int suffix[5011][5011];

void printa(int N, int M) {
  for (int i = 1; i <= N; ++i) {
    for (int j = 1; j <= M; ++j) {
      cout << preffix[i][j] << " ";
    }
    cout << endl;
  }
  cout << "--------" << endl;
  for (int i = 1; i <= N; ++i) {
    for (int j = 1; j <= M; ++j) {
      cout << suffix[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;
}

int main() {
  string A,B;
  int N,M;

  cin >> A >> B;
  N = A.length();
  M = B.length();

  for (int i = 1; i <= N; ++i) {
    for (int j = 1; j <= M; ++j) {
      if (A[i-1] == B[j-1]) preffix[i][j] = max(preffix[i][j], 1 + preffix[i-1][j-1]);
      else preffix[i][j] = max(preffix[i-1][j], preffix[i][j-1]);
    }
  }
  
  for (int i = N; i > 0; --i) {
    for (int j = M; j > 0; --j) {
      if (A[i-1] == B[j-1]) suffix[i][j] = max(suffix[i][j], 1 + suffix[i+1][j+1]);
      else suffix[i][j] = max(suffix[i+1][j], suffix[i][j+1]);
    }
  }
//  printa(N,M);

  int lcs = preffix[N][M];
  int ans = 0;
  unordered_map<char, bool> processed;

  for (int i = 0; i <= N; ++i) {
    processed.clear();Go
    for (int j = 0; j < M; ++j) {
      if (processed.count(B[j])) continue;
      int c = preffix[i][j] + suffix[i+1][j+2];
      if (c == lcs) {
        // cout << i << " " << j << " letter: " << B[j] << endl;
        ans++;
        processed[B[j]] = true;
      }
    }
  }
  cout << ans << endl;
}