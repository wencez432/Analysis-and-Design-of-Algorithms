#include <bits/stdc++.h>
using namespace std;
#define N 3

struct Node{
    Node* parent;
    int pathCost;
    int cost;
    int cityID;
    int containerID;
    bool assigned[N];
};

Node* newNode(int x, int y, bool assigned[], Node* parent){
    Node* node = new Node;

    for (int j = 0; j < N; j++)
        node->assigned[j] = assigned[j];
    node->assigned[y] = true;

    node->parent = parent;
    node->cityID = x;
    node->containerID = y;

    return node;
}

int calculateCost(int costMatrix[N][N], int x, int y, bool assigned[]){
    int cost = 0;
    bool available[N] = {true};

    for (int i = x + 1; i < N; i++){
        int min = INT_MAX, minIndex = -1;

        for (int j = 0; j < N; j++){
            if (!assigned[j] && available[j] && costMatrix[i][j] < min){
                minIndex = j;
                min = costMatrix[i][j];
            }
        }

        cost += min;
        available[minIndex] = false;
    }

    return cost;
}

struct comp{
    bool operator()(const Node* lhs, const Node* rhs) const
    {
        return lhs->cost > rhs->cost;
    }
};

void printAssignments(Node *min){
    if(min->parent==NULL)
        return;

    printAssignments(min->parent);
    cout  << "Asignar contenedor " << min->containerID + 1 << " a la ciudad " << char(min->cityID + '1') << endl;

}

int findMinCost(int costMatrix[N][N]){
    priority_queue<Node*, std::vector<Node*>, comp> pq;

    bool assigned[N] = {false};
    Node* root = newNode(-1, -1, assigned, NULL);
    root->pathCost = root->cost = 0;
    root->cityID = -1;

    pq.push(root);

    while (!pq.empty()){
        Node* min = pq.top();
        pq.pop();

        int i = min->cityID + 1;

        if (i == N){
            printAssignments(min);
            return min->cost;
        }

        for (int j = 0; j < N; j++){
            if (!min->assigned[j]){
                Node* child = newNode(i, j, min->assigned, min);

                child->pathCost = min->pathCost + costMatrix[i][j];
                child->cost = child->pathCost + calculateCost(costMatrix, i, j, child->assigned);

                pq.push(child);
            }
        }
    }
    return 0;
}

int main(){
    int costMatrix[N][N] =
    {
        {30, 40, 70},
        {60, 20, 10},
        {40, 90, 30}
    };

    cout << "\nEl costo optimo es:\n" << findMinCost(costMatrix) << " minutos.";

    return 0;
}