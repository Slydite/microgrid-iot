<template>
  <div class="about">
    <h1>This is an about page</h1>
    <!-- Add a div element for the chart with an id -->
    <div id="chart"></div>
  </div>
</template>

<script>
// Import the necessary ApexCharts components
import ApexCharts from 'apexcharts'

export default {
  name: 'About',
  // Use the mounted lifecycle hook to render the chart when the component is mounted
  mounted() {
    var options = {
      chart: {
        type: 'line',
        height: 'auto',
        // Add theme configuration for dark mode
        foreColor: '#fff', // This will change the text color to white
        toolbar: {
          show: false
        }
      },
      series: [{
        name: 'sales',
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125]
      }],
      xaxis: {
        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
      },
      // Add theme property to the options
      theme: {
        mode: 'dark', // This will set the chart to dark mode
        palette: 'palette7' // You can choose from palette1 to palette10
      }
    }

    var chart = new ApexCharts(document.querySelector("#chart"), options);

    chart.render();

  }
}
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
    flex-direction: column;
    /* Add this to align items vertically */
  }
}
</style>
