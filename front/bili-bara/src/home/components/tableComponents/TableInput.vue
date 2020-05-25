<template>
  <div class="input-wrapper">
    <el-card class="box-card" shadow="hover">
      <el-form
      ref="form"
      :model="form"
      label-width="80px"
      >
        <el-form-item label="BV号">
          <el-input v-model="form.bv" placeholder="BV1zC4y1s7RW"></el-input>
        </el-form-item>
        <el-form-item label="分p号">
          <el-input v-model="form.p_num" placeholder="1"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">确定</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
export default {
  inject:['reload'], 
  name: "TableInput",
  data(){
    return{
      form: {
        bv: "",
        p_num: ''
      }
    }
  },
  methods:{
    onSubmit(){
      if(!sessionStorage.store_bv){
        sessionStorage.store_bv = "BV1zC4y1s7RW";
      }
      if(!sessionStorage.store_p_num){
        sessionStorage.store_p_num = 1;
      }
      this.$store.dispatch('change_bv', this.form.bv);
      this.$store.dispatch('change_p_num',this.form.p_num);
      this.reload();
    }
  }
}
</script>

<style lang="stylus" scoped>
.input-wrapper >>> .box-card
  width: 600px
</style>

