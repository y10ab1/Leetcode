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
    queue<TreeNode*> q;
    vector<int> temp;
    vector<vector<int>> output;
    
    int level=1;
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root){
            return output;
        }
        
        q.push(root);
        while(!q.empty()){
            int size=q.size();
            for(int i=0; i<size; ++i){
                TreeNode *current=q.front();
                temp.push_back(current->val);
                q.pop();
                if(current->left){
                    q.push(current->left);
                }
                if(current->right){
                    q.push(current->right);
                }
            }
            output.push_back(temp);
            temp.clear();

            
        }

        return output;
    }
};