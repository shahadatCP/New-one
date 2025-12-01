class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* left = head;
        ListNode* temp = head;
        int count = 0;
        
        while(temp != NULL) {
            count++;
            temp = temp->next;
        }
        if (n == count) {
            ListNode* newHead = head->next;
            delete head; 
            return newHead;
        }
        for (int i = 1; i < count - n; i++) {
            left = left->next;
        }
        left->next = left->next->next;
        return head;
    }
};
