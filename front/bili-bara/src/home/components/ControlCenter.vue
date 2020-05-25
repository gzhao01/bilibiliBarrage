<template>
  <div>
    <el-row v-for="(index, item) of list" :key="index">
      <el-col :span="24">
        <el-card shadow="hover" class="info-card">
          {{item}}
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<script>
export default {
  name: 'ControlCenter',
  data(){
    return{
      list: [1]
    }
  }
}
</script>

<style lang="stylus" scoped>
.info-card
  margin-bottom: 40px
</style>
