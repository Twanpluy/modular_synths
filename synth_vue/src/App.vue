<template>
	<div id="wrapper">
		<nav class="bg-gray-900 shadow-lg">
			<div class="max-w-6xl mx-auto px-4">
				<div>
					<template v-if="$store.state.isAuthenticated">
						<div class="flex space-x-7">
                    	<!-- Primary Navbar items -->
                    		<div class="hidden md:flex items-center space-x-1">
                          		<router-link to="/home" class="py-4 px-2 text-green-500 font-semibold hover:text-green-500 hover:border-b-4 hover:border-green-500">Home</router-link>
                        		<router-link to="/about" class="py-4 px-2 text-green-500 font-semibold hover:text-green-500 hover:border-b-4 hover:border-green-500">About</router-link>
								<router-link to="/synth_list" class="py-4 px-2 text-green-500 font-semibold hover:text-green-500 hover:border-b-4 hover:border-green-500">Modular Synths</router-link>
        					</div>
								<button @click="logout()" class="inline-block p-3 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded-full shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out mx-1">Log out</button>
		
						</div>	
					</template>
					<!-- Items when not authenicated -->
					<template v-if="!$store.state.isAuthenticated">
						<div class="flex space-x-7">
							<div class="hidden md:flex items-center space-x-3 ">
								<router-link to="/login" class="py-4 px-2 text-green-500 font-semibold hover:text-green-500 hover:border-b-4 hover:border-green-500">LogIn</router-link>
                        		<router-link to="/signup" class="py-4 px-2 text-green-500 font-semibold hover:text-green-500 hover:border-b-4 hover:border-green-500">SignUp</router-link>

						</div>
				</div>
					</template>
				</div>
			</div>


		</nav>

	<section class="section">
      <router-view/>
    </section>

</div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
 
    }
  },
  beforeCreate() {
      this.$store.commit('initializeStore')
      const token = this.$store.state.token
	  const test = this.$store.state.isAuthenticated
	  console.log(token)
	  console.log(test)
      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
	methods:{
	logout()
	{
		axios.post("/api/v1/token/logout/")
		.then(response => {
			axios.defaults.headers.common['Authorization'] = ""

			localStorage.removeItem('username')
			localStorage.removeItem('userid')
			localStorage.removeItem('token')

			this.$store.commit('removeToken')

			this.$router.push('/login')
		})
		.catch(error => {
			if(error.response){
				console.log(JSON.stringify(error.response.data))	
			} else if (error.message){
				console.log(error.message)
			} else {
				console.log(JSON.stringify(error))
			}
			}
		)

	}
  }
}

</script>
