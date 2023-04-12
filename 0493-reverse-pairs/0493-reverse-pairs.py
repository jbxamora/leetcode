class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr: List[int], start: int, end: int) -> int:
            if start >= end:
                return 0

            mid = start + (end - start) // 2
            count = merge_sort(arr, start, mid) + merge_sort(arr, mid + 1, end)

            # Count important reverse pairs
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if arr[i] > 2 * arr[j]:
                    count += mid - i + 1
                    j += 1
                else:
                    i += 1

            # Merge two sorted halves
            merged = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if arr[i] <= arr[j]:
                    merged.append(arr[i])
                    i += 1
                else:
                    merged.append(arr[j])
                    j += 1

            while i <= mid:
                merged.append(arr[i])
                i += 1

            while j <= end:
                merged.append(arr[j])
                j += 1

            # Update the original array
            for i in range(len(merged)):
                arr[start + i] = merged[i]

            return count

        return merge_sort(nums, 0, len(nums) - 1)
