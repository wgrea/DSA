"""
Anagram Analysis - Valid Anagram and Group Anagrams
Time Complexity: O(n*m log m), Space Complexity: O(n*m)
"""
from typing import List, Dict, Any
from collections import defaultdict, Counter

class AnagramAnalyzer:
    def is_valid_anagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are valid anagrams
        """
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)
    
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together using sorted string as key
        """
        groups = defaultdict(list)
        
        for s in strs:
            # Use sorted string as key
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
    
    def get_steps(self, strings: List[str]) -> List[str]:
        """Generate step-by-step explanation"""
        steps = []
        
        if len(strings) == 2:
            # Valid anagram analysis
            s, t = strings[0], strings[1]
            steps.append(f"Comparing '{s}' and '{t}' for anagram validity")
            
            if len(s) != len(t):
                steps.append(f"Length mismatch: {len(s)} != {len(t)} - NOT ANAGRAMS")
                return steps
            
            count_s = Counter(s)
            count_t = Counter(t)
            
            steps.append(f"Character frequency in '{s}': {dict(count_s)}")
            steps.append(f"Character frequency in '{t}': {dict(count_t)}")
            
            if count_s == count_t:
                steps.append("Frequencies match - VALID ANAGRAMS!")
            else:
                steps.append("Frequencies don't match - NOT ANAGRAMS")
        else:
            # Group anagrams analysis
            steps.append("Grouping anagrams by sorted character key")
            groups = defaultdict(list)
            
            for i, s in enumerate(strings):
                key = ''.join(sorted(s))
                groups[key].append(s)
                steps.append(f"'{s}' -> key: '{key}' -> group: {groups[key]}")
            
            steps.append(f"Final groups: {list(groups.values())}")
        
        return steps
    
    def get_visualization_data(self, strings: List[str]) -> Dict[str, Any]:
        """Generate data for visualization"""
        if len(strings) == 2:
            # Character frequency comparison
            s, t = strings[0], strings[1]
            return {
                "type": "anagram_check",
                "string1": {"text": s, "frequency": dict(Counter(s))},
                "string2": {"text": t, "frequency": dict(Counter(t))},
                "is_anagram": self.is_valid_anagram(s, t)
            }
        else:
            # Anagram groups
            groups = self.group_anagrams(strings)
            keys = {}
            
            for s in strings:
                keys[s] = ''.join(sorted(s))
            
            return {
                "type": "anagram_groups",
                "groups": groups,
                "keys": keys,
                "group_count": len(groups)
            }