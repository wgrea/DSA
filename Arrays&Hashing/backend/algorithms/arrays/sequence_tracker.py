"""
Sequence Analysis - Longest Consecutive Sequence
Time Complexity: O(n), Space Complexity: O(n)
"""
from typing import List, Dict, Any

class SequenceTracker:
    def longest_consecutive(self, nums: List[int]) -> int:
        """
        Find length of longest consecutive sequence using hash set
        """
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Check if this is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Extend the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest = max(longest, current_streak)
        
        return longest
    
    def get_steps(self, nums: List[int]) -> List[str]:
        """Generate step-by-step explanation"""
        if not nums:
            return ["Empty array - longest consecutive sequence is 0"]
        
        steps = []
        num_set = set(nums)
        longest = 0
        longest_sequence = []
        
        steps.append(f"Input array: {nums}")
        steps.append(f"Convert to set for O(1) lookups: {sorted(num_set)}")
        
        for num in sorted(num_set):
            # Check if this is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                sequence = [current_num]
                
                steps.append(f"\nFound sequence start: {num} (no {num-1} in set)")
                
                # Extend the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    sequence.append(current_num)
                    steps.append(f"Extend sequence: {sequence} (length: {current_streak})")
                
                if current_streak > longest:
                    longest = current_streak
                    longest_sequence = sequence
                    steps.append(f"New longest sequence: {sequence} (length: {longest})")
        
        steps.append(f"\nFinal result: longest consecutive sequence length = {longest}")
        if longest_sequence:
            steps.append(f"Longest sequence: {longest_sequence}")
        
        return steps
    
    def get_visualization_data(self, nums: List[int]) -> Dict[str, Any]:
        """Generate data for visualization"""
        if not nums:
            return {"length": 0, "sequences": [], "input": nums}
        
        num_set = set(nums)
        sequences = []
        longest_length = 0
        longest_seq = []
        
        for num in sorted(num_set):
            if num - 1 not in num_set:
                # Start of a sequence
                current_num = num
                sequence = [current_num]
                
                while current_num + 1 in num_set:
                    current_num += 1
                    sequence.append(current_num)
                
                sequences.append({
                    "sequence": sequence,
                    "start": num,
                    "length": len(sequence),
                    "is_longest": len(sequence) > longest_length
                })
                
                if len(sequence) > longest_length:
                    longest_length = len(sequence)
                    longest_seq = sequence
        
        return {
            "input": nums,
            "unique_numbers": sorted(num_set),
            "sequences": sequences,
            "longest_length": longest_length,
            "longest_sequence": longest_seq,
            "total_sequences": len(sequences)
        }