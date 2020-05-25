<template>
  <div class="home-page">
    <!-- <el-container class="home-wrapper">
      <el-header class="home-header">
        <home-header></home-header>
      </el-header>

      <el-main>
        <div class="inner-container">
          <router-view/>
        </div>
      </el-main>
    </el-container> -->
    <div class="header-wrapper">
      <home-header></home-header>
    </div>
    <div class="main-cnt">
      <el-scrollbar>
        <div class="inner-container">
          <router-view/>
        </div>
      </el-scrollbar>
    </div>
  </div>
</template>
<script>
import HomeHeader from './components/Header.vue'
export default {
  name: 'Home',
  components:{
    HomeHeader
  },
  methods:{
  }
}
</script>

<style lang="stylus" scoped>
.inner-container
  width: 1020px
  height: 100%
  margin: 0 auto
.main-cnt
  height: 100%
.home-page
  width: 100%
  height: 100%
  overflow: hidden
// .el-main
//   overflow: visible
.header-wrapper
  position: fixed
  z-index: 1500
  width: 100%
  top: 0
  left: 0
.el-scrollbar
  height: calc(100% - 80px)
  margin-top: 80px
.el-scrollbar >>> .el-scrollbar__wrap
  overflow-x: hidden
</style>
