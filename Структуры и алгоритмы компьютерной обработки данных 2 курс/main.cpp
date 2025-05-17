
#include <vector>
#include <tuple>

using namespace std;

vector<vector<tuple<int, int>>> Vec;
vector<vector<int>> mtx;
vector<bool>p;

void dfs(int v) {
    if (p[v]) {
        return;
    }
    p[v] = true;
    cout << v << endl;

    for (auto& tu : vec[v]){
        int to = get<0>(tu);
        int weight = get<1>(tu);
        cout << v << ' ' << to << ' ' << weight << endl;
        dfs(to);
    }
}

int main () {
    int n, m;
        cin >> n >> m;
        vec.resize(n + 1);
        mtx.resize(n + 1);
        p = vector<bool>(n + 1, 0);
        for (int i = 1; i<= n; ++i) {
            mtx[i] = vector<int>(n + 1, 0);
        }

        for (int i = 0; i < m; ++i){
            int from, to, weight;
            cin >> from >> to >> weight;
            mtx[from][to] = weight;
            mtx[to][from] = weight;

            vec[from].push.back(make_tuple(to, weight));
            vec[to].push.back(make_tuple(from, weight));
            
        }

        dfs(1);


}


/*
5 - кол-во вершин  7 - кол-во ребер
1 до 4 вес 2
1 до 2 вес 4
1 до 5 вес 3
3 до 4 вес 6
3 до 5 вес 2
3 до 2 вес 1
5 до 2 вес 4



*/