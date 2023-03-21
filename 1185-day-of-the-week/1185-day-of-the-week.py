class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Import the datetime module
        import datetime
        
        # Get the date object corresponding to the given day, month, and year
        date = datetime.datetime(year, month, day)
        
        # Define a list of weekday names
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        # Get the weekday index (0 for Monday, 1 for Tuesday, etc.) of the date object
        weekday_idx = date.weekday()
        
        # Return the weekday name corresponding to the weekday index
        return weekdays[weekday_idx]
