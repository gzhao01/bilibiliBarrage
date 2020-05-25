<template>
  <div id="wordCloud">wordCloud</div>
</template>

<script>
import {mapState} from 'vuex'
require('echarts-wordcloud');
export default {
  name: 'WordCloud',
  data(){
    return {
      wordCloudData: [],
    }
  },
  computed: {
    ...mapState(['store_bv','store_p_num'])
  },
  methods: {
    wordCloud(){
      var chart = this.$echarts.init(document.getElementById('wordCloud'));
      chart.showLoading(); 
      this.$http({
        method: "get",
        url: "/api/getWordCloud",
        params: {
          // bv: this.store_bv,
          // p_num: this.store_p_num
          bv: sessionStorage.store_bv,
          p_num: sessionStorage.store_p_num
        }
      }).then(res => {
          res = res.data;
          const option = {
          title: {
            text: "词云",
          },
          backgroundColor: "#fff",
          // tooltip: {
          //   pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>"
          // },
          series: [
            {
              type: "wordCloud",
              //用来调整词之间的距离
              gridSize: 10,
              //用来调整字的大小范围
              // Text size range which the value in data will be mapped to.
              // Default to have minimum 12px and maximum 60px size.
              sizeRange: [14, 60],
              // Text rotation range and step in degree. Text will be rotated randomly in range [-90,                                                                             90] by rotationStep 45
              //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
              // rotationRange: [-45, 0, 45, 90],
              // rotationRange: [ 0,90],
              rotationRange: [0, 0],
              //随机生成字体颜色
              // maskImage: maskImage,
              textStyle: {
                normal: {
                  color: function() {
                    return (
                      "rgb(" +
                      Math.round(Math.random() * 255) +
                      ", " +
                      Math.round(Math.random() * 255) +
                      ", " +
                      Math.round(Math.random() * 255) +
                      ")"
                    );
                  }
                }
              },
              //位置相关设置
              // Folllowing left/top/width/height/right/bottom are used for positioning the word cloud
              // Default to be put in the center and has 75% x 80% size.
              left: "center",
              top: "center",
              right: null,
              bottom: null,
              width: "200%",
              height: "200%",
              //data need to be changed
              data: res
            }
          ]
        };
        chart.setOption(option);
        chart.hideLoading(); 
      }).catch(err=>{
        console.log(err)
      })
    }
  },
  mounted() {
    this.wordCloud()
  } 
}
</script>

<style lang="stylus" scoped>
#wordCloud
  width: 1000px
  height:400px
</style>