<template>
  <div class="about">
    <div ref="chart" style="width: 1200px; height: 400px"></div>
  </div>
</template>

<script>
export default {
  props: ["moduleName", "propsData"],
  data() {
    return {
      name: this.$store.getters.getObservedState,
      isLoading: false,
      time: [],
      series: [],
      loadData: [],
      nameList: [],
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
            dataZoom:{
              title:{
                zoom: "",
                back: ""
              },
              iconStyle: {
                opacity: 0
              }
            },
            dataView: {
              readOnly: true,
              buttonColor: "rgb(30,128,255)",
            },
            myTool1: {
              show: true,
              title: "实时刷新",
              icon: "path://M 50 250 Q 100 150 150 250",
              onclick: function () {
                this.isLoading = !this.isLoading;
              },
            },
          },
        },
        title: {
          left: "center",
          text: this.name + "-" + this.moduleName.slice(14, ),
        },
        xAxis: {
          type: "category",
          data: this.time,
        },
        yAxis: {
          type: "value",
          scale:true
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
        dataZoomSelectActive: true
      })
    }
  },
  mounted() {
    this.refreshData();
    this.drawLine();
  },
  watch: {
    isLoading: function (val) {
      if (val) {
        this.data = this.refreshData();
      }
    },
  },
};
</script>
