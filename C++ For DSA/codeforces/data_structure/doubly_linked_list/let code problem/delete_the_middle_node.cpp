class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if(head == NULL || head->next == NULL) return NULL;
        
        // Find size of the list
        ListNode* temp = head;
        int sz = 0;
        while(temp != NULL) {
            sz++;
            temp = temp->next;
        }

        // Traverse to middle and remove it
        ListNode* temp1 = head;
        for(int i = 1; i < sz / 2; i++) {
            temp1 = temp1->next;
        }

        temp1->next = temp1->next->next; // Remove middle node
        return head;
    }
};
