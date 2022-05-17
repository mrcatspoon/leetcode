from typing import Optional


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> Optional[TreeNode]:
        if not original or not cloned:
            return
        if original is target:
            return cloned

        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left
        right = self.getTargetCopy(original.right, cloned.right, target)
        if right:
            return right
