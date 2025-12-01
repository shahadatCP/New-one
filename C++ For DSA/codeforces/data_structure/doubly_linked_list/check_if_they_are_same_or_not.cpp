#include<bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* prev;
    Node(int val) : val(val), next(NULL), prev(NULL) {}
};

void insert_at_tail(Node*& head, Node*& tail, int val) {
    Node* newNode = new Node(val);
    if (!head) {
        head = tail = newNode;
    } else {
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }
}

int size_of_list(Node* head) {
    int count = 0;
    while (head) {
        count++;
        head = head->next;
    }
    return count;
}

void print_forward(Node* head, Node* head1, int sz, int sz1) {
    if (sz != sz1) {
        cout << "NO\n";
        return;
    }
    while (head) {
        if (head->val != head1->val) {
            cout << "NO\n";
            return;
        }
        head = head->next;
        head1 = head1->next;
    }
    cout << "YES\n";
}

int main() {
    Node *head = NULL, *tail = NULL, *head1 = NULL, *tail1 = NULL;
    int val;
    
    // Input first list
    while (cin >> val && val != -1) {
        insert_at_tail(head, tail, val);
    }
    
    // Input second list
    while (cin >> val && val != -1) {
        insert_at_tail(head1, tail1, val);
    }

    int sz = size_of_list(head);
    int sz1 = size_of_list(head1);
    print_forward(head, head1, sz, sz1);

    return 0;
}
