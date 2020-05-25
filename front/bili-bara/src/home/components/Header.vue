<template>
  <div class="home-header">
      <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      router
      >
        <el-menu-item class="header-title">BiliBara</el-menu-item>
        <el-menu-item index="1" route="/controlCenter">控制中心</el-menu-item>
        <el-menu-item index="2" route="/table">表格界面</el-menu-item>
      </el-menu>
  </div>
</template>

<script>
export default{
  name: "Header",
  data() {
    return{
      activeIndex: '1',
      activeIndex2: '2'
    }
  },
  methods:{
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style lang="stylus" scoped>
  .header-title
    font-size: 20px
</style>