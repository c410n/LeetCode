/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    typedef map<signed int, map<unsigned int, vector<signed int>>> MAP_MAP_TYPE;
    void preOrderTraverse(TreeNode* root,
                          MAP_MAP_TYPE& data,
                          signed int col,
                          unsigned int row) {
        data[col][row].push_back(root->val);
        
        if (root->left)
            preOrderTraverse(root->left, data, col-1, row+1);
        if (root->right)
            preOrderTraverse(root->right, data, col+1, row+1);
    }
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> retval;
        if (root == nullptr)
            return retval;
        
        // a std::map<K,V> is ordered based on the key, K, using std::less<K> to compare objects, by default
        MAP_MAP_TYPE data;
                    
        preOrderTraverse(root, data, 0, 0);
        
        retval.resize(data.size());
            
        int i = 0;
        for (auto data_pair : data) {
            for (auto same_cell : data_pair.second) {
                retval[i].insert(retval[i].end(), same_cell.second.begin(), same_cell.second.end());
            }
            
            i++;            
        }
        
        return retval;
    }
};