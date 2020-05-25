export const densityOption = {
  xAxis: {
      //need be changed
      data: []
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
      //need be changed
      data: [],
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
}