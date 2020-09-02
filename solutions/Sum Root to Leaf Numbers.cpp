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
    void you_got_to_work_bitch(TreeNode* node, vector<int> number, vector<vector<int>>& encoded_result) {
        number.push_back(node->val);
        
        if (!node->left && !node->right)
            encoded_result.push_back(number);
        else {
            if (node->left)
                you_got_to_work_bitch(node->left, number, encoded_result);
            if (node->right)
                you_got_to_work_bitch(node->right, number, encoded_result);
        }
    }
public:
    int sumNumbers(TreeNode* root) {
        if (!root)
            return 0;
        
        vector<vector<int>> numbers;
        vector<int> stub;
        
        you_got_to_work_bitch(root, stub, numbers);
        
        int answer = 0;
        
        for (vector<int> data_array : numbers) {
            int tmp = 0;
            
            for (int num : data_array) {
                tmp = tmp*10+num;
            }
            
            answer+=tmp;
        }
        
        return answer;
    }
};