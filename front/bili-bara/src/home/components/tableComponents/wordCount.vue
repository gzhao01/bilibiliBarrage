<template>
  <div>
    <div id="wordCount"></div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
    name: 'WordCount',
    computed: {
      ...mapState(['store_bv','store_p_num'])
    },
    methods:{
      wordCount(){
        //get word count
      var wordCountChart = this.$echarts.init(document.getElementById('wordCount'));
      wordCountChart.showLoading(); 
      var option = {
              title: {
                  text: 'top10弹幕'
              },
              tooltip: {},
              legend: {
                  data:['弹幕']
              },
              xAxis: {
                  data: ['a']
              },
              yAxis: {},
              series: [{
                  name: '数量',
                  type: 'bar',
                  data: [1]
              }]
          };

          this.$http({
            method : "get",
    //       async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
            url : "/api/getWordCount",
            params: {
              // bv: this.store_bv,
              // p_num: this.store_p_num
              bv: sessionStorage.store_bv,
              p_num: sessionStorage.store_p_num
            }
          }).then(result => {
            result = result.data;
            var count_keys = [];
            var count_vals = [];
            for(var val in result){
              count_keys.push(val);
              count_vals.push(result[val]);
            }
            wordCountChart.hideLoading();    //隐藏加载动画
            wordCountChart.setOption({        //加载数据图表
                title: {
                    text: '分词统计'
                },
                xAxis: {
                    data: count_keys
                },
                yAxis: {},
                toolbox: {                   
                    show: true,                  
                    feature: 
                    {                     
                      dataZoom:
                      {                        
                        realtime: false,                         
                        yAxisIndex: 'none',                      
                      },                    
                      restore: {},                   
                    }            
                  },               
                  dataZoom: 
                  [
                    {type: 'inside'},        //用于添加滚轮缩放
                    {type:'slider' },  //用于添加滑动条缩放，
                  ],            
                series: [{
                    // 根据名字对应到相应的系列
                    name: '数量',
                    type: 'bar',
                    data: count_vals,
                    markPoint : {
                      data : [
                          {type : 'max', name: '最大值'},
                          {type : 'min', name: '最小值'}
                            ]
                      },
                    markLine : {
                        data : [
                            {type : 'average', name: '平均值'}
                        ]
                    },
                }]
              })
        }).catch(err=>{
          alert("get wordcount data fail")
          console.log(err)
        })
      }
    },
    mounted() {
      this.wordCount()
    }
  }
</script>

<style lang="stylus" scoped>
#wordCount
  width: 1000px
  height:400px
</style>