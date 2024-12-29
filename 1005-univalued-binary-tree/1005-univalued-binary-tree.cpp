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
    void uniValued(TreeNode* root, int n, bool& flg){
        if(!root) return;
        if(root->val != n) {flg=false; return;}
        uniValued(root->left, n, flg);
        uniValued(root->right, n, flg);
    }

    bool isUnivalTree(TreeNode* root) {
        if(!root) return true;
        bool flg=true;
        int n=root->val;
        uniValued(root, n, flg);
        return flg;
    }
};