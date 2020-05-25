<template>
  <div>
    <div id="densityCount"></div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
  name: 'DensityCount',
  data(){
    return{
      x_data: [],
      y_data: []
    }
  },
  computed: {
    ...mapState(['store_bv', 'store_p_num'])
  },
  methods:{
    densityCount(){
          // based on prepared DOM, initialize echarts instance
            var myChart = this.$echarts.init(document.getElementById('densityCount'));
            myChart.showLoading(); 
            // specify chart configuration item and data
            var option = {
                title: {
                    text: '弹幕密度统计'
                },
                tooltip: {},
                legend: {
                    data:['时间']
                },
                xAxis: {
                    data: ['a']
                },
                yAxis: {},
                series: [{
                    name: '时间',
                    type: 'line',
                    data: [1]
                }]
            };
            myChart.setOption(option);
            // get density of barriage data
            this.$http({
            method : "get",
    //       async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
            url : "/api/getdensity",    //请求发送到Servlet处
            params: {
              // bv: this.store_bv,
              // p_num: this.store_p_num
              bv: sessionStorage.store_bv,
              p_num: sessionStorage.store_p_num
            }
   //       data : {},
            }).then(result => {
              result = result.data;
              var count_keys = [];
              var count_vals = [];
              for(var val in result){
                var time = this.MillisecondToDate(val)
                count_keys.push(time);
                count_vals.push(result[val]);
              }
//           	alert(result["data"]);
                myChart.hideLoading();    //隐藏加载动画
                myChart.setOption({        //加载数据图表
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
                        name: '时间',
                        type: 'line',
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
                });
            }).catch(err => {
                myChart.hideLoading(); 
                alert("get density data fail")
                console.log(err)
            })
    },
    MillisecondToDate(time){
        if (null != time && "" != time) {
        if (time > 60 && time < 60 * 60) {
            time = parseInt(time / 60.0) + "分钟" + parseInt((parseFloat(time / 60.0) -
                parseInt(time / 60.0)) * 60) + "秒";
        }
        else if (time >= 60 * 60 && time < 60 * 60 * 24) {
            time = parseInt(time / 3600.0) + "小时" + parseInt((parseFloat(time / 3600.0) -
                parseInt(time / 3600.0)) * 60) + "分钟" +
                parseInt((parseFloat((parseFloat(time / 3600.0) - parseInt(time / 3600.0)) * 60) -
                parseInt((parseFloat(time / 3600.0) - parseInt(time / 3600.0)) * 60)) * 60) + "秒";
        }
        else {
            time = parseInt(time) + "秒";
        }
      }
      return time;
    }
  },
  mounted(){
    this.densityCount()
  },
  // created(){
  //   this.$http({
  //     method: 'get',
  //     url: 'api/getDensity'
  //   }).then(function(res){
  //       for(var val in res){
  //         var time = MillisecondToDate(val)
  //         this.x_data.push(time);
  //         this.y_data.push(res[val]);
  //       }
  //   }).catch(err => {
  //     alert("弹幕密度请求失败")
  //     console.log(err)
  //     myChart.hideLoading();
  //   })
  // }
}
</script>

<style lang="stylus" scoped>
#densityCount
  width: 1000px
  height:400px
</style>