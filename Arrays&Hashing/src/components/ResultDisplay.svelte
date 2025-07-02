<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import ChartVisualization from './ChartVisualization.svelte';
  
  export let result: any;
  export let algorithm: string;
  
  const dispatch = createEventDispatcher();
  
  let activeTab = 'result';
  
  function handleReset() {
    dispatch('reset');
  }

  function formatResult(data: any) {
    if (typeof data === 'boolean') {
      return data ? '✅ True' : '❌ False';
    }
    if (Array.isArray(data)) {
      return data.length === 0 ? '[]' : `[${data.join(', ')}]`;
    }
    if (typeof data === 'object' && data !== null) {
      return JSON.stringify(data, null, 2);
    }
    return String(data);
  }

  function getResultIcon() {
    if (typeof result.result === 'boolean') {
      return result.result ? '✅' : '❌';
    }
    if (Array.isArray(result.result)) {
      return '📋';
    }
    if (typeof result.result === 'object') {
      return '🔧';
    }
    return '📊';
  }
</script>

<div class="result-display">
  <div class="result-header">
    <div class="result-title-row">
      <h4 class="result-title">
        {getResultIcon()} Algorithm Results
      </h4>
      <button class="btn btn-outline btn-sm" on:click={handleReset}>
        Reset
      </button>
    </div>
    
    <div class="algorithm-meta">
      <span class="algorithm-name">{result.algorithm}</span>
      <div class="complexity-badges">
        <span class="badge complexity-badge">
          Time: {result.complexity.time}
        </span>
        <span class="badge complexity-badge">
          Space: {result.complexity.space}
        </span>
      </div>
    </div>
  </div>

  <div class="result-tabs">
    <button 
      class="tab-button" 
      class:active={activeTab === 'result'}
      on:click={() => activeTab = 'result'}
    >
      Result
    </button>
    <button 
      class="tab-button" 
      class:active={activeTab === 'steps'}
      on:click={() => activeTab = 'steps'}
    >
      Steps ({result.steps?.length || 0})
    </button>
    {#if result.visualization_data}
      <button 
        class="tab-button" 
        class:active={activeTab === 'visualization'}
        on:click={() => activeTab = 'visualization'}
      >
        Visualization
      </button>
    {/if}
  </div>

  <div class="result-content">
    {#if activeTab === 'result'}
      <div class="result-section">
        <div class="result-value">
          <h5 class="result-label">Output:</h5>
          <pre class="result-code">{formatResult(result.result)}</pre>
        </div>
        
        <div class="explanation">
          <h5 class="explanation-label">How it works:</h5>
          <p class="explanation-text">{result.explanation}</p>
        </div>
      </div>
    {/if}

    {#if activeTab === 'steps'}
      <div class="steps-section">
        <h5 class="steps-label">Step-by-step execution:</h5>
        <ol class="steps-list">
          {#each result.steps as step, index}
            <li class="step-item">
              <span class="step-number">{index + 1}</span>
              <span class="step-text">{step}</span>
            </li>
          {/each}
        </ol>
      </div>
    {/if}

    {#if activeTab === 'visualization' && result.visualization_data}
      <div class="visualization-section">
        <h5 class="visualization-label">Visual Analysis:</h5>
        <ChartVisualization 
          data={result.visualization_data} 
          {algorithm} 
        />
      </div>
    {/if}
  </div>
</div>

<style>
  .result-display {
    background-color: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    overflow: hidden;
  }

  .result-header {
    padding: var(--space-4);
    border-bottom: 1px solid var(--border-color);
    background-color: var(--primary-50);
  }

  .result-title-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: var(--space-2);
  }

  .result-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin: 0;
  }

  .algorithm-meta {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }

  .algorithm-name {
    font-size: 0.875rem;
    color: var(--text-secondary);
    font-weight: 500;
  }

  .complexity-badges {
    display: flex;
    gap: var(--space-1);
    flex-wrap: wrap;
  }

  .complexity-badge {
    font-family: var(--font-mono);
    font-size: 0.75rem;
  }

  .result-tabs {
    display: flex;
    border-bottom: 1px solid var(--border-color);
    background-color: var(--neutral-50);
  }

  .tab-button {
    flex: 1;
    padding: var(--space-2) var(--space-3);
    border: none;
    background: none;
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.2s ease;
    border-bottom: 2px solid transparent;
  }

  .tab-button:hover {
    color: var(--text-primary);
    background-color: var(--neutral-100);
  }

  .tab-button.active {
    color: var(--primary-600);
    border-bottom-color: var(--primary-500);
    background-color: var(--bg-secondary);
  }

  .result-content {
    padding: var(--space-4);
  }

  .result-section {
    display: flex;
    flex-direction: column;
    gap: var(--space-4);
  }

  .result-value {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }

  .result-label,
  .explanation-label,
  .steps-label,
  .visualization-label {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0;
  }

  .result-code {
    background-color: var(--neutral-100);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: var(--space-3);
    font-family: var(--font-mono);
    font-size: 0.875rem;
    overflow-x: auto;
    margin: 0;
    white-space: pre-wrap;
  }

  .explanation-text {
    color: var(--text-secondary);
    line-height: 1.6;
    margin: 0;
  }

  .steps-list {
    padding-left: 0;
    margin: 0;
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }

  .step-item {
    display: flex;
    align-items: flex-start;
    gap: var(--space-2);
    padding: var(--space-2);
    background-color: var(--neutral-50);
    border-radius: var(--radius-md);
    border-left: 3px solid var(--primary-300);
  }

  .step-number {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    background-color: var(--primary-500);
    color: white;
    border-radius: 50%;
    font-size: 0.75rem;
    font-weight: 600;
    flex-shrink: 0;
  }

  .step-text {
    font-size: 0.875rem;
    line-height: 1.5;
    color: var(--text-primary);
    font-family: var(--font-mono);
  }

  .visualization-section {
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
  }

  @media (prefers-color-scheme: dark) {
    .result-header {
      background-color: var(--neutral-800);
    }
    
    .result-tabs {
      background-color: var(--neutral-800);
    }
    
    .tab-button.active {
      background-color: var(--neutral-700);
    }
    
    .result-code {
      background-color: var(--neutral-800);
    }
    
    .step-item {
      background-color: var(--neutral-800);
    }
  }

  @media (max-width: 768px) {
    .result-title-row {
      flex-direction: column;
      align-items: flex-start;
      gap: var(--space-2);
    }
    
    .algorithm-meta {
      width: 100%;
    }
    
    .complexity-badges {
      justify-content: flex-start;
    }
  }
</style>