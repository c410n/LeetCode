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
public:
    static const int RESERVED = 8; // How many vector cells are reserved by default
    
    void RetrospectTheValues(
        TreeNode* root,
        int nodeValue,
        map<int, map<int, vector<int>>>& preliminary,
        int level) {
        
        map<int, map<int, vector<int>>>::iterator col_it = preliminary.find(nodeValue);
        map<int, vector<int>>::iterator row_it;
            
        if (col_it == preliminary.end()) {
            map<signed int, vector<int>> column;
            
            vector<int> vals;
            vals.reserve(RESERVED);
            
            column[level] = vals;        
            preliminary[nodeValue] = column;
        } else if ((row_it = col_it->second.find(level)) == col_it->second.end()) {
            if (row_it == col_it->second.end()) {
                vector<int> vals;
                vals.reserve(RESERVED);

                col_it->second[level] = vals;
            }             
        }           
        
        preliminary[nodeValue][level].push_back(root->val);
                
        if (root->left)
            RetrospectTheValues(root->left, nodeValue-1, preliminary, level - 1);
        if (root->right)
            RetrospectTheValues(root->right, nodeValue+1, preliminary, level - 1);
    }
    
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        map<int, map<int, vector<int>>> preliminary;
        
        RetrospectTheValues(root, 0, preliminary, 0);
        
        int analysis_i = 0;
        vector<vector<int> > analysis;
        analysis.resize(preliminary.size());
                
        for (auto column : preliminary) {
            vector<int> vals;
            vals.reserve(column.second.size());
            
            map<int, vector<int>>::reverse_iterator riterator = column.second.rbegin();            
            while (riterator != column.second.rend()) {
                vector<int> vals_same_place;
                vals_same_place.reserve(riterator->second.size());
                for (auto val : riterator->second) {
                    vals_same_place.push_back(val);
                }
                sort(vals_same_place.begin(), vals_same_place.end());
                vals.insert(vals.end(),vals_same_place.begin(),vals_same_place.end());
                
                riterator++;
            }            
            analysis[analysis_i] = vals;
            analysis_i++;
        }
        
        return analysis;
    }
};