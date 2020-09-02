class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> traversal = new LinkedList<>();
        if (root == null)
            return new LinkedList<>();
        
        List<Integer> line = new LinkedList<>();
        line.add(root.val);
            
        traversal.add(line);
        
        List<TreeNode> children = new LinkedList<>(),
                        candidate_children =  new LinkedList<>();
        
        if(root.left != null)
            children.add(root.left);
        if(root.right != null)
            children.add(root.right);
        
        while(children.size() > 0) {
            line = new LinkedList<>();
            candidate_children = new LinkedList<>();
            
            for (TreeNode child : children) {
                if(child.left != null)
                    candidate_children.add(child.left);
                if(child.right != null)
                    candidate_children.add(child.right);

                line.add(child.val);
            }
            
            traversal.add(line);
            
            children = candidate_children;
        }
        
        return traversal;
    }
}