<template>
    <div class=""
         v-for="synth in synths"
         v-bind:key="synth.id"
    >
        <a class="">{{synth.name}}</a>    
    </div>    
 


</template>

<script>
import axios from 'axios';

export default {
  name: 'synthList',
  data() {
    return {
      synths: [],
    };
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
  addSynths(){
    axios.post('/api/v1/synths/')
    .then

  }
}

}

</script>