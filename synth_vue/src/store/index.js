import { createStore } from 'vuex'

export default createStore({
  state: {
    user:{
      username:'',
    },
    isAuthenicated:false,
    token:'',
  },
  getters: {
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenicated = true
      }
      else{
        state.token = ''
        state.isAuthenicated = false
      }
    },
    setToken(state,token){
      state.token = token
      state.isAuthenicated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenicated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
