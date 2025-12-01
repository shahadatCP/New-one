class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* left = head;
        ListNode* right = head;

        for (int i = 1; i < k; i++) {
            left = left->next;
        }
        int sz = 0;
        ListNode* temp = head;
        while (temp != NULL) {
            sz++;
            temp = temp->next;
        }
        for (int i = 1; i <= sz - k; i++) {
            right = right->next;
        }
        swap(left->val, right->val);
        
        return head;
    }
};
