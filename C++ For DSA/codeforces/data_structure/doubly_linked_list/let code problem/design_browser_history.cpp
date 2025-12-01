class BrowserHistory {
public:
    class Node {
        public:
        string val;
        Node* next;
        Node* prev;
        Node(string val) { 
            this->val = val; 
            this->next = NULL;
            this->prev = NULL;
            }
    };

    Node* cur = NULL;
    BrowserHistory(string homepage) {
         cur = new Node(homepage); 
         }

    void visit(string url) {
        Node* newNode = new Node(url);
        newNode->prev = cur;
        cur->next = newNode;
        cur = newNode;
    }

    string back(int steps) {
        for(int i = 1; i <= steps; i++) {
            if(cur->prev != NULL) {
                 cur = cur->prev;
                 }
        }
        return cur->val;
    }

    string forward(int steps) {
        for(int i = 1; i <= steps; i++) {
            if(cur->next != NULL) { 
            cur = cur->next;
            }
        }
        return cur->val;
    }
};
