<template>
<div class="synth-list">

  <button class="button bg-green-600 rounded-3xl" @click="addSynth()">Add Synth</button>

  <div class="overflow-x-auto relative shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" class="py-3 px-6">
                    Name
                </th>
                <th scope="col" class="py-3 px-6">
                    Description
                </th>
                <th scope="col" class="py-3 px-6">
                    Type
                </th>
                <th scope="col" class="py-3 px-6">
                  <span class="sr-only">
                    Edit</span>
                </th>
                <th scope="col" class="py-3 px-6">
                  Delete
                </th>
            </tr>
        </thead>
  <tbody>
    <tr v-for="synth in synths" :key="synth.id">
      <td>{{synth.name}}</td>
      <td>{{synth.description}}</td>
      <td>{{synth.type}}</td>
      <td><router-link :to="'/synth/' + synth.id + '/edit'">Edit</router-link></td>
      <td><button class="bg-red-700 round text-slate-400 hover:text-blue-600" @click="deleteSynth(synth.id)">Delete</button></td>
    </tr>

  </tbody>
</table>
</div>
</div>
</template>

<script>
import axios from 'axios';
import { useToast } from "vue-toastification";
import "vue-toastification/dist/index.css";


export default {
  name: 'synthList',
  data() {
    return {
      synths: [],
    };
  },
  setup() {
    const toast = useToast();
          // or with options
      return { toast }

  },
  mounted() {
    this.getSynths();
  },
  methods : {
    getSynths(){
    axios.get('/api/v1/synths/')
    .then(response => {
        for (let i = 0; i < response.data.length; i++){
            this.synths.push(response.data[i])
        }
    }).catch(error => {
        console.log(JSON.stringify(error))
    } )
  },
    addSynth(){
    axios.post('/api/v1/synths/', {
        name: "test",
        description: "test",
        price: 0,
        image: "test",
        owner: 1
    }).then(response => {
        this.synths.push(response.data)
        this.toast.success("Synth added")
    }).catch(error => {
      this.toast.error("Synth not added")
        console.log(JSON.stringify(error))
    } )
    },
    deleteSynth(id){
    axios.delete('/api/v1/synths/' + id + '/')
    .then(response => {
        this.synths = this.synths.filter(synth => synth.id !== id)
        this.toast.success("Synth deleted")
    }).catch(error => {
      this.toast.error("Synth not deleted")
        console.log(JSON.stringify(error))
    } )
    }
  },
  }
</script>