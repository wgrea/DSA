"""
Duplicate Detection - Contains Duplicate Algorithm
Time Complexity: O(n), Space Complexity: O(n)
"""
from typing import List, Dict, Any

class DuplicateDetector:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Check if array contains any duplicates using hash set
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def get_steps(self, nums: List[int]) -> List[str]:
        """Generate step-by-step explanation"""
        steps = []
        seen = set()
        
        steps.append("Initialize empty hash set to track seen elements")
        
        for i, num in enumerate(nums):
            if num in seen:
                steps.append(f"Step {i+1}: Found {num} already in set - DUPLICATE FOUND!")
                return steps
            seen.add(num)
            steps.append(f"Step {i+1}: Add {num} to set, current set: {list(seen)}")
        
        steps.append("No duplicates found after scanning all elements")
        return steps
    
    def get_visualization_data(self, nums: List[int]) -> Dict[str, Any]:
        """Generate data for visualization"""
        frequency = {}
        positions = {}
        
        for i, num in enumerate(nums):
            if num not in frequency:
                frequency[num] = 0
                positions[num] = []
            frequency[num] += 1
            positions[num].append(i)
        
        return {
            "frequency": frequency,
            "positions": positions,
            "has_duplicates": any(count > 1 for count in frequency.values()),
            "duplicate_elements": [num for num, count in frequency.items() if count > 1]
        }