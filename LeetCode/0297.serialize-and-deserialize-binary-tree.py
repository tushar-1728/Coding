# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        res = ""
        if root:
            node_count = self.countNode(root)
            queue = [root]
            res = []
            while queue:
                temp = queue.pop(0)
                if temp != None:
                    res += [str(temp.val)]
                    queue += [temp.left, temp.right]
                    node_count -= 1
                else:
                    res += ["null"]
            res = ".".join(res)
            return res

    def deserialize(self, data):
        root = None
        if data:
            data = list(data.split("."))
            root = TreeNode(data[0])
            queue = [[root, 0]]
            nc = 0
            n = len(data)
            while queue:
                node, i = queue.pop(0)
                if node != None:
                    li = 2*i+1-2*nc
                    ri = 2*i+2-2*nc
                    if li < n:
                        if data[li] != "null":
                            node.left = TreeNode(int(data[li]))
                        queue.append([node.left, li])
                    if ri < n:
                        if data[ri] != "null":
                            node.right = TreeNode(int(data[ri]))
                        queue.append([node.right, ri])
                else:
                    nc += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))