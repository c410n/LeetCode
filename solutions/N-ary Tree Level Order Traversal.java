/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        if (root == null) {
            return new LinkedList<>();
        }
        
        List<List<Integer>> traversal = new LinkedList<>();    
        List<Integer> level = new LinkedList<>();
        List<Node> children = null;
        
        level.add(root.val);
        
        traversal.add(level);
        
        children = root.children;
                
        while (children.size() > 0) {
            
            List<Node> children_candidate = new LinkedList<>();
            level = new LinkedList<>();
            
            for(Node child : children) {
                children_candidate.addAll(child.children);    
                level.add(child.val);
            }
            
            traversal.add(level);   
            
            children = children_candidate;
        }
        
        return traversal;
    }
}