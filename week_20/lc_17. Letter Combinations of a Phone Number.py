class Solution:
    def recur(self, string: List[str], index: int, graph: dict, digits: str, answer: List[str]):
        if index == len(digits):
            answer.append(''.join(string))
            return

        digit = digits[index]
        for letter in graph[digit]:
            string.append(letter)
            self.recur(string, index + 1, graph, digits, answer)
            string.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        graph = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []

        answer = []
        string = []
        self.recur(string, 0, graph, digits, answer)

        return answer
