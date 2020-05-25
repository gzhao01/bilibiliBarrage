<template>
  <div class="table-text-container">
    <el-card class="text-card" shadow="hover">
      <p>1. 如果报错请将页面刷新几遍</p>
      <p>2. 默认爬取
        <el-link
        type="primary"
        href="https://www.bilibili.com/video/BV1zC4y1s7RW?p=2"
        target="_blank"
        >
        BV1zC4y1s7RW
        </el-link>的内容
      </p>
      <p>3. 无分p的请在分p号栏内填<span class="emphasis">1</span></p>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "TableText"  
}
</script>

<style lang="stylus" scoped>
.table-text-container >>> .text-card
  width: 420px
  height: 226px
.text-card >>> .emphasis
  color: #66b1ff
</style>