<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  
  export let algorithm: string;
  export let inputType: 'numbers' | 'strings' = 'numbers';
  export let disabled = false;
  
  const dispatch = createEventDispatcher();
  
  let inputValue = '';
  let targetValue = '';
  let kValue = '';
  let error = '';

  // Example data for different algorithms
  const examples = {
    duplicates: '1,2,3,1',
    anagrams: 'eat,tea,bat,tab',
    frequency: '1,1,1,2,2,3',
    pairs: '2,7,11,15',
    products: '1,2,3,4',
    sequences: '100,4,200,1,3,2',
    encoding: 'hello,world,test'
  };

  function handleSubmit() {
    error = '';
    
    if (!inputValue.trim()) {
      error = 'Please enter some data';
      return;
    }

    try {
      let data: any = {};
      
      if (inputType === 'numbers') {
        const numbers = inputValue.split(',').map(s => {
          const num = parseInt(s.trim());
          if (isNaN(num)) {
            throw new Error(`"${s.trim()}" is not a valid number`);
          }
          return num;
        });
        
        data.numbers = numbers;
        
        // Add target for pair algorithms
        if (['pairs'].includes(algorithm) && targetValue) {
          const target = parseInt(targetValue);
          if (isNaN(target)) {
            throw new Error('Target must be a valid number');
          }
          data.target = target;
        }
        
        // Add k for frequency algorithms
        if (['frequency'].includes(algorithm) && kValue) {
          const k = parseInt(kValue);
          if (isNaN(k) || k <= 0) {
            throw new Error('K must be a positive number');
          }
          data.k = k;
        }
      } else {
        const strings = inputValue.split(',').map(s => s.trim()).filter(s => s.length > 0);
        if (strings.length === 0) {
          throw new Error('Please enter at least one string');
        }
        data.strings = strings;
      }
      
      dispatch('submit', data);
    } catch (err) {
      error = err instanceof Error ? err.message : 'Invalid input';
    }
  }

  function loadExample() {
    inputValue = examples[algorithm] || '';
    if (algorithm === 'pairs') {
      targetValue = '9';
    }
    if (algorithm === 'frequency') {
      kValue = '2';
    }
    error = '';
  }

  function getPlaceholder() {
    if (inputType === 'numbers') {
      return 'Enter numbers separated by commas (e.g., 1,2,3,1)';
    } else {
      return 'Enter strings separated by commas (e.g., eat,tea,bat)';
    }
  }

  function getInputLabel() {
    return inputType === 'numbers' ? 'Numbers' : 'Strings';
  }
</script>

<form class="input-form" on:submit|preventDefault={handleSubmit}>
  <div class="form-group">
    <label for="input-data" class="label">
      {getInputLabel()}
      <span class="text-secondary text-sm">(comma-separated)</span>
    </label>
    <div class="input-with-example">
      <input
        id="input-data"
        type="text"
        class="input"
        placeholder={getPlaceholder()}
        bind:value={inputValue}
        {disabled}
      />
      <button
        type="button"
        class="btn-example"
        on:click={loadExample}
        {disabled}
        title="Load example data"
      >
        💡
      </button>
    </div>
  </div>

  {#if algorithm === 'pairs'}
    <div class="form-group">
      <label for="target-value" class="label">
        Target Sum
        <span class="text-secondary text-sm">(required for Two Sum)</span>
      </label>
      <input
        id="target-value"
        type="number"
        class="input"
        placeholder="Enter target sum (e.g., 9)"
        bind:value={targetValue}
        {disabled}
      />
    </div>
  {/if}

  {#if algorithm === 'frequency'}
    <div class="form-group">
      <label for="k-value" class="label">
        K Value
        <span class="text-secondary text-sm">(how many top elements)</span>
      </label>
      <input
        id="k-value"
        type="number"
        class="input"
        placeholder="Enter K (e.g., 2)"
        bind:value={kValue}
        min="1"
        {disabled}
      />
    </div>
  {/if}

  {#if error}
    <div class="error-message">
      <span class="error-icon">⚠️</span>
      {error}
    </div>
  {/if}

  <div class="form-actions">
    <button
      type="submit"
      class="btn btn-primary"
      {disabled}
    >
      {disabled ? 'Processing...' : 'Run Algorithm'}
      <span class="action-icon">🚀</span>
    </button>
  </div>
</form>

<style>
  .input-form {
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: var(--space-1);
  }

  .input-with-example {
    display: flex;
    gap: var(--space-1);
    align-items: center;
  }

  .input {
    flex: 1;
  }

  .btn-example {
    padding: var(--space-2);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    background-color: var(--bg-secondary);
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 44px;
    min-height: 44px;
  }

  .btn-example:hover:not(:disabled) {
    background-color: var(--primary-50);
    border-color: var(--primary-300);
    transform: scale(1.05);
  }

  .btn-example:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .error-message {
    display: flex;
    align-items: center;
    gap: var(--space-1);
    padding: var(--space-2);
    background-color: #fee2e2;
    color: #991b1b;
    border-radius: var(--radius-md);
    font-size: 0.875rem;
    border: 1px solid #fecaca;
  }

  .error-icon {
    font-size: 1rem;
    flex-shrink: 0;
  }

  .form-actions {
    display: flex;
    justify-content: flex-end;
    gap: var(--space-2);
    margin-top: var(--space-2);
  }

  .action-icon {
    font-size: 0.875rem;
  }

  @media (prefers-color-scheme: dark) {
    .error-message {
      background-color: #450a0a;
      color: #fca5a5;
      border-color: #7f1d1d;
    }
    
    .btn-example:hover:not(:disabled) {
      background-color: var(--neutral-700);
    }
  }

  @media (max-width: 768px) {
    .input-with-example {
      flex-direction: column;
    }
    
    .btn-example {
      width: 100%;
    }
  }
</style>