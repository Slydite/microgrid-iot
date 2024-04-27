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
          <tr v-for="(data, index) in recentVoltageData" :key="index">
            <td>{{ data.time }}</td>
            <td>{{ data.voltage }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Chart placeholder -->
    <div id="staticChart"></div>
  </div>
</template>


<script lang="ts">
import { defineComponent, ref, computed, onMounted, type Ref } from 'vue';
import axios from 'axios';
import ApexCharts, { type ApexOptions } from 'apexcharts';

interface VoltageMeasurement {
  voltage: [string, string][]; // 2D array of voltage and deltaT
  time: string; // Start time
}

interface VoltageData {
  voltage: string;
  time: string;
}

export default defineComponent({
  name: 'SensorView',
  setup() {
    const measurement: Ref<VoltageMeasurement | null> = ref(null);
    const staticChart: Ref<ApexCharts | null> = ref(null);
    const startTime: Ref<Date> = ref(new Date());

    const fetchSensorData = async () => {
      try {
        const url = 'http://localhost:8000/microgrid_back/measurements/6/6/';
        const response = await axios.get(url);
        const data: VoltageMeasurement = response.data.measurements;
        startTime.value = new Date(data.time);
        measurement.value = data;
        updateStaticChart();
      } catch (error) {
        console.error('Error during Axios GET request:', error);
      }
    };

    const recentVoltageData = computed((): VoltageData[] => {
      return measurement.value?.voltage.slice(-10).map(voltageTuple => {
        const voltageValue = voltageTuple[0];
        const deltaTime = parseFloat(voltageTuple[1]);
        const measurementTime = new Date(startTime.value.getTime() + deltaTime*1000).toISOString();
        return {
          voltage: voltageValue,
          time: measurementTime
        };
      }) || [];
    });

    const initStaticChart = () => {
      const options: ApexOptions = {
        chart: {
          type: 'line',
          height: 'auto',
          width: 1000,
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
                return new Date(timestamp).toISOString().slice(11, 23);
              }
              return '';
            }
          },//BT
          range: 1000, // 1 second range for 1000Hz polling rate
          min: startTime.value.getTime(), // Use the startTime ref for the minimum value
          max: startTime.value.getTime() + 999  // Use the startTime ref + 999 seconds for the maximum value
        },
        yaxis: {
          min: -300, // Set the minimum value of y-axis to -300
          max: 300, // Set the maximum value of y-axis to 300
          tickAmount: 10
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
    if (staticChart.value && measurement.value) {
      const seriesData = measurement.value.voltage.map(voltageTuple => {
        const voltageValue = voltageTuple[0];
        const deltaTime = parseFloat(voltageTuple[1]);
        const timeValue = new Date(startTime.value.getTime() + deltaTime * 1000);
        return {
          x: timeValue.getTime(),
          y: parseFloat(voltageValue)
        };
      });

      // Update the series data
      staticChart.value.updateSeries([{ data: seriesData }]);

      // Update the x-axis labels to reflect the new time
      staticChart.value.updateOptions({
        xaxis: {
          min: startTime.value.getTime(),
          max: startTime.value.getTime() + (measurement.value.voltage.length - 1) * 1000,
          tickAmount: 10, // Adjust this value as needed for your desired number of ticks
          labels: {
            formatter: function(value: any, timestamp: string | number | Date) {
              if (typeof timestamp !== 'undefined' && typeof value !== 'undefined') {
                return new Date(timestamp).toISOString().slice(11, 23);
              }
              return '';}
          }
        }
      }, false, true); // The second parameter (false) prevents the chart from re-rendering entirely
    }
  };

    onMounted(() => {
      fetchSensorData();
      initStaticChart();
      setInterval(fetchSensorData, 1000);
    });

    return {
      recentVoltageData
    };
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