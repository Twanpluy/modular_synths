<template>
<div class= "wrapper">
  <nav class="bg-white shadow-lg">
			<div class="max-w-6xl mx-auto px-4">
				<div class="flex justify-between">
					<div class="flex space-x-7">
						<!-- Primary Navbar items -->
						<div class="hidden md:flex items-center space-x-1">
              <router-link to="/home" class="py-4 px-2 text-green-500 font-semibold hover:text-green-500 hover:border-b-4 hover:border-green-500">Home</router-link>
							<router-link to="/about" class="py-4 px-2 text-green-500 font-semibold hover:text-green-500 hover:border-b-4 hover:border-green-500">About</router-link>
							<router-link to="/synth_list" class="py-4 px-2 text-green-500 font-semibold hover:text-green-500 hover:border-b-4 hover:border-green-500">Modular Synths</router-link>

            </div>
					</div>
					<!-- Secondary Navbar items -->
					<div class="hidden md:flex items-center space-x-3 ">
						<a href="" class="py-2 px-2 font-medium text-gray-500 rounded hover:bg-green-500 hover:text-white transition duration-300">Log In</a>
						<a href="" class="py-2 px-2 font-medium text-white bg-green-500 rounded hover:bg-green-400 transition duration-300">Sign Up</a>
					</div>
					
				</div>
			</div>
  </nav>

<router-view/>
</div>
</template>
