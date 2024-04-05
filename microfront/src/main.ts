import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'

// HTTP connection to the API
const httpLink = createHttpLink({
  // You should use an absolute URL here
  uri: 'http://127.0.0.1:8000/graphql/',
})

// Cache implementation
const cache = new InMemoryCache()

// Create the apollo client
const apolloClient = new ApolloClient({
  link: httpLink,
  cache,
})
const app=createApp({
    setup() {
        provide(DefaultAppolloClient, apolloClient)
        
    },
    render: () => h(App)
    

})

app.mount('#app')


import './assets/main.css'

//import { createApp } from 'vue'
//import { createPinia } from 'pinia'

//import App from './App.vue'
//import router from './router'

//const app = createApp(App)

//app.use(createPinia())
//app.use(router)

//app.mount('#app')
