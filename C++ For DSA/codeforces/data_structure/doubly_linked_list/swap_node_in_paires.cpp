/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL || head->next == NULL) return head;

        ListNode* curr = head->next;
        ListNode* prev = head;
        head = curr;
        while(curr != NULL){
            prev->next = curr->next;
            curr->next = prev;
            if(prev->next != NULL){
                curr = prev->next->next;
            }
            else{
                curr = NULL;
            }
            ListNode* temp = prev;
            prev = prev->next;
            if(curr != NULL){
                temp->next = curr;
            }
        }
        return head;
    }
};