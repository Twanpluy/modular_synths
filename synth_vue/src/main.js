import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './index.css'
import axios from 'axios'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";



axios.defaults.baseURL = 'http://127.0.0.1:8000/'


const options = {
    // You can set your default options here
    timeout:2000
};

createApp(App).use(store,).use(router, axios).use(Toast, options).mount('#app')


