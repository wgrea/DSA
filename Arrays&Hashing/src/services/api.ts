/**
 * API Service for SmartPack Backend Communication
 * Handles all API calls to the FastAPI backend
 */

// API Configuration
const API_BASE_URL = 'http://localhost:8000';

// TypeScript Interfaces for API Communication
export interface NumericAnalysisRequest {
  numbers: number[];
  target?: number;
  k?: number;
  options?: Record<string, any>;
}

export interface AnagramRequest {
  strings: string[];
  options?: Record<string, any>;
}

export interface AnalysisResponse {
  result: any;
  algorithm: string;
  complexity: {
    time: string;
    space: string;
  };
  explanation: string;
  steps: string[];
  visualization_data?: Record<string, any>;
}

export interface AlgorithmMapping {
  pattern: string;
  features: string[];
  real_world: string[];
  blind75: string[];
}

// API Service Class
class ApiService {
  private baseUrl: string;

  constructor(baseUrl: string = API_BASE_URL) {
    this.baseUrl = baseUrl;
  }

  private async makeRequest<T>(
    endpoint: string, 
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseUrl}${endpoint}`;
    
    const config: RequestInit = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(
          errorData.detail || 
          `HTTP ${response.status}: ${response.statusText}`
        );
      }

      return await response.json();
    } catch (error) {
      if (error instanceof Error) {
        throw error;
      }
      throw new Error('Network error occurred');
    }
  }

  // Algorithm Analysis Methods
  async analyzeData(algorithm: string, data: any): Promise<AnalysisResponse> {
    const endpoint = this.getAnalysisEndpoint(algorithm);
    
    return this.makeRequest<AnalysisResponse>(endpoint, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  private getAnalysisEndpoint(algorithm: string): string {
    const endpointMap: Record<string, string> = {
      duplicates: '/analyze/duplicates',
      anagrams: '/analyze/anagrams',
      frequency: '/analyze/frequency',
      pairs: '/analyze/pairs',
      products: '/analyze/products',
      sequences: '/analyze/sequences',
      encoding: '/analyze/encoding',
    };

    const endpoint = endpointMap[algorithm];
    if (!endpoint) {
      throw new Error(`Unknown algorithm: ${algorithm}`);
    }

    return endpoint;
  }

  // Specific Algorithm Methods
  async analyzeDuplicates(request: NumericAnalysisRequest): Promise<AnalysisResponse> {
    return this.makeRequest<AnalysisResponse>('/analyze/duplicates', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  async analyzeAnagrams(request: AnagramRequest): Promise<AnalysisResponse> {
    return this.makeRequest<AnalysisResponse>('/analyze/anagrams', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  async analyzeFrequency(request: NumericAnalysisRequest): Promise<AnalysisResponse> {
    return this.makeRequest<AnalysisResponse>('/analyze/frequency', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  async analyzePairs(request: NumericAnalysisRequest): Promise<AnalysisResponse> {
    return this.makeRequest<AnalysisResponse>('/analyze/pairs', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  async analyzeProducts(request: NumericAnalysisRequest): Promise<AnalysisResponse> {
    return this.makeRequest<AnalysisResponse>('/analyze/products', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  async analyzeSequences(request: NumericAnalysisRequest): Promise<AnalysisResponse> {
    return this.makeRequest<AnalysisResponse>('/analyze/sequences', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  async analyzeEncoding(request: AnagramRequest): Promise<AnalysisResponse> {
    return this.makeRequest<AnalysisResponse>('/analyze/encoding', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  // Utility Methods
  async getAlgorithmMapping(): Promise<{ patterns: AlgorithmMapping[] }> {
    return this.makeRequest<{ patterns: AlgorithmMapping[] }>('/algorithms/mapping');
  }

  async healthCheck(): Promise<{ message: string; version: string }> {
    return this.makeRequest<{ message: string; version: string }>('/');
  }

  // Error Handling Utilities
  isNetworkError(error: Error): boolean {
    return error.message.includes('Failed to fetch') || 
           error.message.includes('Network error');
  }

  isValidationError(error: Error): boolean {
    return error.message.includes('validation') || 
           error.message.includes('Invalid input');
  }

  isServerError(error: Error): boolean {
    return error.message.includes('HTTP 5');
  }
}

// Export singleton instance
export const apiService = new ApiService();

// Export types for external use
export type { AnalysisResponse, NumericAnalysisRequest, AnagramRequest, AlgorithmMapping };

// Development/Testing utilities
export const createMockApiService = (baseUrl?: string) => {
  return new ApiService(baseUrl || 'http://localhost:8000');
};

// Next.js compatibility note:
// When converting to Next.js, replace fetch with:
// - axios for client-side requests
// - fetch in server-side functions (getServerSideProps, API routes)
// - Consider using SWR or React Query for caching and state management
export const NEXTJS_MIGRATION_NOTES = {
  clientSide: 'Replace fetch with axios or use built-in fetch with proper error boundaries',
  serverSide: 'Use fetch in getServerSideProps or API routes',
  stateManagement: 'Consider SWR, React Query, or Zustand for state management',
  errorHandling: 'Implement proper error boundaries and user feedback',
};