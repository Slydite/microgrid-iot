import { createApp, provide, h } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import { ApolloClient, InMemoryCache, split, HttpLink } from '@apollo/client/core';
import { DefaultApolloClient } from '@vue/apollo-composable';
import { createClient } from 'graphql-ws';
import { getMainDefinition } from '@apollo/client/utilities';
import { WebSocketLink } from '@apollo/client/link/ws';

// Create an HTTP link for queries and mutations
const httpLink = new HttpLink({
    uri: 'http://127.0.0.1/graphql', // Use your HTTP GraphQL endpoint here
});

// Create a WebSocket client
const wsClient = createClient({
    url: 'ws://127.0.0.1/graphql', // Use your WebSocket GraphQL endpoint here
});

// Create a link that routes to the WebSocket link or HTTP link based on operation type
const link = split(
    ({ query }) => {
        const definition = getMainDefinition(query);
        return (
            definition.kind === 'OperationDefinition' &&
            definition.operation === 'subscription'
        );
    },
    new WebSocketLink(wsClient), // Use WebSocket link for subscriptions
    httpLink, // Use HTTP link for queries and mutations
);

// Create the Apollo Client instance
const apolloClient = new ApolloClient({
    link,
    cache: new InMemoryCache(),
});

// Create the Vue application
const app = createApp({
    setup() {
        provide(DefaultApolloClient, apolloClient);
    },
    render: () => h(App),
});

app.use(createPinia());
app.use(router);

app.mount('#app');
