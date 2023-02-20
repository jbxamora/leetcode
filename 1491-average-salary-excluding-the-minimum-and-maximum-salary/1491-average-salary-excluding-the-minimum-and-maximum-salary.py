class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        # Remove the minimum and maximum salary from the list
        salary.remove(max(salary))
        salary.remove(min(salary))
        
        # Calculate the average of the remaining salaries
        avg_salary = float(sum(salary)) / len(salary)
        
        return round(avg_salary, 5)
