<template>
  <div class="about">
    <div ref="chart" style="width: 800px; height: 400px"></div>
  </div>
</template>
<script>
export default {
  props: ["moduleName", "propsData"],
  data() {
    return {
      name: this.$store.getters.getObservedState,
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
            dataZoom: {
              title: {
                zoom: "",
                back: "",
              },
              iconStyle: {
                opacity: 0,
              },
            },
            dataView: {
              readOnly: true,
              buttonColor: "rgb(30,128,255)",
            }
          },
        },
        title: {
          left: "center",
          text: this.name + "-" + this.moduleName.slice(14),
        },
        xAxis: {
          type: "category",
          data: this.time,
        },
        yAxis: {
          type: "value",
          scale: true,
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
      chart.on("datazoom", (params) => {
        const startValue = this.time[params.batch[0].startValue];
        const endValue = this.time[params.batch[0].endValue];
        let time = [];
        time.push(startValue);
        time.push(endValue);
        this.$emit("datazoom", time);
      });
    },
    refreshData() {
      const keys = Object.keys(this.propsData);
      for (let item in keys) {
        if (typeof this.propsData[keys[item]] != "string") {
          this.loadData.push(this.propsData[keys[item]]);
          this.time = this.propsData[keys[item]].map((d) =>
            this.$moment(d.time * 1000).format("YYYY/MM/DD HH:mm")
          );
          this.series.push({
            name: keys[item],
            data: this.propsData[keys[item]].map((d) => d.value),
            type: "line",
            smooth: true,
          });
        }
      }
    },
    clickFunction() {
      if(this.$store.getters.getIsUpdate){
        return;
      }
      this.$store.commit("updateIsUpdate", true)
      let time = []
      time.push(this.time[0])
      time.push(this.time.slice(-1)[0])
      this.$emit("refresh", time);
    },
    stopFunction() {
      if(!this.$store.getters.getIsUpdate){
        return;
      }
      this.$store.commit("updateIsUpdate", false)
      this.$emit("stop")
    }
  },
  mounted() {
    this.refreshData();
    this.drawLine();
  },
};
</script>
