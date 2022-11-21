<template>
    <div class="page-signup">
<section class="h-screen">
  <div class="px-6 h-full text-gray-800 bg-slate-200">
    <div
      class="flex xl:justify-center lg:justify-between justify-center items-center flex-wrap h-full g-6"
    >

      <div class="xl:ml-20 xl:w-5/12 lg:w-5/12 md:w-8/12 mb-12 md:mb-0 border-spacing-3 border-cyan-200">
        <form @submit.prevent="submitForm">

            <div class="flex flex-col mb-6">
                <label for="name" class="mb-2 text-sm font-bold text-gray-700">Username</label>
                <input type="text" id="username" placeholder="Enter your username" class="border rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" v-model="username">
            </div>    


            <div class="flex flex-col mb-6">
                <label for="email" class="mb-2 text-sm font-bold text-gray-700">Email</label>
                <input type="text" id="email" placeholder="Enter your email" class="border rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" v-model="email">
            </div>    


            <div class="flex flex-col mb-6">
                <label for="password" class="mb-2 text-sm font-bold text-gray-700">Password</label>
                <input type="password" id="password" placeholder="Enter your password" class="border rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" v-model="password">
            </div>    


            <div class="flex flex-col mb-6">
                <label for="password" class="mb-2 text-sm font-bold text-gray-700">Repeat Password</label>
                <input type="password" id="password1" placeholder="Repeat password" class="border rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" v-model="password1">
            </div>    

            <div class="text-center lg:text-left">
                <div class="field">
                    <div class="control">
                    </div>
            <button
              type="submit"
              class="inline-block px-7 py-3 bg-blue-600 text-white font-medium text-sm leading-snug uppercase rounded shadow-md 
                    hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
                    active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out" 
            >
              Sign Up
            </button>
        </div>

          </div>

          <div class="text-center mt-6" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error" 
                  class="text-red-500 text-sm">
                {{ error }}
            </p>
            
          </div>
         </form>
      </div>
    </div>
  </div>
</section>

    </div>
</template>

<script>
import axios from 'axios';

    export default {
        name: "SignUp",
        data() {
            return {
                username: "",
                email: "",
                password: "",
                password1: "",
                errors: []
            }
        },
        methods:{
            submitForm(e){
                
                console.log("submitting form");

                this.errors = []

                if(this.password !== this.password1){
                    this.errors.push("Passwords do not match");
                }
                if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }
            console.log(formData);
    
            axios.post("/api/v1/users/",formData)
            .then(response => {
                console.log(response)
                this.$router.push("/login")
            })
            .catch(error => {
                if (error.response) {
                    for (const property in error.response.data){
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                    }
                    console.log(JSON.stringify(error.response.data))
                }
                else if (error.message){
                    console.log(JSON.stringify(error.message))
                }
                else {
                    console.log(JSON.stringify(error))
                }
            })
        }
    }}}
    
</script>