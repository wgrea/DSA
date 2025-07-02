<script lang="ts">
  import AlgorithmCard from './AlgorithmCard.svelte';
  
  const features = [
    {
      id: 'duplicates',
      title: 'Duplicate Detector',
      description: 'Identify duplicate elements using hash-based algorithms',
      algorithm: 'Contains Duplicate',
      complexity: { time: 'O(n)', space: 'O(n)' },
      icon: '🔍',
      color: 'primary',
      inputType: 'numbers',
      blind75: true
    },
    {
      id: 'anagrams',
      title: 'Anagram Analyzer',
      description: 'Detect and group anagrams with frequency mapping',
      algorithm: 'Valid Anagram / Group Anagrams',
      complexity: { time: 'O(n*m log m)', space: 'O(n*m)' },
      icon: '🔠',
      color: 'secondary',
      inputType: 'strings',
      blind75: true
    },
    {
      id: 'frequency',
      title: 'Frequency Insights',
      description: 'Find most frequent elements using heap optimization',
      algorithm: 'Top K Frequent Elements',
      complexity: { time: 'O(n log k)', space: 'O(n + k)' },
      icon: '📊',
      color: 'accent',
      inputType: 'numbers',
      blind75: true
    },
    {
      id: 'pairs',
      title: 'Pair Calculator',
      description: 'Discover number pairs that sum to target values',
      algorithm: 'Two Sum',
      complexity: { time: 'O(n)', space: 'O(n)' },
      icon: '➕',
      color: 'success',
      inputType: 'numbers',
      blind75: true
    },
    {
      id: 'products',
      title: 'Product Calculator',
      description: 'Calculate array products excluding current element',
      algorithm: 'Product of Array Except Self',
      complexity: { time: 'O(n)', space: 'O(1)' },
      icon: '✖️',
      color: 'warning',
      inputType: 'numbers',
      blind75: true
    },
    {
      id: 'sequences',
      title: 'Sequence Tracker',
      description: 'Find longest consecutive sequences efficiently',
      algorithm: 'Longest Consecutive Sequence',
      complexity: { time: 'O(n)', space: 'O(n)' },
      icon: '📈',
      color: 'primary',
      inputType: 'numbers',
      blind75: true
    },
    {
      id: 'encoding',
      title: 'Safe Encoder/Decoder',
      description: 'Encode and decode strings with delimiter handling',
      algorithm: 'Encode and Decode Strings',
      complexity: { time: 'O(n)', space: 'O(n)' },
      icon: '🔐',
      color: 'secondary',
      inputType: 'strings',
      blind75: true
    }
  ];
</script>

<section id="features" class="features-section">
  <div class="section-header text-center mb-8">
    <h2 class="section-title">🚀 Explore DSA Patterns</h2>
    <p class="section-description text-secondary">
      Interactive implementations of core algorithms from the Blind 75 collection, 
      designed to teach fundamental patterns through hands-on exploration.
    </p>
  </div>

  <div class="feature-grid">
    {#each features as feature}
      <AlgorithmCard {feature} />
    {/each}
  </div>
</section>

<style>
  .features-section {
    padding: var(--space-8) 0;
  }

  .section-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: var(--space-2);
  }

  .section-description {
    font-size: 1.125rem;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
  }

  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: var(--space-4);
    margin-top: var(--space-8);
  }

  @media (max-width: 768px) {
    .section-title {
      font-size: 2rem;
    }
    
    .feature-grid {
      grid-template-columns: 1fr;
    }
  }
</style>