"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    importance = 0

    def traverse(self, employees, ids):
        for employee in employees:
            if employee.id in ids:
                self.importance += employee.importance
                self.traverse(employees, employee.subordinates)

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.traverse(employees, [id])
        return self.importance
