class Solution:
    def constructFromPrePost(self, preorder, postorder):
        return self.helper(preorder, postorder[::-1], 0, len(preorder) - 1, 0, len(preorder) - 1)
    
    def helper(self, pre, post, pre_s, pre_e, post_s, post_e):
        if pre_s > pre_e or post_s > post_e:
            return None
        
        root = TreeNode(pre[pre_s])
        if pre_s == pre_e:
            return root
        left_len = pre.index(post[post_s + 1]) - (pre_s + 1)
        right_len = pre_e - left_len - pre_s
        
        root.left = self.helper(pre, post, pre_s + 1, pre_s + left_len, post_s + right_len + 1, post_e)
        root.right = self.helper(pre, post, pre_s + left_len + 1, pre_e, post_s + 1, post_s + right_len)
        
        return root