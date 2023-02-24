from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # Initialize minimum distance and index 
        min_distance = float('inf')
        min_index = -1
    
        # Iterate over the array of points
        for i in range(len(points)):
            xi, yi = points[i]

            # Check if the point is valid
            if xi == x or yi == y:
                # Calculate the Manhattan distance to the given point
                distance = abs(x - xi) + abs(y - yi)

                # If the distance is smaller than the current minimum distance, update the minimum distance and index
                if distance < min_distance:
                    min_distance = distance
                    min_index = i
        
        # Return the index of the point with the smallest distance, or -1 if no valid points are found
        return min_index

# Driver code to test the nearestValidPoint function
if __name__ == "__main__":
    sol = Solution()
    x = 3
    y = 4
    points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
    result = sol.nearestValidPoint(x, y, points)
    print(result)  # Expected output: 2
