<template>
  <div class="sensor">
    <h1>Recent Sensor Data</h1>
    <!-- Table for sensor data -->
    <div class="sensor-table">
      <table>
        <thead>
          <tr>
            <th>Time</th>
            <th>Voltage (V)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="measurement in measurements" :key="measurement.time">
            <td>{{ measurement.time }}</td>
            <td>{{ measurement.voltage }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- Static ApexCharts example -->
    <div id="staticChart"></div>
    <!-- Live ApexCharts example -->
    <div id="liveChart"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted} from 'vue';
import type { Ref } from 'vue';
import axios from 'axios';
import ApexCharts, { type ApexOptions } from 'apexcharts';

interface Measurement {
  time: string;
  voltage: string;
}

export default defineComponent({
  name: 'SensorView',
  setup() {
    const measurements: Ref<Measurement[]> = ref([]);
    const staticChart: Ref<ApexCharts | null> = ref(null);
    const liveChart: Ref<ApexCharts | null> = ref(null);

    // Function to fetch sensor data from the backend
    const fetchSensorData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/microgrid_back/measurements/1/6/');
        measurements.value = response.data.measurements;
        updateStaticChart();
      } catch (error) {
        console.error('Error during Axios GET request:', error);
      }
    };

    // Initialize the static chart with empty data
    const initStaticChart = () => {
      const options: ApexOptions = {
        chart: {
          type: 'line',
          height: 'auto',
          zoom: {
            enabled: true,
            type: 'x',  
            autoScaleYaxis: true  
          },
          toolbar: {
            autoSelected: 'zoom' 
          }
        },
        series: [{
          name: 'Voltage',
          data: []
        }],
        xaxis: {
          type: 'datetime',
          labels: {
    formatter: function(value, timestamp) {
      // Check if timestamp is defined to avoid TypeScript error
      if (typeof timestamp !== 'undefined') {
        return new Date(timestamp).toISOString().slice(17, 23); // Display only the seconds and microseconds
      }
      return ''; // Return an empty string or some default value if timestamp is undefined
    }
  },
          tickAmount: 10, // Adjust this value as needed for your data
          range: 1000 // This will need to be adjusted based on the actual range of your data
        },
        tooltip: {
          x: {
            format: 'HH:mm:ss.SSS' // Format tooltip to show hours, minutes, seconds, and milliseconds
          }
        },
        theme: {
          mode: 'dark'
        }
      };

      staticChart.value = new ApexCharts(document.querySelector("#staticChart"), options);
      staticChart.value.render();
    };

    // Update the static chart with new data
    const updateStaticChart = () => {
  if (staticChart.value) {
    const seriesData = measurements.value.map(m => {
      // Ensure that m.time is not undefined
      const time = m.time ? new Date(m.time) : new Date();
      return {
        x: time,
        y: parseFloat(m.voltage)
      };
    });

    staticChart.value.updateSeries([{ data: seriesData }]);
  }
};

    // Initialize the live chart with empty data
    const initLiveChart = () => {
      const options: ApexOptions = {
        chart: {
          type: 'line',
          height: 'auto',
          animations: {
            enabled: true,
            dynamicAnimation: {
              speed: 1000
            }
          }
        },
        series: [{
          name: 'Live Voltage',
          data: []
        }],
        xaxis: {
          type: 'datetime',
          labels: {
    formatter: function(value, timestamp) {
      // Check if timestamp is defined to avoid TypeScript error
      if (typeof timestamp !== 'undefined') {
        return new Date(timestamp).toISOString().slice(17, 23); // Display only the seconds and microseconds
      }
      return ''; // Return an empty string or some default value if timestamp is undefined
    }
  },
          tickAmount: 1, // Adjust this value as needed for your data
          range: 10 // This will need to be adjusted based on the actual range of your data
        },
        tooltip: {
          x: {
            format: 'HH:mm:ss.SSS' // Format tooltip to show hours, minutes, seconds, and milliseconds
          }
        },
        theme: {
          mode: 'dark'
        }
      };

      liveChart.value = new ApexCharts(document.querySelector("#liveChart"), options);
      liveChart.value.render();
    };

// Poll for live data every second and update the live chart
const pollLiveData = () => {
  setInterval(async () => {
    try {
      const response = await axios.get('http://localhost:8000/microgrid_back/measurements/1/6/');
      const latestMeasurement = response.data.measurements[response.data.measurements.length - 1];
      if (liveChart.value && latestMeasurement.time) {
        const time = new Date(latestMeasurement.time);
        const voltage = parseFloat(latestMeasurement.voltage);
        liveChart.value.appendData([{
          data: [{ x: time, y: voltage }]
        }]);
      }
    } catch (error) {
      console.error('Error during live data polling:', error);
    }
  }, 5000);
};

    onMounted(() => {
      initStaticChart();
      initLiveChart();
      fetchSensorData();
      pollLiveData();
    });

    return { measurements, staticChart, liveChart };
  }
});
</script>


<style scoped>
.home {
  padding: 1rem;
}

.home-table {
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
  .home {
    padding: 0.5rem;
  }

  table {
    font-size: 0.8rem;
  }
}
</style>