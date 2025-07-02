# 📦 SmartPack - Intelligent DSA Pattern Explorer

A modern web application that helps users explore text and numeric data through the lens of foundational Data Structures & Algorithms patterns, especially those from the famous "Blind 75" collection.

![SmartPack Demo](https://via.placeholder.com/800x400/3B82F6/FFFFFF?text=SmartPack+DSA+Explorer)

## 🚀 Features

### Core Algorithm Implementations
- **🔍 Duplicate Detector** - Hash-based duplicate detection (`Contains Duplicate`)
- **🔠 Anagram Analyzer** - Frequency mapping for anagrams (`Valid Anagram`, `Group Anagrams`)
- **📊 Frequency Insights** - Heap-optimized top-K analysis (`Top K Frequent Elements`)
- **➕ Pair Calculator** - Complement-based pair finding (`Two Sum`)
- **✖️ Product Calculator** - Efficient array products (`Product of Array Except Self`)
- **📈 Sequence Tracker** - Consecutive sequence detection (`Longest Consecutive Sequence`)
- **🔐 Safe Encoder/Decoder** - Length-prefix string encoding (`Encode and Decode Strings`)

### Interactive Features
- **Real-time Algorithm Execution** with step-by-step visualization
- **Interactive Charts** powered by Chart.js
- **Complexity Analysis** with time/space breakdown
- **Pattern Mapping** connecting DSA concepts to real-world applications
- **Responsive Design** optimized for all devices

## 🛠️ Tech Stack

### Frontend
- **Framework**: Svelte + TypeScript
- **Styling**: Custom CSS with design system
- **Visualization**: Chart.js
- **Build Tool**: Vite

### Backend
- **Framework**: FastAPI (Python 3.9+)
- **API Design**: RESTful with automatic OpenAPI docs
- **Algorithm Implementation**: Pure Python with type hints

### Development
- **Hot Reload**: Vite HMR for frontend, Uvicorn for backend
- **Type Safety**: Full TypeScript integration
- **Modular Architecture**: Clean separation of concerns

## 📋 Quick Start

### Prerequisites
- Node.js 16+ and npm/yarn
- Python 3.9+
- pip for Python package management

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/smartpack.git
   cd smartpack
   ```

2. **Install frontend dependencies**
   ```bash
   npm install
   ```

3. **Set up backend environment**
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

4. **Start development servers**
   ```bash
   # Start both frontend and backend
   npm run dev:full
   
   # Or start individually:
   npm run dev          # Frontend only (http://localhost:5173)
   npm run dev:backend  # Backend only (http://localhost:8000)
   ```

5. **Open your browser**
   - Frontend: `http://localhost:5173`
   - Backend API docs: `http://localhost:8000/docs`

## 🏗️ Project Structure

```
smartpack/
├── src/                          # Frontend source
│   ├── components/              # Reusable UI components
│   │   ├── AlgorithmCard.svelte
│   │   ├── AlgorithmRunner.svelte
│   │   ├── ChartVisualization.svelte
│   │   └── ...
│   ├── services/               # API communication
│   │   └── api.ts
│   ├── templates/              # Component templates
│   │   └── _template.svelte
│   └── App.svelte             # Main application
├── backend/                    # Python FastAPI backend
│   ├── algorithms/            # Algorithm implementations
│   │   ├── arrays/           # Array & hashing algorithms
│   │   │   ├── duplicate_detector.py
│   │   │   ├── anagram_analyzer.py
│   │   │   └── ...
│   │   └── strings/          # String algorithms
│   │       └── encoder_decoder.py
│   ├── templates/            # Algorithm templates
│   │   └── _template.py
│   ├── main.py              # FastAPI application
│   └── requirements.txt     # Python dependencies
├── package.json            # Frontend dependencies
└── README.md              # This file
```

## 🧠 Algorithm Patterns & Real-World Connections

| DSA Pattern | SmartPack Features | Real-World Applications | Blind 75 Problems |
|-------------|-------------------|------------------------|------------------|
| **Hash Set/Map** | Duplicate Detection, Anagram Analysis | Database Deduplication, Spam Detection | Contains Duplicate, Valid Anagram |
| **Two Pointers** | Pair Finding, Sum Calculations | Recommendation Systems, Financial Analysis | Two Sum, 3Sum |
| **Prefix Arrays** | Product Calculations, Range Queries | Stock Analysis, Performance Metrics | Product of Array Except Self |
| **Union Find** | Sequence Detection, Graph Components | Social Networks, System Dependencies | Longest Consecutive Sequence |
| **String Processing** | Safe Encoding, Data Serialization | API Design, Data Storage | Encode and Decode Strings |

## 📚 API Documentation

### Core Endpoints

- `POST /analyze/duplicates` - Detect duplicates in numeric arrays
- `POST /analyze/anagrams` - Analyze anagrams in string arrays
- `POST /analyze/frequency` - Find top-K frequent elements
- `POST /analyze/pairs` - Find two-sum pairs
- `POST /analyze/products` - Calculate array products except self
- `POST /analyze/sequences` - Find longest consecutive sequences
- `POST /analyze/encoding` - Encode/decode string arrays

### Request/Response Format

```typescript
// Request
interface NumericAnalysisRequest {
  numbers: number[];
  target?: number;  // For two-sum problems
  k?: number;       // For top-K problems
}

// Response
interface AnalysisResponse {
  result: any;
  algorithm: string;
  complexity: { time: string; space: string };
  explanation: string;
  steps: string[];
  visualization_data?: Record<string, any>;
}
```

## 🔄 Next.js Migration Guide

Planning to convert to Next.js? Here's what you need to know:

### Frontend Migration
1. **Components**: Svelte components → React components with hooks
2. **Routing**: File-based routing in Next.js
3. **API Calls**: Replace current API service with Next.js API routes or keep FastAPI
4. **Styling**: Convert CSS to CSS Modules or styled-components

### Backend Options
- **Keep FastAPI**: Continue using as external API
- **Next.js API Routes**: Migrate Python logic to TypeScript/JavaScript
- **Hybrid**: Use Next.js for frontend, FastAPI for complex algorithms

### Migration Steps
```bash
# 1. Create Next.js project
npx create-next-app@latest smartpack-next --typescript

# 2. Copy and convert components
# 3. Set up API integration
# 4. Migrate styling system
# 5. Update deployment configuration
```

## 🤝 Contributing

### Adding New Algorithms

1. **Backend**: Copy `backend/templates/_template.py`
   ```python
   # backend/algorithms/arrays/new_algorithm.py
   class NewAlgorithm:
       def solve(self, input_data):
           # Implementation
           pass
       
       def get_steps(self, input_data):
           # Step-by-step explanation
           pass
   ```

2. **Frontend**: Copy `src/templates/_template.svelte`
   ```typescript
   // Add to algorithm list in FeatureGrid.svelte
   {
       id: 'new-algo',
       title: 'New Algorithm',
       // ... configuration
   }
   ```

3. **API Integration**: Update `main.py` and `api.ts`

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new algorithms
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📊 Performance & Complexity

All algorithms include detailed complexity analysis:

- **Time Complexity**: Big O notation for time requirements
- **Space Complexity**: Memory usage analysis
- **Real-world Performance**: Practical considerations and optimizations
- **Scalability Notes**: How algorithms perform with large datasets

## 🔧 Configuration & Customization

### Environment Variables
```bash
# Backend configuration
API_HOST=localhost
API_PORT=8000
CORS_ORIGINS=http://localhost:5173

# Frontend configuration  
VITE_API_BASE_URL=http://localhost:8000
```

### Styling Customization
The design system uses CSS custom properties for easy theming:

```css
:root {
  --primary-500: #3b82f6;
  --secondary-500: #14b8a6;
  --accent-500: #f97316;
  /* ... more variables */
}
```

## 🚀 Deployment

### Frontend (Netlify/Vercel)
```bash
npm run build
# Upload dist/ folder
```

### Backend (Railway/Heroku)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Docker Deployment
```dockerfile
# Multi-stage Docker build available
# See Dockerfile for full configuration
```

## 📈 Roadmap

- [ ] **More Algorithms**: Tree, Graph, and Dynamic Programming patterns
- [ ] **Advanced Visualizations**: 3D charts and interactive algorithm animations
- [ ] **Code Generation**: Export algorithm implementations in multiple languages
- [ ] **Learning Paths**: Guided tutorials for different skill levels
- [ ] **Collaboration Features**: Share and discuss algorithm solutions
- [ ] **Performance Benchmarking**: Compare algorithm implementations
- [ ] **Mobile App**: React Native version for mobile learning

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Blind 75**: The legendary LeetCode problem collection
- **NeetCode**: Excellent algorithm explanations and patterns
- **Svelte Team**: For the amazing framework
- **FastAPI Team**: For the high-performance Python framework
- **Chart.js**: For beautiful data visualizations

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/smartpack/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/smartpack/discussions)
- **Email**: support@smartpack.dev
- **Discord**: Join our learning community

---

**Built with ❤️ for DSA learners everywhere**

*SmartPack - Where algorithms meet intuition*