<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import AlgorithmRunner from './AlgorithmRunner.svelte';
  
  export let feature: any;
  
  const dispatch = createEventDispatcher();
  let showRunner = false;

  function toggleRunner() {
    showRunner = !showRunner;
  }

  function getColorClass(color: string) {
    const colorMap = {
      primary: 'border-primary-200 hover:border-primary-300',
      secondary: 'border-secondary-200 hover:border-secondary-300', 
      accent: 'border-accent-200 hover:border-accent-300',
      success: 'border-green-200 hover:border-green-300',
      warning: 'border-yellow-200 hover:border-yellow-300'
    };
    return colorMap[color] || colorMap.primary;
  }

  function getBadgeColor(color: string) {
    const badgeMap = {
      primary: 'badge-primary',
      secondary: 'bg-secondary-100 text-secondary-700',
      accent: 'bg-accent-100 text-accent-700',
      success: 'badge-success',
      warning: 'badge-warning'
    };
    return badgeMap[color] || badgeMap.primary;
  }
</script>

<div class="algorithm-card card {getColorClass(feature.color)}">
  <div class="card-header">
    <div class="card-title-row">
      <div class="card-icon">{feature.icon}</div>
      <div class="card-title-content">
        <h3 class="card-title">{feature.title}</h3>
        {#if feature.blind75}
          <span class="badge badge-primary blind75-badge">Blind 75</span>
        {/if}
      </div>
    </div>
    <p class="card-description">{feature.description}</p>
  </div>

  <div class="card-content">
    <div class="algorithm-info">
      <div class="algorithm-name">
        <span class="text-sm font-medium text-secondary">Algorithm:</span>
        <span class="font-mono text-sm">{feature.algorithm}</span>
      </div>
      
      <div class="complexity-info">
        <div class="complexity-item">
          <span class="complexity-label">Time:</span>
          <span class="complexity-value badge {getBadgeColor(feature.color)}">{feature.complexity.time}</span>
        </div>
        <div class="complexity-item">
          <span class="complexity-label">Space:</span>
          <span class="complexity-value badge {getBadgeColor(feature.color)}">{feature.complexity.space}</span>
        </div>
      </div>
    </div>

    <div class="card-actions">
      <button class="btn btn-primary" on:click={toggleRunner}>
        {showRunner ? 'Hide' : 'Try It'} 
        <span class="action-icon">{showRunner ? '⬆️' : '▶️'}</span>
      </button>
    </div>
  </div>

  {#if showRunner}
    <div class="runner-container slide-up">
      <AlgorithmRunner algorithm={feature.id} inputType={feature.inputType} />
    </div>
  {/if}
</div>

<style>
  .algorithm-card {
    transition: all 0.3s ease;
    border-width: 2px;
    position: relative;
    overflow: hidden;
  }

  .algorithm-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--primary-500), var(--secondary-500), var(--accent-500));
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .algorithm-card:hover::before {
    opacity: 1;
  }

  .card-title-row {
    display: flex;
    align-items: flex-start;
    gap: var(--space-2);
    margin-bottom: var(--space-2);
  }

  .card-icon {
    font-size: 2rem;
    line-height: 1;
  }

  .card-title-content {
    flex: 1;
    display: flex;
    align-items: center;
    gap: var(--space-2);
    flex-wrap: wrap;
  }

  .card-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
  }

  .blind75-badge {
    font-size: 0.6rem;
    padding: 0.25rem 0.5rem;
  }

  .card-content {
    margin-top: var(--space-3);
  }

  .algorithm-info {
    margin-bottom: var(--space-3);
  }

  .algorithm-name {
    display: flex;
    flex-direction: column;
    gap: var(--space-1);
    margin-bottom: var(--space-2);
  }

  .complexity-info {
    display: flex;
    gap: var(--space-3);
    flex-wrap: wrap;
  }

  .complexity-item {
    display: flex;
    align-items: center;
    gap: var(--space-1);
  }

  .complexity-label {
    font-size: 0.875rem;
    color: var(--text-secondary);
    font-weight: 500;
  }

  .complexity-value {
    font-family: var(--font-mono);
    font-size: 0.75rem;
  }

  .card-actions {
    display: flex;
    gap: var(--space-2);
    margin-top: var(--space-3);
  }

  .action-icon {
    font-size: 0.875rem;
    transition: transform 0.2s ease;
  }

  .btn:hover .action-icon {
    transform: scale(1.1);
  }

  .runner-container {
    margin-top: var(--space-4);
    padding-top: var(--space-4);
    border-top: 1px solid var(--border-color);
  }

  /* Color variants */
  .border-primary-200 { border-color: var(--primary-200); }
  .border-primary-300 { border-color: var(--primary-300); }
  .border-secondary-200 { border-color: var(--secondary-200); }
  .border-secondary-300 { border-color: var(--secondary-300); }
  .border-accent-200 { border-color: var(--accent-200); }
  .border-accent-300 { border-color: var(--accent-300); }
  .border-green-200 { border-color: #bbf7d0; }
  .border-green-300 { border-color: #86efac; }
  .border-yellow-200 { border-color: #fef3c7; }
  .border-yellow-300 { border-color: #fcd34d; }

  .bg-secondary-100 { background-color: var(--secondary-100); }
  .text-secondary-700 { color: var(--secondary-700); }
  .bg-accent-100 { background-color: var(--accent-100); }
  .text-accent-700 { color: var(--accent-700); }

  @media (max-width: 768px) {
    .card-title-row {
      flex-direction: column;
      align-items: flex-start;
    }
    
    .card-title-content {
      flex-direction: column;
      align-items: flex-start;
      gap: var(--space-1);
    }
    
    .complexity-info {
      flex-direction: column;
      gap: var(--space-1);
    }
  }
</style>