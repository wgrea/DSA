<!-- 
Template for new Svelte components
Copy this file and rename to create new components
-->

<script lang="ts">
  import { createEventDispatcher, onMount } from 'svelte';
  
  // Component props
  export let data: any = null;
  export let title: string = '';
  export let loading: boolean = false;
  
  // Event dispatcher for parent communication
  const dispatch = createEventDispatcher();
  
  // Component state
  let internalState = null;
  let error: string | null = null;
  
  // Lifecycle
  onMount(() => {
    // Initialize component
    console.log('Component mounted');
  });
  
  // Event handlers
  function handleAction() {
    dispatch('action', { data: internalState });
  }
  
  function handleError(err: Error) {
    error = err.message;
    dispatch('error', { error: err });
  }
  
  // Reactive statements
  $: if (data) {
    processData(data);
  }
  
  // Helper functions
  function processData(inputData: any) {
    try {
      // Process the data
      internalState = inputData;
      error = null;
    } catch (err) {
      handleError(err instanceof Error ? err : new Error('Unknown error'));
    }
  }
</script>

<!-- Component template -->
<div class="template-component">
  {#if loading}
    <div class="loading-state">
      <div class="loading"></div>
      <p class="loading-text">Loading...</p>
    </div>
  {:else if error}
    <div class="error-state">
      <span class="error-icon">⚠️</span>
      <p class="error-message">{error}</p>
      <button class="btn btn-outline" on:click={() => error = null}>
        Retry
      </button>
    </div>
  {:else}
    <div class="content">
      <header class="component-header">
        <h3 class="component-title">{title}</h3>
      </header>
      
      <main class="component-main">
        <!-- Component content goes here -->
        <p>Template component content</p>
        
        {#if data}
          <pre class="data-display">{JSON.stringify(data, null, 2)}</pre>
        {/if}
      </main>
      
      <footer class="component-footer">
        <button class="btn btn-primary" on:click={handleAction}>
          Action
        </button>
      </footer>
    </div>
  {/if}
</div>

<style>
  .template-component {
    background-color: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: var(--space-4);
    min-height: 200px;
  }

  .loading-state,
  .error-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 200px;
    text-align: center;
    gap: var(--space-2);
  }

  .loading-text {
    color: var(--text-secondary);
    font-size: 0.875rem;
    margin: 0;
  }

  .error-state {
    color: var(--error-500);
  }

  .error-icon {
    font-size: 2rem;
  }

  .error-message {
    color: var(--text-secondary);
    margin: 0;
  }

  .content {
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
  }

  .component-header {
    border-bottom: 1px solid var(--border-color);
    padding-bottom: var(--space-2);
  }

  .component-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin: 0;
  }

  .component-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }

  .data-display {
    background-color: var(--neutral-100);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: var(--space-2);
    font-family: var(--font-mono);
    font-size: 0.75rem;
    overflow-x: auto;
    margin: 0;
  }

  .component-footer {
    display: flex;
    justify-content: flex-end;
    gap: var(--space-2);
    padding-top: var(--space-2);
    border-top: 1px solid var(--border-color);
  }

  @media (prefers-color-scheme: dark) {
    .data-display {
      background-color: var(--neutral-800);
    }
  }

  @media (max-width: 768px) {
    .template-component {
      padding: var(--space-3);
    }
    
    .component-footer {
      flex-direction: column;
    }
  }
</style>