<template>
  <div class="about">
    <div ref="chart" style="width: 800px; height: 400px"></div>
  </div>
</template>
  
  <script>
import { standardData } from "../assets/data";
export default {
  name: "SingleChart",
  props: ['compare'],
  data() {
    return {
      series: [],
      time: [],
    };
  },
  computed: {
    option() {
      return {
        tooltip: {
          // 查看详细数据
          trigger: "axis",
          position: function (pt) {
            return [pt[0], "10%"];
          },
        },
        toolbox: {
          feature: {
            dataZoom: {
              title: {
                zoom: "",
                back: "",
              },
              iconStyle: {
                opacity: 0,
              },
              yAxisIndex: false
            },
            dataView: {
              readOnly: true,
              buttonColor: "rgb(30,128,255)",
            },
          },
        },
        xAxis: {
          type: "category",
          data: this.time,
        },
        yAxis: {
          type: "value",
          scale: true,
        },
        title: {
            left: 'center',
            text: this.$store.getters.getAlgorithm +'算法异常比较-'+ this.compare
        },
        series: this.series,
      };
    },
  },
  methods: {
    drawLine() {
      let chart = this.$echarts.init(this.$refs.chart);
      chart.setOption(this.option);
      chart.dispatchAction({
        type: "takeGlobalCursor",
        key: "dataZoomSelect",
        dataZoomSelectActive: true,
      });
    },
    refreshData() {
        const index = [0]
        if(typeof(this.compare) != "string"){
            index.push(this.compare)
        }
        for(let i=0;i<index.length;i++){
            this.series.push({
                name: index[i],
                data: standardData[index[i]],
                type: 'line',
                smooth: true
            })
        }
      this.time = Array.from({ length: 121 }, (val, i) => this.$moment((i*120+1682232522)*1000).format("YYYY/MM/DD HH:mm"));
    },
  },
  mounted() {
    this.refreshData();
    this.drawLine();
  },
};
</script>
  
  <style scoped>
</style>
  