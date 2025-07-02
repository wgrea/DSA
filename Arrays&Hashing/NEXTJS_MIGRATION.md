# 🔄 Next.js Migration Guide for SmartPack

This guide provides a comprehensive roadmap for converting SmartPack from Svelte + FastAPI to Next.js, maintaining all functionality while leveraging Next.js features.

## 📋 Migration Overview

### Current Architecture
```
Svelte Frontend + FastAPI Backend
├── Client-side rendering
├── Separate API server
└── Manual API integration
```

### Target Architecture
```
Next.js Full-Stack Application
├── Server-side rendering (SSR/SSG)
├── API routes for algorithms
└── Integrated frontend/backend
```

## 🚀 Migration Strategy

### Phase 1: Project Setup

1. **Initialize Next.js Project**
   ```bash
   npx create-next-app@latest smartpack-next --typescript --tailwind --eslint --app
   cd smartpack-next
   ```

2. **Install Dependencies**
   ```bash
   npm install chart.js chartjs-adapter-date-fns date-fns
   npm install axios swr  # For API calls and caching
   npm install @types/node  # For server-side TypeScript
   ```

3. **Project Structure Setup**
   ```
   smartpack-next/
   ├── app/                    # App Router (Next.js 13+)
   │   ├── components/        # React components
   │   ├── api/              # API routes
   │   ├── algorithms/       # Algorithm pages
   │   └── globals.css       # Global styles
   ├── lib/                  # Utility functions
   │   ├── algorithms/       # Algorithm implementations
   │   └── api.ts           # API utilities
   ├── types/               # TypeScript definitions
   └── public/             # Static assets
   ```

### Phase 2: Component Migration

#### Svelte → React Component Conversion

**Svelte Component Example:**
```svelte
<!-- AlgorithmCard.svelte -->
<script lang="ts">
  export let feature: any;
  let showRunner = false;
  
  function toggleRunner() {
    showRunner = !showRunner;
  }
</script>

<div class="algorithm-card">
  <h3>{feature.title}</h3>
  <button on:click={toggleRunner}>
    {showRunner ? 'Hide' : 'Show'} Runner
  </button>
  {#if showRunner}
    <AlgorithmRunner algorithm={feature.id} />
  {/if}
</div>
```

**React Component Conversion:**
```tsx
// components/AlgorithmCard.tsx
'use client'
import { useState } from 'react'
import AlgorithmRunner from './AlgorithmRunner'

interface AlgorithmCardProps {
  feature: any
}

export default function AlgorithmCard({ feature }: AlgorithmCardProps) {
  const [showRunner, setShowRunner] = useState(false)
  
  const toggleRunner = () => {
    setShowRunner(!showRunner)
  }
  
  return (
    <div className="algorithm-card">
      <h3>{feature.title}</h3>
      <button onClick={toggleRunner}>
        {showRunner ? 'Hide' : 'Show'} Runner
      </button>
      {showRunner && (
        <AlgorithmRunner algorithm={feature.id} />
      )}
    </div>
  )
}
```

#### Key Conversion Patterns

| Svelte | React | Notes |
|--------|-------|-------|
| `<script lang="ts">` | `'use client'` + hooks | Client component directive |
| `export let prop` | `interface Props` | TypeScript interfaces |
| `let variable` | `useState()` | State management |
| `$: reactive` | `useEffect()` | Side effects |
| `on:click` | `onClick` | Event handlers |
| `{#if condition}` | `{condition &&}` | Conditional rendering |
| `{#each items}` | `{items.map()}` | List rendering |

### Phase 3: Algorithm Implementation

#### Option A: Keep FastAPI Backend
```typescript
// lib/api.ts - External API calls
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export async function analyzeData(algorithm: string, data: any) {
  const response = await fetch(`${API_BASE_URL}/analyze/${algorithm}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  return response.json()
}
```

#### Option B: Migrate to Next.js API Routes
```typescript
// app/api/analyze/duplicates/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { DuplicateDetector } from '@/lib/algorithms/duplicate-detector'

export async function POST(request: NextRequest) {
  try {
    const { numbers } = await request.json()
    const detector = new DuplicateDetector()
    const result = detector.containsDuplicate(numbers)
    
    return NextResponse.json({
      result,
      algorithm: 'Contains Duplicate',
      complexity: { time: 'O(n)', space: 'O(n)' },
      explanation: 'Uses hash set to track seen elements',
      steps: detector.getSteps(numbers)
    })
  } catch (error) {
    return NextResponse.json(
      { error: 'Invalid input' },
      { status: 400 }
    )
  }
}
```

#### Algorithm Implementation in TypeScript
```typescript
// lib/algorithms/duplicate-detector.ts
export class DuplicateDetector {
  containsDuplicate(nums: number[]): boolean {
    const seen = new Set<number>()
    
    for (const num of nums) {
      if (seen.has(num)) {
        return true
      }
      seen.add(num)
    }
    
    return false
  }
  
  getSteps(nums: number[]): string[] {
    const steps: string[] = []
    const seen = new Set<number>()
    
    steps.push('Initialize empty hash set')
    
    for (let i = 0; i < nums.length; i++) {
      const num = nums[i]
      if (seen.has(num)) {
        steps.push(`Found duplicate: ${num}`)
        break
      }
      seen.add(num)
      steps.push(`Add ${num} to set: {${Array.from(seen).join(', ')}}`)
    }
    
    return steps
  }
}
```

### Phase 4: State Management

#### Using SWR for Data Fetching
```typescript
// hooks/useAlgorithm.ts
import useSWR from 'swr'
import { analyzeData } from '@/lib/api'

export function useAlgorithm(algorithm: string, data: any) {
  const { data: result, error, isLoading } = useSWR(
    data ? [algorithm, data] : null,
    ([algo, input]) => analyzeData(algo, input)
  )
  
  return {
    result,
    error,
    isLoading,
    isValidating: !error && !result
  }
}
```

#### Component Usage
```tsx
// components/AlgorithmRunner.tsx
'use client'
import { useState } from 'react'
import { useAlgorithm } from '@/hooks/useAlgorithm'

export default function AlgorithmRunner({ algorithm }: { algorithm: string }) {
  const [inputData, setInputData] = useState<any>(null)
  const { result, error, isLoading } = useAlgorithm(algorithm, inputData)
  
  const handleSubmit = (data: any) => {
    setInputData(data)
  }
  
  return (
    <div>
      <InputForm onSubmit={handleSubmit} />
      {isLoading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {result && <ResultDisplay result={result} />}
    </div>
  )
}
```

### Phase 5: Styling Migration

#### CSS Modules Approach
```css
/* components/AlgorithmCard.module.css */
.algorithmCard {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: var(--space-4);
  transition: all 0.3s ease;
}

.algorithmCard:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}
```

```tsx
// components/AlgorithmCard.tsx
import styles from './AlgorithmCard.module.css'

export default function AlgorithmCard({ feature }) {
  return (
    <div className={styles.algorithmCard}>
      {/* Content */}
    </div>
  )
}
```

#### Tailwind CSS Integration
```tsx
// Alternative: Using Tailwind classes
export default function AlgorithmCard({ feature }) {
  return (
    <div className="bg-white border border-gray-200 rounded-lg p-4 transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
      {/* Content */}
    </div>
  )
}
```

### Phase 6: Routing & Navigation

#### App Router Structure
```
app/
├── page.tsx                 # Home page
├── algorithms/
│   ├── page.tsx            # Algorithms overview
│   ├── duplicates/page.tsx # Duplicate detection
│   ├── anagrams/page.tsx   # Anagram analysis
│   └── [slug]/page.tsx     # Dynamic algorithm pages
└── api/
    ├── analyze/
    │   ├── duplicates/route.ts
    │   ├── anagrams/route.ts
    │   └── [algorithm]/route.ts
    └── algorithms/
        └── mapping/route.ts
```

#### Dynamic Algorithm Pages
```tsx
// app/algorithms/[slug]/page.tsx
import { Metadata } from 'next'
import AlgorithmRunner from '@/components/AlgorithmRunner'
import { getAlgorithmConfig } from '@/lib/algorithms'

interface PageProps {
  params: { slug: string }
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const config = getAlgorithmConfig(params.slug)
  
  return {
    title: `${config.title} - SmartPack`,
    description: config.description
  }
}

export default function AlgorithmPage({ params }: PageProps) {
  const config = getAlgorithmConfig(params.slug)
  
  return (
    <div>
      <h1>{config.title}</h1>
      <p>{config.description}</p>
      <AlgorithmRunner algorithm={params.slug} />
    </div>
  )
}
```

### Phase 7: Performance Optimization

#### Server-Side Rendering
```tsx
// app/algorithms/page.tsx - Server Component
import { getAlgorithmMapping } from '@/lib/api'
import AlgorithmGrid from '@/components/AlgorithmGrid'

export default async function AlgorithmsPage() {
  const mapping = await getAlgorithmMapping()
  
  return (
    <div>
      <h1>DSA Algorithms</h1>
      <AlgorithmGrid mapping={mapping} />
    </div>
  )
}
```

#### Static Generation for Algorithm Pages
```tsx
// app/algorithms/[slug]/page.tsx
import { getAllAlgorithmSlugs } from '@/lib/algorithms'

export async function generateStaticParams() {
  const slugs = getAllAlgorithmSlugs()
  
  return slugs.map((slug) => ({
    slug: slug
  }))
}

export const dynamicParams = false // Only pre-render known algorithms
```

### Phase 8: Chart.js Integration

```tsx
// components/ChartVisualization.tsx
'use client'
import { useEffect, useRef } from 'react'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Bar } from 'react-chartjs-2'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

interface ChartProps {
  data: any
  algorithm: string
}

export default function ChartVisualization({ data, algorithm }: ChartProps) {
  const chartData = {
    labels: Object.keys(data.frequency || {}),
    datasets: [{
      label: 'Frequency',
      data: Object.values(data.frequency || {}),
      backgroundColor: 'rgba(59, 130, 246, 0.8)',
      borderColor: 'rgba(59, 130, 246, 1)',
      borderWidth: 2
    }]
  }
  
  const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: `${algorithm} Visualization`
      }
    }
  }
  
  return <Bar data={chartData} options={options} />
}
```

### Phase 9: Testing Strategy

#### Unit Tests with Jest
```typescript
// __tests__/algorithms/duplicate-detector.test.ts
import { DuplicateDetector } from '@/lib/algorithms/duplicate-detector'

describe('DuplicateDetector', () => {
  let detector: DuplicateDetector
  
  beforeEach(() => {
    detector = new DuplicateDetector()
  })
  
  test('should detect duplicates', () => {
    expect(detector.containsDuplicate([1, 2, 3, 1])).toBe(true)
  })
  
  test('should return false for unique elements', () => {
    expect(detector.containsDuplicate([1, 2, 3, 4])).toBe(false)
  })
})
```

#### Component Tests with React Testing Library
```typescript
// __tests__/components/AlgorithmCard.test.tsx
import { render, screen, fireEvent } from '@testing-library/react'
import AlgorithmCard from '@/components/AlgorithmCard'

const mockFeature = {
  id: 'duplicates',
  title: 'Duplicate Detector',
  description: 'Test description'
}

test('should toggle runner visibility', () => {
  render(<AlgorithmCard feature={mockFeature} />)
  
  const button = screen.getByText('Show Runner')
  fireEvent.click(button)
  
  expect(screen.getByText('Hide Runner')).toBeInTheDocument()
})
```

### Phase 10: Deployment

#### Vercel Deployment
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Environment variables in Vercel dashboard:
# NEXT_PUBLIC_API_URL (if using external FastAPI)
```

#### Configuration Files
```json
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true
  },
  env: {
    CUSTOM_KEY: process.env.CUSTOM_KEY
  }
}

module.exports = nextConfig
```

## 📊 Migration Checklist

### Pre-Migration
- [ ] Audit current Svelte components
- [ ] Document API endpoints
- [ ] Test algorithm implementations
- [ ] Plan component hierarchy

### During Migration
- [ ] Set up Next.js project structure
- [ ] Convert Svelte components to React
- [ ] Implement API routes or keep FastAPI
- [ ] Migrate styling system
- [ ] Set up state management
- [ ] Implement routing
- [ ] Add performance optimizations

### Post-Migration
- [ ] Test all algorithms
- [ ] Verify responsive design
- [ ] Performance audit
- [ ] SEO optimization
- [ ] Deploy to production
- [ ] Update documentation

## 🔧 Troubleshooting Common Issues

### 1. Hydration Mismatches
```tsx
// Use dynamic imports for client-only components
import dynamic from 'next/dynamic'

const ChartVisualization = dynamic(
  () => import('@/components/ChartVisualization'),
  { ssr: false }
)
```

### 2. API Route CORS
```typescript
// app/api/analyze/duplicates/route.ts
export async function POST(request: NextRequest) {
  const response = NextResponse.json(data)
  
  response.headers.set('Access-Control-Allow-Origin', '*')
  response.headers.set('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
  
  return response
}
```

### 3. Environment Variables
```bash
# .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
API_SECRET_KEY=your-secret-key
```

## 📚 Additional Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [React Migration Guide](https://react.dev/learn/start-a-new-react-project)
- [SWR Documentation](https://swr.vercel.app/)
- [Chart.js React Integration](https://react-chartjs-2.js.org/)

## 🎯 Final Notes

### Benefits of Migration
- **Better SEO**: Server-side rendering
- **Improved Performance**: Built-in optimizations
- **Larger Ecosystem**: More React libraries
- **Team Scalability**: More React developers available

### Considerations
- **Learning Curve**: Team needs React/Next.js knowledge
- **Bundle Size**: React might be larger than Svelte
- **Complexity**: Additional build complexity

The migration can be done incrementally, starting with core components and gradually moving all functionality to Next.js.