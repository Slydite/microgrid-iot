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
          <tr v-for="measurement in slicedMeasurements" :key="measurement.time">
            <td>{{ measurement.time }}</td>
            <td>{{ measurement.voltage }}</td>
          </tr>
        </tbody>
        
      </table>
    </div>

    <br></br>
    <br></br>
    <!-- Static ApexCharts example -->
    <div id="staticChart"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from 'vue';
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

      const fetchSensorData = async () => {
  try {
    let url;
    const currentHour = new Date().getHours();
    url = 'http://localhost:8000/microgrid_back/measurements/6/6/';
    // if (currentHour >= 0 && currentHour < 4) {
    //   url = 'http://localhost:8000/microgrid_back/measurements/1/6/';
    // } else if (currentHour >= 4 && currentHour < 8) {
    //   url = 'http://localhost:8000/microgrid_back/measurements/2/6/';
    // } else if (currentHour >= 8 && currentHour < 12) {
    //   url = 'http://localhost:8000/microgrid_back/measurements/3/6/';
    // } else if (currentHour >= 12 && currentHour < 16) {
    //   url = 'http://localhost:8000/microgrid_back/measurements/4/6/';
    // } else if (currentHour >= 16 && currentHour < 20) {
    //   url = 'http://localhost:8000/microgrid_back/measurements/5/6/';
    // } else {
    //   url = 'http://localhost:8000/microgrid_back/measurements/6/6/';
    // }

    const response = await axios.get(url);
    measurements.value = response.data.measurements;
    updateStaticChart();
  } catch (error) {
    console.error('Error during Axios GET request:', error);
  }
};

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
          tickAmount: 10,
          labels: {
            formatter: function(value, timestamp) {
              if (typeof timestamp !== 'undefined') {
                return new Date(timestamp).toISOString().slice(17, 23);
              }
              return '';
            }
          },
          range: 1000
        },
        tooltip: {
          x: {
            format: 'HH:mm:ss.SSS'
          }
        },
        theme: {
          mode: 'dark'
        }
      };

      staticChart.value = new ApexCharts(document.querySelector("#staticChart"), options);
      staticChart.value.render();
    };

    const updateStaticChart = () => {
      if (staticChart.value) {
        const seriesData = measurements.value.map(m => {
          const time = new Date(m.time).getTime();
          return {
            x: time,
            y: parseFloat(m.voltage)
          };
        });

        staticChart.value.updateSeries([{ data: seriesData }]);
      }
    };

    onMounted(() => {
      fetchSensorData();
      initStaticChart();
      
      // Refresh chart data every 2 seconds
      setInterval(fetchSensorData, 5000);
    });

    const slicedMeasurements = computed(() => {
      return measurements.value.slice(0, 10);
    });

    return { measurements, staticChart, slicedMeasurements };
  }
});
</script>


<style scoped>
.home {
  padding: 1rem;
}
h1{
  color: white;
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
  color: white;
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