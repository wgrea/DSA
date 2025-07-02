<script lang="ts">
  import { onMount } from 'svelte';
  import InputForm from './InputForm.svelte';
  import ResultDisplay from './ResultDisplay.svelte';
  import { apiService } from '../services/api';
  
  export let algorithm: string;
  export let inputType: 'numbers' | 'strings' = 'numbers';
  
  let inputData: any = null;
  let result: any = null;
  let isLoading = false;
  let error: string | null = null;

  async function handleInputSubmit(data: any) {
    isLoading = true;
    error = null;
    result = null;
    
    try {
      const response = await apiService.analyzeData(algorithm, data);
      result = response;
    } catch (err) {
      error = err instanceof Error ? err.message : 'An error occurred';
      console.error('Algorithm execution error:', err);
    } finally {
      isLoading = false;
    }
  }

  function handleReset() {
    result = null;
    error = null;
    inputData = null;
  }
</script>

<div class="algorithm-runner">
  <div class="runner-header">
    <h4 class="runner-title">🧪 Interactive Algorithm Runner</h4>
    <p class="runner-description text-secondary">
      Enter your data below to see the algorithm in action with step-by-step execution.
    </p>
  </div>

  <div class="runner-content">
    {#if !result && !error}
      <InputForm 
        {algorithm} 
        {inputType} 
        on:submit={(e) => handleInputSubmit(e.detail)}
        disabled={isLoading}
      />
    {/if}

    {#if isLoading}
      <div class="loading-state">
        <div class="loading"></div>
        <p class="loading-text">Processing your data...</p>
      </div>
    {/if}

    {#if error}
      <div class="error-state">
        <div class="error-icon">❌</div>
        <h5 class="error-title">Oops! Something went wrong</h5>
        <p class="error-message">{error}</p>
        <button class="btn btn-outline" on:click={handleReset}>
          Try Again
        </button>
      </div>
    {/if}

    {#if result}
      <ResultDisplay {result} {algorithm} on:reset={handleReset} />
    {/if}
  </div>
</div>

<style>
  .algorithm-runner {
    background-color: var(--neutral-50);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: var(--space-4);
  }

  .runner-header {
    margin-bottom: var(--space-4);
  }

  .runner-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: var(--space-1);
    display: flex;
    align-items: center;
    gap: var(--space-1);
  }

  .runner-description {
    font-size: 0.875rem;
    line-height: 1.5;
  }

  .runner-content {
    min-height: 200px;
  }

  .loading-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: var(--space-6);
    text-align: center;
  }

  .loading-text {
    margin-top: var(--space-2);
    color: var(--text-secondary);
    font-size: 0.875rem;
  }

  .error-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: var(--space-6);
    text-align: center;
  }

  .error-icon {
    font-size: 2rem;
    margin-bottom: var(--space-2);
  }

  .error-title {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--error-500);
    margin-bottom: var(--space-2);
  }

  .error-message {
    color: var(--text-secondary);
    margin-bottom: var(--space-3);
    font-size: 0.875rem;
  }

  @media (prefers-color-scheme: dark) {
    .algorithm-runner {
      background-color: var(--neutral-800);
    }
  }
</style>