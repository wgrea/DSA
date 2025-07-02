<script lang="ts">
  import { onMount } from 'svelte';
  
  let mappingData: any[] = [];
  let isLoading = true;
  let error = null;

  onMount(async () => {
    try {
      // In a real app, this would come from the API
      // For now, we'll use mock data
      mappingData = [
        {
          pattern: "Hash Set/Map",
          features: ["Duplicate Detection", "Anagram Analysis", "Frequency Counting"],
          real_world: ["Database Deduplication", "Spam Detection", "Log Analysis"],
          blind75: ["Contains Duplicate", "Valid Anagram", "Group Anagrams"]
        },
        {
          pattern: "Two Pointers/Complement",
          features: ["Pair Finding", "Sum Calculations"],
          real_world: ["Recommendation Systems", "Financial Analysis"],
          blind75: ["Two Sum", "3Sum"]
        },
        {
          pattern: "Prefix/Suffix Arrays",
          features: ["Product Calculations", "Range Queries"],
          real_world: ["Stock Analysis", "Performance Metrics"],
          blind75: ["Product of Array Except Self"]
        },
        {
          pattern: "Union Find/Consecutive",
          features: ["Sequence Detection", "Graph Components"],
          real_world: ["Social Networks", "System Dependencies"],
          blind75: ["Longest Consecutive Sequence"]
        },
        {
          pattern: "String Processing",
          features: ["Safe Encoding", "Data Serialization"],
          real_world: ["API Design", "Data Storage"],
          blind75: ["Encode and Decode Strings"]
        }
      ];
      isLoading = false;
    } catch (err) {
      error = err;
      isLoading = false;
    }
  });

  function getPatternIcon(pattern: string) {
    const icons = {
      "Hash Set/Map": "🗂️",
      "Two Pointers/Complement": "👉",
      "Prefix/Suffix Arrays": "📊",
      "Union Find/Consecutive": "🔗",
      "String Processing": "📝"
    };
    return icons[pattern] || "🔧";
  }

  function getPatternColor(index: number) {
    const colors = [
      'primary',
      'secondary', 
      'accent',
      'success',
      'warning'
    ];
    return colors[index % colors.length];
  }
</script>

<section id="algorithms" class="mapping-section">
  <div class="section-header text-center">
    <h2 class="section-title">🗺️ DSA Pattern Mapping</h2>
    <p class="section-description text-secondary">
      Understanding how fundamental algorithms connect to real-world applications and system design
    </p>
  </div>

  {#if isLoading}
    <div class="loading-container">
      <div class="loading"></div>
      <p class="text-secondary">Loading algorithm mappings...</p>
    </div>
  {:else if error}
    <div class="error-container">
      <p class="text-error">Failed to load algorithm mappings</p>
    </div>
  {:else}
    <div class="mapping-grid">
      {#each mappingData as mapping, index}
        <div class="mapping-card card algorithm-card">
          <div class="card-header">
            <div class="pattern-header">
              <span class="pattern-icon">{getPatternIcon(mapping.pattern)}</span>
              <h3 class="pattern-title">{mapping.pattern}</h3>
            </div>
          </div>

          <div class="mapping-content">
            <div class="mapping-section">
              <h4 class="mapping-subtitle">
                <span class="section-icon">🚀</span>
                SmartPack Features
              </h4>
              <div class="tag-list">
                {#each mapping.features as feature}
                  <span class="tag feature-tag">{feature}</span>
                {/each}
              </div>
            </div>

            <div class="mapping-section">
              <h4 class="mapping-subtitle">
                <span class="section-icon">🌍</span>
                Real-World Applications
              </h4>
              <div class="tag-list">
                {#each mapping.real_world as app}
                  <span class="tag world-tag">{app}</span>
                {/each}
              </div>
            </div>

            <div class="mapping-section">
              <h4 class="mapping-subtitle">
                <span class="section-icon">🎯</span>
                Blind 75 Problems
              </h4>
              <div class="tag-list">
                {#each mapping.blind75 as problem}
                  <span class="tag blind75-tag">{problem}</span>
                {/each}
              </div>
            </div>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</section>

<style>
  .mapping-section {
    padding: var(--space-8) 0;
  }

  .section-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: var(--space-2);
  }

  .section-description {
    font-size: 1.125rem;
    max-width: 700px;
    margin: 0 auto var(--space-8) auto;
    line-height: 1.6;
  }

  .loading-container,
  .error-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: var(--space-8);
    text-align: center;
  }

  .mapping-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: var(--space-4);
  }

  .mapping-card {
    height: fit-content;
  }

  .pattern-header {
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }

  .pattern-icon {
    font-size: 1.5rem;
  }

  .pattern-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
    color: var(--text-primary);
  }

  .mapping-content {
    display: flex;
    flex-direction: column;
    gap: var(--space-4);
    margin-top: var(--space-3);
  }

  .mapping-section {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }

  .mapping-subtitle {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--text-secondary);
    margin: 0;
    display: flex;
    align-items: center;
    gap: var(--space-1);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .section-icon {
    font-size: 1rem;
  }

  .tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-1);
  }

  .tag {
    display: inline-block;
    padding: 0.375rem 0.75rem;
    border-radius: var(--radius-xl);
    font-size: 0.75rem;
    font-weight: 500;
    line-height: 1;
    transition: transform 0.2s ease;
  }

  .tag:hover {
    transform: translateY(-1px);
  }

  .feature-tag {
    background-color: var(--primary-100);
    color: var(--primary-700);
    border: 1px solid var(--primary-200);
  }

  .world-tag {
    background-color: var(--secondary-100);
    color: var(--secondary-700);
    border: 1px solid var(--secondary-200);
  }

  .blind75-tag {
    background-color: var(--accent-100);
    color: var(--accent-700);
    border: 1px solid var(--accent-200);
  }

  @media (prefers-color-scheme: dark) {
    .feature-tag {
      background-color: var(--primary-900);
      color: var(--primary-300);
      border-color: var(--primary-800);
    }
    
    .world-tag {
      background-color: var(--secondary-900);
      color: var(--secondary-300);
      border-color: var(--secondary-800);
    }
    
    .blind75-tag {
      background-color: var(--accent-900);
      color: var(--accent-300);
      border-color: var(--accent-800);
    }
  }

  @media (max-width: 768px) {
    .section-title {
      font-size: 2rem;
    }
    
    .mapping-grid {
      grid-template-columns: 1fr;
    }
  }
</style>