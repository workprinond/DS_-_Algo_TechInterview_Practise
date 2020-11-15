class Solution:
 def generateParenthesis(self, n: int) -> List[str]:
    if n == 0:
        return []
    elif n == 1:
        return ["()"]
    else:
        pairs = set()
        for word in self.generateParenthesis(n-1):
            for i in range(0, len(word)):
                pairs.add(word[:i] + "()" + word[i:])
        return pairs