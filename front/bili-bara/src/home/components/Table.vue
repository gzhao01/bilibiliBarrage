<template>
  <div class="table-wrapper">
    <div class="text-row">
        <table-input></table-input>
        <table-text></table-text>
    </div>
    <el-card shadow="hover" class="table-card">
      <density-count></density-count>
    </el-card>
    <el-card shadow="hover" class="table-card">
      <word-count></word-count>
    </el-card>
    <el-card shadow="hover" class="table-card">
      <word-cloud></word-cloud>
    </el-card>
  </div>
</template>
<script>
import DensityCount from './tableComponents/densityCount.vue'
import WordCount from './tableComponents/wordCount.vue'
import WordCloud from './tableComponents/wordCloud.vue'
import TableInput from './tableComponents/TableInput.vue'
import TableText from './tableComponents/TableText.vue'
export default {
  name: 'Table',
  components: {
    DensityCount,
    WordCount,
    WordCloud,
    TableInput,
    TableText
  },
  created() {
    //session sotrage 默认值
      if(!sessionStorage.store_bv){
        sessionStorage.store_bv = "BV1zC4y1s7RW";
      }
      if(!sessionStorage.store_p_num){
        sessionStorage.store_p_num = 1;
      }
  }
}
</script>

<style lang="stylus" scoped>
.text-row
  display: flex
.table-card
  width: 1020px
  margin-top: 20px
</style>
