"""
Pair and Product Calculations - Two Sum and Product of Array Except Self
Time Complexity: O(n), Space Complexity: O(n) for Two Sum, O(1) for Product
"""
from typing import List, Dict, Any, Optional

class PairCalculator:
    def two_sum(self, nums: List[int], target: int) -> Optional[List[int]]:
        """
        Find two numbers that add up to target using hash map
        """
        complement_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                return [complement_map[complement], i]
            complement_map[num] = i
        
        return None  # No solution found
    
    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        Calculate product of array except self without division
        """
        n = len(nums)
        result = [1] * n
        
        # Left pass: multiply by all elements to the left
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        
        # Right pass: multiply by all elements to the right
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
    
    def get_steps(self, nums: List[int], target: int) -> List[str]:
        """Generate step-by-step explanation for Two Sum"""
        steps = []
        complement_map = {}
        
        steps.append(f"Target: {target}")
        steps.append("Initialize empty hash map for complements")
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                steps.append(f"Step {i+1}: Found complement {complement} at index {complement_map[complement]}")
                steps.append(f"Solution: indices [{complement_map[complement]}, {i}] = [{complement}, {num}]")
                return steps
            
            complement_map[num] = i
            steps.append(f"Step {i+1}: Add {num} -> index {i} to map")
            steps.append(f"Current map: {complement_map}")
        
        steps.append("No solution found")
        return steps
    
    def get_product_steps(self, nums: List[int]) -> List[str]:
        """Generate step-by-step explanation for Product Except Self"""
        steps = []
        n = len(nums)
        result = [1] * n
        
        steps.append(f"Input array: {nums}")
        steps.append(f"Initialize result array: {result}")
        
        # Left pass
        steps.append("\nLeft pass - multiply by elements to the left:")
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
            steps.append(f"result[{i}] = result[{i-1}] * nums[{i-1}] = {result[i-1]} * {nums[i-1]} = {result[i]}")
        
        steps.append(f"After left pass: {result}")
        
        # Right pass
        steps.append("\nRight pass - multiply by elements to the right:")
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            steps.append(f"result[{i}] *= right_product({right_product}) = {result[i]}")
            right_product *= nums[i]
            steps.append(f"Update right_product: {right_product}")
        
        steps.append(f"Final result: {result}")
        return steps
    
    def get_visualization_data(self, nums: List[int], target: int) -> Dict[str, Any]:
        """Generate data for Two Sum visualization"""
        solution = self.two_sum(nums, target)
        complement_map = {}
        search_path = []
        
        for i, num in enumerate(nums):
            complement = target - num
            search_path.append({
                "index": i,
                "value": num,
                "complement": complement,
                "found": complement in complement_map,
                "map_state": dict(complement_map)
            })
            if complement in complement_map:
                break
            complement_map[num] = i
        
        return {
            "solution": solution,
            "target": target,
            "search_path": search_path,
            "array": nums
        }
    
    def get_product_visualization_data(self, nums: List[int]) -> Dict[str, Any]:
        """Generate data for Product Except Self visualization"""
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        
        # Calculate left products
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]
        
        # Calculate right products
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]
        
        final_result = [left_products[i] * right_products[i] for i in range(n)]
        
        return {
            "input": nums,
            "left_products": left_products,
            "right_products": right_products,
            "final_result": final_result,
            "steps": {
                "left_pass": list(enumerate(left_products)),
                "right_pass": list(enumerate(right_products))
            }
        }