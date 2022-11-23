<template>
    <div class="page-login">
  <div class="px-6 h-full text-gray-800">
    <div
      class="flex xl:justify-center lg:justify-between justify-center items-center flex-wrap h-full g-6"
    >

      <div class="xl:ml-20 xl:w-5/12 lg:w-5/12 md:w-8/12 mb-12 md:mb-0">
        <form @submit.prevent="submitForm">
          <div
            class="flex items-center my-4 before:flex-1 before:border-t before:border-gray-300 before:mt-0.5 after:flex-1 after:border-t after:border-gray-300 after:mt-0.5"
          >
          <a class="text-gray-800  text-2xl">Log In</a>
          </div>

          <!-- username input -->
          <div class="mb-6">
            <div class="flex flex-col mb-6">
                <label for="name" class="mb-2 text-sm font-bold text-gray-700">Username</label>
                <input type="text" id="username" placeholder="Enter your username" class="border rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" v-model="username">
            </div>  
          </div>
 

          <!-- Password input -->
          <div class="mb-6">
            <div class="flex flex-col mb-6">
                <label for="password" class="mb-2 text-sm font-bold text-gray-700">Password</label>
                <input type="password" id="password" placeholder="Enter your password" class="border rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-blue-500" v-model="password">
            </div>    
          </div>

          <div class="flex justify-between items-center mb-6">
            <div class="form-group form-check">
              <input
                type="checkbox"
                class="form-check-input appearance-none h-4 w-4 border border-gray-300 rounded-sm bg-white checked:bg-blue-600 
                      checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain
                       float-left mr-2 cursor-pointer"
                id="remember"
              />
              <label class="form-check-label inline-block text-gray-800" for="remember"
                >Remember me</label
              >
            </div>
            <router-link to="/resetpassword" class="text-gray-800">Forgot password</router-link>
          </div>

          <div class="text-center lg:text-left">
            <button
              type="submit"
              class="inline-block px-7 py-3 bg-blue-600 text-white font-medium text-sm leading-snug uppercase rounded shadow-md 
                  hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 
                  active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            >
              Login
            </button>
            <p class="text-sm font-semibold mt-2 pt-1 mb-0">
              Don't have an account?
            <router-link to="/SignUp" class="text-red-600 hover:text-red-700 focus:text-red-700 transition duration-200 ease-in-out">Register</router-link>    
            </p>    
            
            <div class="text-center mt-6" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error" 
                  class="text-red-500 text-sm">
                {{ error }}
            </p>
            </div>

          </div>
        </form>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';


    export default {
        name: "LogIn",
        data() {
            return {
                username: "",
                password: "",
                errors: [], 
            };
        },
        methods: {
          async submitForm(e){
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            const formData = {
              username: this.username,
              password: this.password
            }
            await axios.post('/api/v1/token/login/', formData)
            .then(response => {
              const token = response.data.auth_token

              this.$store.commit('setToken', token)

              axios.defaults.headers.common['Authorization'] = 'Token ' + token

              localStorage.setItem('token', token)

            })
            .catch(error => {
              if(error.response){
                for (const property in error.response.data){
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
                console.log(JSON.stringify(error.response.data))
              }
                else if(error.message){
                  console.log(JSON.stringify.error.message)
                }
                else {
                  console.log(JSON.stringify(error))
                }
            })

            axios.get('/api/v1/users/me/')
            .then(response => {
              this.$store.commit('setUser',{'username': response.data.username, 'id':response.data.id})

              localStorage.setItem('username',response.data.username)
              localStorage.setItem('userid',response.data.id)

              this.$router.push('/home')
            })
            .catch(error => {
              console.log(JSON.stringify(error))
            })
          }
        }
    }
</script>

