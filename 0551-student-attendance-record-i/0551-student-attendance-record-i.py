class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0
        
        for i in range(len(s)):
            # If the current character is 'A', increment absent_count
            if s[i] == 'A':
                absent_count += 1
                # If there are more than one 'A's, return False
                if absent_count > 1:
                    return False
            
            # If the current character is 'L', increment late_count
            if s[i] == 'L':
                late_count += 1
                # If there are three consecutive 'L's, return False
                if late_count > 2 and s[i-1] == s[i-2] == s[i]:
                    return False
            else:
                late_count = 0  # Reset late_count if current character is not 'L'
        
        # If there are no issues with attendance, return True
        return True
