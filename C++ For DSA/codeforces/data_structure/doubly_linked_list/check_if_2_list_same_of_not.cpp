#include<bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* prev;
    Node(int val) {
        this->val = val;
        this->next = NULL;
        this->prev = NULL;
    }
};

void insert_at_tail(Node* &head, Node* &tail, int val) {
    Node* newNode = new Node(val);
    if (head == NULL) {
        head = newNode;
        tail = newNode;
        return;
    }
    tail->next = newNode;
    newNode->prev = tail;
    tail = newNode;
}

int find_the_size(Node* head) {
    Node* temp = head;
    int count = 0;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    return count;
}

void comp_their_value(Node* &head, Node* &head1, int size_of_head, int size_of_head1) {
    if (size_of_head != size_of_head1) {
        cout << "NO\n";
        return;
    }

    Node* temp = head;
    Node* temp1 = head1;
    while (temp != NULL) {
        if (temp->val != temp1->val) {
            cout << "NO\n";
            return;
        }
        temp = temp->next;
        temp1 = temp1->next;
    }
    cout << "YES\n";
}

int main() {
    Node* head = NULL;
    Node* tail = NULL;
    int val;
    while (true) {
        cin >> val;
        if (val == -1) break;
        insert_at_tail(head, tail, val);
    }
    
    Node* head1 = NULL;
    Node* tail1 = NULL;
    int val1;
    while (true) {
        cin >> val1;
        if (val1 == -1) break;
        insert_at_tail(head1, tail1, val1);
    }
    
    int size_of_head = find_the_size(head);
    int size_of_head1 = find_the_size(head1);
    comp_their_value(head, head1, size_of_head, size_of_head1);
}
