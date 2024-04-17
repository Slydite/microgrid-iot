<script setup lang="ts">
import { ref, type Ref } from 'vue';
import { RouterLink, RouterView, useRoute } from 'vue-router';
import { HomeIcon, BoltIcon, PlusIcon } from '@heroicons/vue/24/solid';

interface Sensor {
  name: string;
  path: string;
  icon: any; // Use appropriate type for your icon components
}

const sensors: Ref<Array<Sensor>> = ref([
  { name: 'Home', path: '/', icon: HomeIcon },
  { name: 'Sensor 1', path: '/sensor', icon: BoltIcon },
  // ... more sensors
]);

// Function to add a new sensor
function addSensor(name: string) {
  const NewIcon = BoltIcon; // Placeholder for new sensor icon
  sensors.value.push({ name, path: '/sensor', icon: NewIcon });
}

// Function to remove a sensor by name
function removeSensor(name: string) {
  sensors.value = sensors.value.filter(sensor => sensor.name !== name);
}

// Function to add a placeholder sensor when the plus button is clicked
function addPlaceholderSensor() {
  const newSensorName = `Sensor ${sensors.value.length + 1}`;
  addSensor(newSensorName);
}

const route = useRoute();
</script>

<template>
  <div id="app">
    <header>
      <h1>Microgrid</h1>
      <input type="search" placeholder="Search..." />
    </header>
    <aside>
      <nav>
        <ul>
          <li v-for="sensor in sensors" :key="sensor.name">
            <!-- Pass the sensor name as a route query parameter -->
            <router-link :to="{ path: sensor.path, query: { name: sensor.name } }">
              <component :is="sensor.icon" class="icon" />
              <span class="text">{{ sensor.name }}</span>
            </router-link>
          </li>
          <!-- Plus button to add a new sensor -->
          <li>
            <button @click="addPlaceholderSensor">
              <PlusIcon class="icon" />
              <span class="text">Add Sensor</span>
            </button>
          </li>
        </ul>
      </nav>
    </aside>
    <main>
      <router-view />
    </main>
  </div>
</template><style scoped>
:root {
  --color-background: #013220; /* Dark green background */
  --color-text: #ffffff; /* White text color */
  --color-icon: #4caf50; /* Lighter green for icons */
  --color-button: #064f2e; /* Dark green for buttons */
  --color-button-hover: #026e3d; /* Slightly lighter green for button hover state */
}

body {
  background-color: var(--color-background); /* Apply the background color to the entire app */
}

header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--color-background);
  padding: 1rem;
  z-index: 1000; /* Ensure the header is above other elements */
}

input[type="search"] {
  margin-left: auto;
  background-color: #022c1a; /* Darker green background for search input */
  color: var(--color-text); /* White color for search input text */
  border: none; /* Remove default border */
  padding: 0.5rem;
  border-radius: 4px;
}

aside {
  width: 50px;
  transition: width 0.5s;
  position: fixed;
  top: 60px; /* Adjust top position to not overlap with the header */
  left: 0;
  height: calc(100vh - 60px);
  overflow-y: auto;
  background-color: var(--color-background);
  z-index: 1100; /* Higher z-index for the sidebar to be clickable */
}

aside:hover {
  width: 200px;
}

aside nav ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

aside nav ul li a,
aside nav ul li button {
  display: flex;
  align-items: center;
  padding: 10px;
  overflow: hidden;
  text-decoration: none;
  color: var(--color-text); /* White color for text */
  transition: background-color 0.3s;
}

aside nav ul li button {
  background-color: var(--color-button);
}

aside nav ul li button:hover {
  background-color: var(--color-button-hover);
}

.icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
  color: var(--color-icon); /* Green color for icons */
}

.text {
  white-space: nowrap;
  overflow: hidden;
  transition: opacity 0.5s, max-width 0.5s;
  opacity: 0;
  max-width: 0;
}

aside:hover .text {
  opacity: 1;
  max-width: 100px; /* Adjust max-width for text visibility */
}

main {
  flex: 1;
  padding: 1rem;
  margin-left: 50px;
  margin-top: 4rem;
  transition: margin-left 0.5s;
}

@media (max-width: 768px) {
  header {
    position: relative;
  }

  aside {
    width: 100%;
    height: auto;
    position: relative;
    top: auto;
    overflow-y: visible;
  }

  aside nav ul {
    flex-direction: row;
    justify-content: space-around;
  }

  aside nav ul li a,
  aside nav ul li button {
    flex-direction: column;
  }

  .icon {
    margin: 0;
    margin-bottom: 4px;
  }

  .text {
    display: block;
    font-size: 0.75rem;
    max-width: none;
    opacity: 1;
  }

  main {
    margin-left: 0;
    margin-top: 60px;
  }
}
</style>


<!-- 
<style scoped>
header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--color-sidebar);
  padding: 1rem;
  z-index: 1000;
  overflow-x: hidden;
  /* Hide horizontal scrollbar */
}

input[type="search"] {
  margin-left: auto;
}

aside {
  width: 50px;
  transition: width 0.5s;
  position: fixed;
  top: 60px;
  left: 0;
  height: calc(100vh - 60px);
  overflow-y: auto;
  background-color: var(--color-sidebar);
  z-index: 500;
}

aside:hover {
  width: 200px;
}

aside nav ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

aside nav ul li a,
aside nav ul li button {
  display: flex;
  align-items: center;
  padding: 10px;
  overflow: hidden;
  text-decoration: none;
  color: var(--color-text);
}

.icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
  opacity: 1;
}

.text {
  white-space: nowrap;
  overflow: hidden;
  transition: opacity 0.5s, max-width 0.5s;
  opacity: 0;
  max-width: 0;
}

aside:hover .text {
  opacity: 1;
  max-width: 100px;
}

main {
  flex: 1;
  padding: 1rem;
  margin-left: 50px;
  margin-top: 4rem;
  transition: margin-left 0.5s;
}

/* Update colors */
aside nav ul li a,
aside nav ul li button {
  color: grey;
  /* Updated text color */
}

aside nav ul li button {
  background-color: black;
  /* Updated background color */
}

/* Green color for list items */
aside nav ul li a .icon {
  color: rgb(26, 241, 26);
}

@media (max-width: 768px) {
  header {
    position: relative;
  }

  aside {
    width: 100%;
    height: auto;
    position: relative;
    top: auto;
    overflow-y: visible;
  }

  aside nav ul {
    flex-direction: row;
    justify-content: space-around;
  }

  aside nav ul li a,
  aside nav ul li button {
    flex-direction: column;
  }

  .icon {
    margin: 0;
    margin-bottom: 4px;
  }

  .text {
    display: block;
    font-size: 0.75rem;
    max-width: none;
    opacity: 1;
  }

  main {
    margin-left: 0;
    margin-top: 60px;
  }
}
</style> -->

