<template>
  <div class="sensor">
    <!-- New table for THD, Power Factor, and RMS readings -->
    <div class="sensor-table">
      <h1>Real-Time Readings of {{ sensorName }}</h1>
      <table>
        <thead>
          <tr>
            <th>THD (%)</th>
            <th>Power Factor</th>
            <th>RMS</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{ thd }}</td>
            <td>{{ powerFactor }}</td>
            <td>{{ rms }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <h1>{{ sensorType }} Data</h1>
    <!-- Table for sensor data -->
    <div class="sensor-table">
      <table>
        <thead>
          <tr>
            <th>Time</th>
            <th>Readings</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(data, index) in recentSensdataData" :key="index">
            <td>{{ data.time }}</td>
            <td>{{ data.sensdata }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Chart placeholder -->
    <div id="staticChart"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted, type Ref } from 'vue'
import axios from 'axios'
import ApexCharts, { type ApexOptions } from 'apexcharts'
import { useRoute } from 'vue-router'

interface SensdataMeasurement {
  sensdata: [string, string][] // 2D array of sensdata and deltaT
  time: string // Start time
  thd: string
  rms: string
  pf: string
  sname: string
  stype: string
}

interface SensdataData {
  sensdata: string
  time: string
}

export default defineComponent({
  name: 'SensorView',
  setup() {
    const route = useRoute()
    const sensorNumber = route.query.number
    const measurement: Ref<SensdataMeasurement | null> = ref(null)
    const staticChart: Ref<ApexCharts | null> = ref(null)
    const startTime: Ref<Date> = ref(new Date())
    const thd: Ref<string> = ref('0')
    const powerFactor: Ref<string> = ref('0')
    const rms: Ref<string> = ref('0')
    const sensorName: Ref<string> = ref('0')
    const sensorType: Ref<string> = ref('0')

    const fetchSensorData = async () => {
      try {
        const currentTime = new Date()
        const currentHour = currentTime.getHours()
        const tableNumber = Math.floor(currentHour / 4) + 1 // Calculate table number based on time
        //const url = `http://localhost:8000/microgrid_back/measurements/6/6/`
        // const url = `http://localhost:8000/microgrid_back/measurements/${tableNumber}/${sensorNumber}/`
        const url = `http://localhost:8000/microgrid_back/measurements/6/${sensorNumber}/`
        const response = await axios.get(url)
        const data: SensdataMeasurement = response.data.measurements
        startTime.value = new Date(data.time)
        measurement.value = data
        thd.value = data.thd
        powerFactor.value = data.pf
        rms.value = data.rms
        sensorName.value = data.sname
        sensorType.value = data.stype
        updateStaticChart()
      } catch (error) {
        console.error('Error during Axios GET request:', error)
      }
    }

    const recentSensdataData = computed((): SensdataData[] => {
      return (
        measurement.value?.sensdata.slice(0, 20).map((sensdataTuple) => {
          const sensdataValue = sensdataTuple[0]
          const deltaTime = parseFloat(sensdataTuple[1])
          const measurementTime = new Date(startTime.value.getTime() + deltaTime).toISOString()
          return {
            sensdata: sensdataValue,
            time: measurementTime
          }
        }) || []
      )
    })

    const initStaticChart = () => {
      const options: ApexOptions = {
        chart: {
          type: 'line',
          height: 1000,
          width: 2000,
          zoom: {
            enabled: true,
            type: 'x',
            autoScaleYaxis: true
          },
          toolbar: {
            autoSelected: 'zoom'
          }
        },
        series: [
          {
            name: 'Sensdata',
            data: []
          }
        ],
        xaxis: {
          type: 'datetime',
          labels: {
            formatter: function (value, timestamp) {
              return new Date(value).toISOString().slice(11, 23)
            }
          }
        },
        tooltip: {
          x: {
            formatter: function (value, timestamp) {
              return new Date(value).toISOString().slice(11, 23)
            }
          }
        },
        theme: {
          mode: 'dark'
        }
      }

      staticChart.value = new ApexCharts(document.querySelector('#staticChart'), options)
      staticChart.value.render()
    }

    const updateStaticChart = () => {
      if (staticChart.value && measurement.value) {
        const seriesData = measurement.value.sensdata.map((sensdataTuple) => {
          const sensdataValue = sensdataTuple[0]
          const deltaTime = parseFloat(sensdataTuple[1])
          const timeValue = new Date(startTime.value.getTime() + deltaTime).toISOString()
          return {
            x: timeValue,
            y: parseFloat(sensdataValue)
          }
        })

        // Update the series data
        staticChart.value.updateSeries([
          {
            name: 'Sensdata',
            data: seriesData
          }
        ])
      }
    }

    onMounted(() => {
      fetchSensorData()
      initStaticChart()
      setInterval(fetchSensorData, 3000)
    })

    return {
      recentSensdataData,
      thd,
      powerFactor,
      rms,
      sensorName,
      sensorType
    }
  }
})
</script>

<style scoped>
.home {
  padding: 1rem;
}
h1 {
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
  background-color: #04aa6d;
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
