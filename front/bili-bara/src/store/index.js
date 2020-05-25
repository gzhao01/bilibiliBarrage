import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    store_bv: "BV1zC4y1s7RW",
    store_p_num: 1
  },
  mutations: {
    change_bv(state, bv){
      state.store_bv = bv;
      localStorage.store_bv = bv;
      sessionStorage.store_bv = bv;
      console.log(sessionStorage.store_bv)
    },
    change_p_num(state, p){
      state.store_p_num = p;
      localStorage.store_p_num = p;
      sessionStorage.store_p_num = p;
      console.log(sessionStorage.store_p_num)
    }
  },
  actions: {
    change_bv(ctx, bv){
      ctx.commit("change_bv",bv);
    },
    change_p_num(ctx, p){
      ctx.commit("change_p_num",p)
    }
  },
  modules: {
  }
})
