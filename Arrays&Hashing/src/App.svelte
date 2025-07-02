<script lang="ts">
  import Header from './components/Header.svelte';
  import FeatureGrid from './components/FeatureGrid.svelte';
  import AlgorithmMappingTable from './components/AlgorithmMappingTable.svelte';
  import Footer from './components/Footer.svelte';
  import { onMount } from 'svelte';

  let isLoading = true;

  onMount(() => {
    // Simulate initial loading
    setTimeout(() => {
      isLoading = false;
    }, 500);
  });
</script>

<main class="app">
  {#if isLoading}
    <div class="loading-container">
      <div class="loading-spinner">
        <div class="loading"></div>
        <p class="text-secondary mt-2">Loading SmartPack...</p>
      </div>
    </div>
  {:else}
    <Header />
    
    <div class="container">
      <!-- Hero Section -->
      <section class="hero fade-in">
        <div class="hero-content text-center">
          <h1 class="hero-title">
            Smart<span class="text-primary">Pack</span>
          </h1>
          <p class="hero-subtitle text-secondary">
            Intelligent Text & Data Pattern Explorer
          </p>
          <p class="hero-description">
            Discover the power of Data Structures & Algorithms through interactive exploration 
            of text and numeric patterns. Built with the Blind 75 foundations in mind.
          </p>
          <div class="hero-badges">
            <span class="badge badge-primary">Arrays & Hashing</span>
            <span class="badge badge-primary">Interactive Learning</span>
            <span class="badge badge-primary">Real-time Visualization</span>
          </div>
        </div>
      </section>

      <!-- Feature Grid -->
      <FeatureGrid />

      <!-- Algorithm Mapping -->
      <AlgorithmMappingTable />

      <!-- Why This Works Section -->
      <section class="why-section card slide-up">
        <div class="card-header">
          <h2 class="card-title">🧠 Why This Works: Bridging DSA to System Design</h2>
        </div>
        
        <div class="grid grid-cols-1 gap-4">
          <div class="insight-card">
            <h3 class="text-lg font-semibold mb-2">🔍 Pattern Recognition</h3>
            <p class="text-secondary">
              Real-world systems constantly deal with duplicate detection, frequency analysis, 
              and pattern matching. These fundamental algorithms form the backbone of everything 
              from database optimization to fraud detection systems.
            </p>
          </div>
          
          <div class="insight-card">
            <h3 class="text-lg font-semibold mb-2">⚡ Performance Matters</h3>
            <p class="text-secondary">
              Understanding time and space complexity isn't academic - it's the difference between 
              a system that scales to millions of users and one that crashes under load. 
              Hash-based algorithms provide O(1) lookups that power modern applications.
            </p>
          </div>
          
          <div class="insight-card">
            <h3 class="text-lg font-semibold mb-2">🔗 Building Blocks</h3>
            <p class="text-secondary">
              These patterns are composable. Two Sum becomes recommendation systems, 
              anagram detection becomes fuzzy search, and sequence tracking becomes 
              anomaly detection in time series data.
            </p>
          </div>
        </div>
      </section>
    </div>

    <Footer />
  {/if}
</main>

<style>
  .app {
    min-height: 100vh;
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--neutral-100) 100%);
  }

  .loading-container {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background-color: var(--bg-primary);
  }

  .loading-spinner {
    text-align: center;
  }

  .hero {
    padding: var(--space-10) 0 var(--space-8) 0;
    text-align: center;
  }

  .hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: var(--space-2);
    background: linear-gradient(135deg, var(--primary-600), var(--secondary-500));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-subtitle {
    font-size: 1.5rem;
    font-weight: 500;
    margin-bottom: var(--space-3);
  }

  .hero-description {
    font-size: 1.125rem;
    line-height: 1.7;
    max-width: 600px;
    margin: 0 auto var(--space-4) auto;
    color: var(--text-secondary);
  }

  .hero-badges {
    display: flex;
    justify-content: center;
    gap: var(--space-2);
    flex-wrap: wrap;
  }

  .why-section {
    margin: var(--space-8) 0;
  }

  .insight-card {
    padding: var(--space-3);
    border-left: 4px solid var(--primary-500);
    background-color: var(--primary-50);
    border-radius: var(--radius-md);
  }

  @media (prefers-color-scheme: dark) {
    .app {
      background: linear-gradient(135deg, var(--neutral-900) 0%, var(--neutral-800) 100%);
    }
    
    .insight-card {
      background-color: var(--neutral-800);
      border-left-color: var(--primary-400);
    }
  }

  @media (max-width: 768px) {
    .hero-title {
      font-size: 2.5rem;
    }
    
    .hero-subtitle {
      font-size: 1.25rem;
    }
    
    .hero-description {
      font-size: 1rem;
    }
    
    .hero-badges {
      justify-content: center;
    }
  }
</style>