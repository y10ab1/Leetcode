/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        int sum=0;
        return check(root,sum,targetSum);
    }
    
    bool check(TreeNode* T,int sum, int targetSum){
        if(T==NULL) return false;
        sum+=T->val;
        if(T->left==NULL&&T->right==NULL&&sum!=targetSum) return false;
        if(T->left==NULL&&T->right==NULL&&sum==targetSum) return true;
        
        return check(T->left,sum,targetSum)||check(T->right,sum,targetSum);
    }
};