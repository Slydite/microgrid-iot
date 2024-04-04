<template>
  <div class="sensor">
    <h1>Recent Sensor Data</h1>
    <!-- Table for sensor data -->
    <div class="sensor-table">
      <table>
        <thead>
          <tr>
            <th>RMS Current (A)</th>
            <th>Voltage (V)</th>
            <th>Power Factor</th>
            <th>THD (%)</th>
            <!-- Add more columns as needed -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="data in sensorData" :key="data.id">
            <td>{{ data.current }}</td>
            <td>{{ data.voltage }}</td>
            <td>{{ data.powerFactor }}</td>
            <td>{{ data.thd }}</td>
            <!-- Add more data cells as needed -->
          </tr>
        </tbody>
      </table>
    </div>
    <!-- ApexCharts example -->
    <div id="chart"></div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import ApexCharts from 'apexcharts';

export default {
  name: 'SensorView',
  setup() {
    // Synthetic data for sensor readings
    const sensorData = ref([
      { id: 1, current: 5.2, voltage: 220, powerFactor: 0.95, thd: 5 },
      { id: 2, current: 5.4, voltage: 225, powerFactor: 0.96, thd: 4 },
      { id: 3, current: 5.6, voltage: 230, powerFactor: 0.97, thd: 6 },
      { id: 4, current: 5.8, voltage: 235, powerFactor: 0.98, thd: 3 }
    ]);

    // Initialize the chart
    const initChart = () => {
      const options = {
        chart: {
          type: 'line',
          height: 'auto',
          foreColor: '#fff',
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
        theme: {
          mode: 'dark',
          palette: 'palette7'
        }
      };

      const chart = new ApexCharts(document.querySelector("#chart"), options);
      chart.render();
    };

    onMounted(() => {
      initChart();
    });

    return { sensorData };
  }
}
</script>

<style scoped>
.sensor {
  padding: 1rem;
}

.sensor-table {
  margin-top: 2rem;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #04AA6D;
  color: white;
}

@media (max-width: 768px) {
  .sensor {
    padding: 0.5rem;
  }

  table {
    font-size: 0.8rem;
  }
}
</style>
