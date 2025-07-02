"""
SmartPack Backend - FastAPI server for DSA pattern analysis
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uvicorn

# Import algorithm modules
from algorithms.arrays.duplicate_detector import DuplicateDetector
from algorithms.arrays.anagram_analyzer import AnagramAnalyzer
from algorithms.arrays.frequency_insights import FrequencyInsights
from algorithms.arrays.pair_calculator import PairCalculator
from algorithms.arrays.sequence_tracker import SequenceTracker
from algorithms.strings.encoder_decoder import EncoderDecoder

app = FastAPI(
    title="SmartPack API",
    description="Intelligent DSA Pattern Explorer Backend API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class TextAnalysisRequest(BaseModel):
    text: str
    options: Optional[Dict[str, Any]] = {}

class NumericAnalysisRequest(BaseModel):
    numbers: List[int]
    target: Optional[int] = None
    k: Optional[int] = None
    options: Optional[Dict[str, Any]] = {}

class AnagramRequest(BaseModel):
    strings: List[str]
    options: Optional[Dict[str, Any]] = {}

class AnalysisResponse(BaseModel):
    result: Any
    algorithm: str
    complexity: Dict[str, str]
    explanation: str
    steps: List[str]
    visualization_data: Optional[Dict[str, Any]] = None

# Initialize algorithm instances
duplicate_detector = DuplicateDetector()
anagram_analyzer = AnagramAnalyzer()
frequency_insights = FrequencyInsights()
pair_calculator = PairCalculator()
sequence_tracker = SequenceTracker()
encoder_decoder = EncoderDecoder()

@app.get("/")
async def root():
    return {"message": "SmartPack DSA Pattern Explorer API", "version": "1.0.0"}

@app.post("/analyze/duplicates", response_model=AnalysisResponse)
async def analyze_duplicates(request: NumericAnalysisRequest):
    """Detect duplicates in numeric array"""
    try:
        result = duplicate_detector.contains_duplicate(request.numbers)
        return AnalysisResponse(
            result=result,
            algorithm="Contains Duplicate (Hash Set)",
            complexity={"time": "O(n)", "space": "O(n)"},
            explanation="Uses hash set to track seen elements in single pass",
            steps=duplicate_detector.get_steps(request.numbers),
            visualization_data=duplicate_detector.get_visualization_data(request.numbers)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/anagrams", response_model=AnalysisResponse)
async def analyze_anagrams(request: AnagramRequest):
    """Analyze anagrams in string array"""
    try:
        if len(request.strings) == 2:
            # Valid anagram check
            result = anagram_analyzer.is_valid_anagram(request.strings[0], request.strings[1])
            algorithm = "Valid Anagram (Frequency Count)"
        else:
            # Group anagrams
            result = anagram_analyzer.group_anagrams(request.strings)
            algorithm = "Group Anagrams (Hash Map)"
        
        return AnalysisResponse(
            result=result,
            algorithm=algorithm,
            complexity={"time": "O(n*m log m)", "space": "O(n*m)"},
            explanation="Groups strings by sorted character frequency",
            steps=anagram_analyzer.get_steps(request.strings),
            visualization_data=anagram_analyzer.get_visualization_data(request.strings)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/frequency", response_model=AnalysisResponse)
async def analyze_frequency(request: NumericAnalysisRequest):
    """Find top K frequent elements"""
    try:
        k = request.k or 1
        result = frequency_insights.top_k_frequent(request.numbers, k)
        return AnalysisResponse(
            result=result,
            algorithm="Top K Frequent Elements (Heap)",
            complexity={"time": "O(n log k)", "space": "O(n + k)"},
            explanation="Uses frequency counter and min-heap for efficient top-K selection",
            steps=frequency_insights.get_steps(request.numbers, k),
            visualization_data=frequency_insights.get_visualization_data(request.numbers, k)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/pairs", response_model=AnalysisResponse)
async def analyze_pairs(request: NumericAnalysisRequest):
    """Find two sum pairs"""
    try:
        if request.target is None:
            raise HTTPException(status_code=400, detail="Target value required for pair analysis")
        
        result = pair_calculator.two_sum(request.numbers, request.target)
        return AnalysisResponse(
            result=result,
            algorithm="Two Sum (Hash Map)",
            complexity={"time": "O(n)", "space": "O(n)"},
            explanation="Uses hash map to find complement in single pass",
            steps=pair_calculator.get_steps(request.numbers, request.target),
            visualization_data=pair_calculator.get_visualization_data(request.numbers, request.target)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/products", response_model=AnalysisResponse)
async def analyze_products(request: NumericAnalysisRequest):
    """Calculate product of array except self"""
    try:
        result = pair_calculator.product_except_self(request.numbers)
        return AnalysisResponse(
            result=result,
            algorithm="Product of Array Except Self",
            complexity={"time": "O(n)", "space": "O(1)"},
            explanation="Uses left and right pass to calculate products without division",
            steps=pair_calculator.get_product_steps(request.numbers),
            visualization_data=pair_calculator.get_product_visualization_data(request.numbers)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/sequences", response_model=AnalysisResponse)
async def analyze_sequences(request: NumericAnalysisRequest):
    """Find longest consecutive sequence"""
    try:
        result = sequence_tracker.longest_consecutive(request.numbers)
        return AnalysisResponse(
            result=result,
            algorithm="Longest Consecutive Sequence (Hash Set)",
            complexity={"time": "O(n)", "space": "O(n)"},
            explanation="Uses hash set to identify sequence starts and extend efficiently",
            steps=sequence_tracker.get_steps(request.numbers),
            visualization_data=sequence_tracker.get_visualization_data(request.numbers)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/encoding", response_model=AnalysisResponse)
async def analyze_encoding(request: AnagramRequest):
    """Encode and decode strings safely"""
    try:
        encoded = encoder_decoder.encode(request.strings)
        decoded = encoder_decoder.decode(encoded)
        
        return AnalysisResponse(
            result={"encoded": encoded, "decoded": decoded, "valid": decoded == request.strings},
            algorithm="Encode/Decode Strings (Length Prefix)",
            complexity={"time": "O(n)", "space": "O(n)"},
            explanation="Uses length prefix encoding to handle arbitrary delimiters safely",
            steps=encoder_decoder.get_steps(request.strings),
            visualization_data=encoder_decoder.get_visualization_data(request.strings)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/algorithms/mapping")
async def get_algorithm_mapping():
    """Get DSA pattern to feature mapping"""
    return {
        "patterns": [
            {
                "pattern": "Hash Set/Map",
                "features": ["Duplicate Detection", "Anagram Analysis", "Frequency Counting"],
                "real_world": ["Database Deduplication", "Spam Detection", "Log Analysis"],
                "blind75": ["Contains Duplicate", "Valid Anagram", "Group Anagrams"]
            },
            {
                "pattern": "Two Pointers/Complement",
                "features": ["Pair Finding", "Sum Calculations"],
                "real_world": ["Recommendation Systems", "Financial Analysis"],
                "blind75": ["Two Sum", "3Sum"]
            },
            {
                "pattern": "Prefix/Suffix Arrays",
                "features": ["Product Calculations", "Range Queries"],
                "real_world": ["Stock Analysis", "Performance Metrics"],
                "blind75": ["Product of Array Except Self"]
            },
            {
                "pattern": "Union Find/Consecutive",
                "features": ["Sequence Detection", "Graph Components"],
                "real_world": ["Social Networks", "System Dependencies"],
                "blind75": ["Longest Consecutive Sequence"]
            },
            {
                "pattern": "String Processing",
                "features": ["Safe Encoding", "Data Serialization"],
                "real_world": ["API Design", "Data Storage"],
                "blind75": ["Encode and Decode Strings"]
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)