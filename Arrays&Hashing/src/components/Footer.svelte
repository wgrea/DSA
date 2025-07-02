<script>
  const currentYear = new Date().getFullYear();
</script>

<footer class="app-footer">
  <div class="container">
    <div class="footer-content">
      <div class="footer-section">
        <h4 class="footer-title">📦 SmartPack</h4>
        <p class="footer-description">
          Intelligent DSA Pattern Explorer built for learning and exploration
        </p>
        <div class="footer-badges">
          <span class="badge badge-primary">Open Source</span>
          <span class="badge badge-primary">Educational</span>
        </div>
      </div>
      
      <div class="footer-section">
        <h5 class="footer-subtitle">Features</h5>
        <ul class="footer-links">
          <li><a href="#duplicates" class="footer-link">Duplicate Detection</a></li>
          <li><a href="#anagrams" class="footer-link">Anagram Analysis</a></li>
          <li><a href="#frequency" class="footer-link">Frequency Insights</a></li>
          <li><a href="#pairs" class="footer-link">Pair Calculator</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h5 class="footer-subtitle">Resources</h5>
        <ul class="footer-links">
          <li><a href="https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions" target="_blank" rel="noopener noreferrer" class="footer-link">Blind 75 List</a></li>
          <li><a href="https://neetcode.io/" target="_blank" rel="noopener noreferrer" class="footer-link">NeetCode</a></li>
          <li><a href="https://github.com/your-repo/smartpack" target="_blank" rel="noopener noreferrer" class="footer-link">Source Code</a></li>
          <li><a href="#" class="footer-link">API Documentation</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h5 class="footer-subtitle">Connect</h5>
        <div class="social-links">
          <a href="https://github.com/your-repo/smartpack" target="_blank" rel="noopener noreferrer" class="social-link" title="GitHub">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
              <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
            </svg>
          </a>
          <a href="https://twitter.com/your-handle" target="_blank" rel="noopener noreferrer" class="social-link" title="Twitter">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
              <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
            </svg>
          </a>
        </div>
      </div>
    </div>
    
    <div class="footer-bottom">
      <div class="footer-bottom-content">
        <p class="copyright">
          © {currentYear} SmartPack. Built with ❤️ for DSA learners everywhere.
        </p>
        <div class="tech-stack">
          <span class="tech-badge">Svelte</span>
          <span class="tech-badge">FastAPI</span>
          <span class="tech-badge">Chart.js</span>
        </div>
      </div>
    </div>
  </div>
</footer>

<style>
  .app-footer {
    background-color: var(--neutral-900);
    color: var(--neutral-100);
    padding: var(--space-8) 0 var(--space-4) 0;
    margin-top: var(--space-10);
  }

  .footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--space-6);
    margin-bottom: var(--space-8);
  }

  .footer-section {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }

  .footer-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin: 0 0 var(--space-1) 0;
    color: var(--neutral-50);
  }

  .footer-subtitle {
    font-size: 1rem;
    font-weight: 600;
    margin: 0 0 var(--space-2) 0;
    color: var(--neutral-200);
  }

  .footer-description {
    color: var(--neutral-400);
    font-size: 0.875rem;
    line-height: 1.5;
    margin: 0;
  }

  .footer-badges {
    display: flex;
    gap: var(--space-1);
    margin-top: var(--space-2);
  }

  .footer-links {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: var(--space-1);
  }

  .footer-link {
    color: var(--neutral-400);
    text-decoration: none;
    font-size: 0.875rem;
    transition: color 0.2s ease;
  }

  .footer-link:hover {
    color: var(--primary-400);
  }

  .social-links {
    display: flex;
    gap: var(--space-2);
  }

  .social-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background-color: var(--neutral-800);
    color: var(--neutral-400);
    border-radius: var(--radius-md);
    text-decoration: none;
    transition: all 0.2s ease;
  }

  .social-link:hover {
    background-color: var(--primary-600);
    color: white;
    transform: translateY(-2px);
  }

  .footer-bottom {
    border-top: 1px solid var(--neutral-800);
    padding-top: var(--space-4);
  }

  .footer-bottom-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: var(--space-2);
  }

  .copyright {
    color: var(--neutral-500);
    font-size: 0.875rem;
    margin: 0;
  }

  .tech-stack {
    display: flex;
    gap: var(--space-1);
  }

  .tech-badge {
    background-color: var(--neutral-800);
    color: var(--neutral-300);
    padding: 0.25rem 0.5rem;
    border-radius: var(--radius-sm);
    font-size: 0.75rem;
    font-weight: 500;
  }

  @media (max-width: 768px) {
    .footer-bottom-content {
      flex-direction: column;
      text-align: center;
    }
    
    .footer-content {
      grid-template-columns: 1fr;
    }
  }
</style>