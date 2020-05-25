import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import echarts from 'echarts'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.prototype.$http = axios
Vue.prototype.$echarts = echarts
Vue.use(ElementUI)
Vue.config.productionTip = false
//返回顶部
router.afterEach((to,from,next) => {
  window.scrollTo(0,0);
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
