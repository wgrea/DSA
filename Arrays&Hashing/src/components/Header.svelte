<script lang="ts">
  import { onMount } from 'svelte';
  
  let isScrolled = false;

  onMount(() => {
    const handleScroll = () => {
      isScrolled = window.scrollY > 10;
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  });
</script>

<header class="app-header" class:scrolled={isScrolled}>
  <div class="container">
    <nav class="nav">
      <div class="nav-brand">
        <h1 class="brand-title">
          <span class="brand-icon">📦</span>
          Smart<span class="brand-accent">Pack</span>
        </h1>
        <span class="brand-subtitle">DSA Explorer</span>
      </div>
      
      <div class="nav-links">
        <a href="#features" class="nav-link">Features</a>
        <a href="#algorithms" class="nav-link">Algorithms</a>
        <a href="https://github.com/your-repo/smartpack" 
           target="_blank" 
           rel="noopener noreferrer" 
           class="btn btn-outline btn-sm">
          <span>GitHub</span>
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
          </svg>
        </a>
      </div>
    </nav>
  </div>
</header>

<style>
  .app-header {
    transition: all 0.3s ease;
    border-bottom: 1px solid transparent;
  }

  .app-header.scrolled {
    background-color: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(12px);
    border-bottom-color: var(--border-color);
    box-shadow: var(--shadow-sm);
  }

  .nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 64px;
  }

  .nav-brand {
    display: flex;
    align-items: center;
    gap: var(--space-2);
  }

  .brand-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0;
    display: flex;
    align-items: center;
    gap: var(--space-1);
  }

  .brand-icon {
    font-size: 1.25rem;
  }

  .brand-accent {
    color: var(--primary-500);
  }

  .brand-subtitle {
    font-size: 0.75rem;
    color: var(--text-secondary);
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .nav-links {
    display: flex;
    align-items: center;
    gap: var(--space-4);
  }

  .nav-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.875rem;
    transition: color 0.2s ease;
    position: relative;
  }

  .nav-link:hover {
    color: var(--primary-500);
  }

  .nav-link::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 0;
    height: 2px;
    background-color: var(--primary-500);
    transition: width 0.2s ease;
  }

  .nav-link:hover::after {
    width: 100%;
  }

  .btn-sm {
    padding: var(--space-1) var(--space-2);
    font-size: 0.8rem;
  }

  @media (prefers-color-scheme: dark) {
    .app-header.scrolled {
      background-color: rgba(31, 41, 55, 0.95);
    }
  }

  @media (max-width: 768px) {
    .nav-links {
      gap: var(--space-2);
    }
    
    .nav-link {
      display: none;
    }
    
    .nav-link:last-child {
      display: flex;
    }
    
    .brand-subtitle {
      display: none;
    }
  }
</style>