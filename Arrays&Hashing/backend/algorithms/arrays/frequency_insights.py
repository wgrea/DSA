"""
Frequency Analysis - Top K Frequent Elements
Time Complexity: O(n log k), Space Complexity: O(n + k)
"""
from typing import List, Dict, Any
from collections import Counter
import heapq

class FrequencyInsights:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Find top K frequent elements using heap
        """
        if k == 0:
            return []
        
        # Count frequencies
        frequency = Counter(nums)
        
        # Use min heap to maintain top k elements
        heap = []
        
        for num, freq in frequency.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract elements from heap
        result = [num for freq, num in heap]
        return result[::-1]  # Reverse for descending order
    
    def get_steps(self, nums: List[int], k: int) -> List[str]:
        """Generate step-by-step explanation"""
        steps = []
        frequency = Counter(nums)
        
        steps.append(f"Step 1: Count frequencies - {dict(frequency)}")
        steps.append(f"Step 2: Find top {k} frequent elements using min-heap")
        
        heap = []
        for num, freq in frequency.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
                steps.append(f"Add ({freq}, {num}) to heap: {heap}")
            elif freq > heap[0][0]:
                removed = heapq.heapreplace(heap, (freq, num))
                steps.append(f"Replace {removed} with ({freq}, {num}): {heap}")
        
        result = [num for freq, num in sorted(heap, reverse=True)]
        steps.append(f"Final result: {result}")
        
        return steps
    
    def get_visualization_data(self, nums: List[int], k: int) -> Dict[str, Any]:
        """Generate data for visualization"""
        frequency = Counter(nums)
        top_k = self.top_k_frequent(nums, k)
        
        # Prepare chart data
        chart_data = {
            "labels": list(map(str, frequency.keys())),
            "frequencies": list(frequency.values()),
            "top_k_indices": [i for i, num in enumerate(frequency.keys()) if num in top_k]
        }
        
        return {
            "frequency_map": dict(frequency),
            "top_k_elements": top_k,
            "chart_data": chart_data,
            "total_unique": len(frequency),
            "total_elements": len(nums)
        }