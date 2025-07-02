"""
String Encoding/Decoding - Encode and Decode Strings
Time Complexity: O(n), Space Complexity: O(n)
"""
from typing import List, Dict, Any

class EncoderDecoder:
    def encode(self, strs: List[str]) -> str:
        """
        Encode list of strings using length prefix
        Format: "length#string" for each string
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    
    def decode(self, s: str) -> List[str]:
        """
        Decode string back to list of strings
        """
        result = []
        i = 0
        
        while i < len(s):
            # Find the delimiter '#'
            delimiter_pos = s.find('#', i)
            if delimiter_pos == -1:
                break
            
            # Extract length
            length = int(s[i:delimiter_pos])
            
            # Extract string of specified length
            start = delimiter_pos + 1
            end = start + length
            result.append(s[start:end])
            
            # Move to next encoded string
            i = end
        
        return result
    
    def get_steps(self, strs: List[str]) -> List[str]:
        """Generate step-by-step explanation"""
        steps = []
        steps.append(f"Input strings: {strs}")
        
        # Encoding steps
        steps.append("\nEncoding process:")
        encoded = ""
        for i, s in enumerate(strs):
            prefix = str(len(s)) + "#"
            encoded += prefix + s
            steps.append(f"String {i+1}: '{s}' -> length={len(s)} -> '{prefix}{s}'")
        
        steps.append(f"Final encoded string: '{encoded}'")
        
        # Decoding steps
        steps.append("\nDecoding process:")
        result = []
        i = 0
        string_num = 1
        
        while i < len(encoded):
            delimiter_pos = encoded.find('#', i)
            if delimiter_pos == -1:
                break
            
            length = int(encoded[i:delimiter_pos])
            start = delimiter_pos + 1
            end = start + length
            decoded_string = encoded[start:end]
            result.append(decoded_string)
            
            steps.append(f"String {string_num}: length={length} -> extract '{decoded_string}' from position {start} to {end-1}")
            
            i = end
            string_num += 1
        
        steps.append(f"Final decoded strings: {result}")
        steps.append(f"Encoding/Decoding successful: {result == strs}")
        
        return steps
    
    def get_visualization_data(self, strs: List[str]) -> Dict[str, Any]:
        """Generate data for visualization"""
        encoded = self.encode(strs)
        decoded = self.decode(encoded)
        
        # Track encoding process
        encoding_steps = []
        current_pos = 0
        
        for i, s in enumerate(strs):
            prefix = str(len(s)) + "#"
            encoding_steps.append({
                "string_index": i,
                "original": s,
                "length": len(s),
                "prefix": prefix,
                "encoded_part": prefix + s,
                "position": current_pos,
                "end_position": current_pos + len(prefix + s)
            })
            current_pos += len(prefix + s)
        
        # Track decoding process
        decoding_steps = []
        i = 0
        string_num = 0
        
        while i < len(encoded) and string_num < len(strs):
            delimiter_pos = encoded.find('#', i)
            if delimiter_pos == -1:
                break
            
            length = int(encoded[i:delimiter_pos])
            start = delimiter_pos + 1
            end = start + length
            decoded_string = encoded[start:end]
            
            decoding_steps.append({
                "string_index": string_num,
                "length": length,
                "start_pos": start,
                "end_pos": end,
                "decoded": decoded_string
            })
            
            i = end
            string_num += 1
        
        return {
            "input": strs,
            "encoded": encoded,
            "decoded": decoded,
            "is_valid": decoded == strs,
            "encoding_steps": encoding_steps,
            "decoding_steps": decoding_steps,
            "encoded_length": len(encoded),
            "compression_ratio": len(encoded) / sum(len(s) for s in strs) if strs else 1
        }