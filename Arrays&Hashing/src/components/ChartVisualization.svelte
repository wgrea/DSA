<script lang="ts">
  import { onMount } from 'svelte';
  import { Chart, registerables } from 'chart.js';
  
  export let data: any;
  export let algorithm: string;
  
  Chart.register(...registerables);
  
  let chartCanvas: HTMLCanvasElement;
  let chartInstance: Chart | null = null;
  
  onMount(() => {
    createChart();
    return () => {
      if (chartInstance) {
        chartInstance.destroy();
      }
    };
  });
  
  $: if (data && chartInstance) {
    updateChart();
  }
  
  function createChart() {
    if (!chartCanvas || !data) return;
    
    const config = getChartConfig();
    chartInstance = new Chart(chartCanvas, config);
  }
  
  function updateChart() {
    if (!chartInstance) return;
    
    const config = getChartConfig();
    chartInstance.data = config.data;
    chartInstance.options = config.options;
    chartInstance.update();
  }
  
  function getChartConfig() {
    switch (algorithm) {
      case 'duplicates':
        return getDuplicateChart();
      case 'frequency':
        return getFrequencyChart();
      case 'anagrams':
        return getAnagramChart();
      case 'pairs':
        return getPairChart();
      case 'sequences':
        return getSequenceChart();
      default:
        return getGenericChart();
    }
  }
  
  function getDuplicateChart() {
    const frequencies = Object.values(data.frequency);
    const labels = Object.keys(data.frequency);
    
    return {
      type: 'bar',
      data: {
        labels,
        datasets: [{
          label: 'Frequency',
          data: frequencies,
          backgroundColor: frequencies.map((freq: number) => 
            freq > 1 ? 'rgba(239, 68, 68, 0.8)' : 'rgba(34, 197, 94, 0.8)'
          ),
          borderColor: frequencies.map((freq: number) => 
            freq > 1 ? 'rgba(239, 68, 68, 1)' : 'rgba(34, 197, 94, 1)'
          ),
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Element Frequency Distribution'
          },
          legend: {
            display: false
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Frequency'
            }
          },
          x: {
            title: {
              display: true,
              text: 'Elements'
            }
          }
        }
      }
    };
  }
  
  function getFrequencyChart() {
    const frequencies = Object.values(data.frequency_map);
    const labels = Object.keys(data.frequency_map);
    
    return {
      type: 'doughnut',
      data: {
        labels,
        datasets: [{
          data: frequencies,
          backgroundColor: [
            'rgba(59, 130, 246, 0.8)',
            'rgba(16, 185, 129, 0.8)',
            'rgba(245, 158, 11, 0.8)',
            'rgba(239, 68, 68, 0.8)',
            'rgba(139, 92, 246, 0.8)',
            'rgba(236, 72, 153, 0.8)'
          ],
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: `Top ${data.top_k_elements?.length || 'K'} Frequent Elements`
          }
        }
      }
    };
  }
  
  function getAnagramChart() {
    if (data.type === 'anagram_check') {
      const freq1 = Object.values(data.string1.frequency);
      const freq2 = Object.values(data.string2.frequency);
      const labels = Object.keys(data.string1.frequency);
      
      return {
        type: 'bar',
        data: {
          labels,
          datasets: [
            {
              label: `"${data.string1.text}"`,
              data: freq1,
              backgroundColor: 'rgba(59, 130, 246, 0.8)',
              borderColor: 'rgba(59, 130, 246, 1)',
              borderWidth: 2
            },
            {
              label: `"${data.string2.text}"`,
              data: freq2,
              backgroundColor: 'rgba(16, 185, 129, 0.8)',
              borderColor: 'rgba(16, 185, 129, 1)',
              borderWidth: 2
            }
          ]
        },
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: 'Character Frequency Comparison'
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Frequency'
              }
            },
            x: {
              title: {
                display: true,
                text: 'Characters'
              }
            }
          }
        }
      };
    } else {
      // Group anagrams visualization
      const groupSizes = data.groups.map(group => group.length);
      const labels = data.groups.map((group, index) => `Group ${index + 1}`);
      
      return {
        type: 'pie',
        data: {
          labels,
          datasets: [{
            data: groupSizes,
            backgroundColor: [
              'rgba(59, 130, 246, 0.8)',
              'rgba(16, 185, 129, 0.8)',
              'rgba(245, 158, 11, 0.8)',
              'rgba(239, 68, 68, 0.8)',
              'rgba(139, 92, 246, 0.8)'
            ],
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: 'Anagram Groups Distribution'
            }
          }
        }
      };
    }
  }
  
  function getPairChart() {
    const array = data.array;
    const solution = data.solution;
    
    return {
      type: 'scatter',
      data: {
        datasets: [{
          label: 'Array Elements',
          data: array.map((value, index) => ({ x: index, y: value })),
          backgroundColor: array.map((_, index) => 
            solution && (index === solution[0] || index === solution[1]) 
              ? 'rgba(239, 68, 68, 0.8)' 
              : 'rgba(59, 130, 246, 0.8)'
          ),
          borderColor: array.map((_, index) => 
            solution && (index === solution[0] || index === solution[1]) 
              ? 'rgba(239, 68, 68, 1)' 
              : 'rgba(59, 130, 246, 1)'
          ),
          pointRadius: 8,
          pointHoverRadius: 10
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: `Two Sum: Target = ${data.target}`
          }
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Array Index'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Value'
            }
          }
        }
      }
    };
  }
  
  function getSequenceChart() {
    const sequences = data.sequences || [];
    
    return {
      type: 'bar',
      data: {
        labels: sequences.map((seq, index) => `Seq ${index + 1}`),
        datasets: [{
          label: 'Sequence Length',
          data: sequences.map(seq => seq.length),
          backgroundColor: sequences.map(seq => 
            seq.is_longest ? 'rgba(239, 68, 68, 0.8)' : 'rgba(59, 130, 246, 0.8)'
          ),
          borderColor: sequences.map(seq => 
            seq.is_longest ? 'rgba(239, 68, 68, 1)' : 'rgba(59, 130, 246, 1)'
          ),
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Consecutive Sequences Found'
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Sequence Length'
            }
          }
        }
      }
    };
  }
  
  function getGenericChart() {
    return {
      type: 'bar',
      data: {
        labels: ['Data'],
        datasets: [{
          label: 'Value',
          data: [1],
          backgroundColor: 'rgba(59, 130, 246, 0.8)',
          borderColor: 'rgba(59, 130, 246, 1)',
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Algorithm Visualization'
          }
        }
      }
    };
  }
</script>

<div class="chart-container">
  <canvas bind:this={chartCanvas}></canvas>
</div>

<style>
  .chart-container {
    position: relative;
    height: 300px;
    background-color: var(--bg-secondary);
    border-radius: var(--radius-md);
    padding: var(--space-2);
  }

  @media (max-width: 768px) {
    .chart-container {
      height: 250px;
    }
  }
</style>