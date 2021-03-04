/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        ListNode *ptA=headA,*ptB=headB;
        int cntA=0,cntB=0;
        while(ptA!=NULL){
            ptA=ptA->next;
            ++cntA;
        }
        while(ptB!=NULL){
            ptB=ptB->next;
            ++cntB;
        }
        ptA=headA;
        ptB=headB;
        int offset=0;
        
        if((offset=(cntA-cntB))>0){
            for(int i=0;i<offset;++i)
                ptA=ptA->next;
        }else if((offset=(cntB-cntA))>0){
            for(int i=0;i<offset;++i)
                ptB=ptB->next;
        }
        /*cout<<cntA;
        cout<<cntB;
        cout<<offset;
        cout<<ptA->val;
        cout<<ptB->val;
        */
        for(int i=0;i<min(cntA,cntB);++i){
            if(ptA==ptB){
                return ptA;
            }
            ptA=ptA->next;
            ptB=ptB->next;
        }
        return NULL;
    }
};