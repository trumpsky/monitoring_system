<template>
  <div class="about">
    <div ref="chart" style="width: 600px; height: 400px"></div>
  </div>
</template>
  
<script>
export default {
  props: ["moduleName", "propsData"],
  data() {
    return {
      name: this.$store.getters.getObservedState,
      isLoading: false,
      data: [],
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
          text: this.name + "-" + this.moduleName.slice(15, -1),
        },
        xAxis: {
          type: "category",
          data: this.data.map((d) =>
            this.$moment(d.time * 1000).format("YYYY-MM-DD HH:mm:ss")
          ), // 将数据对象映射成数组
        },
        yAxis: {
          type: "value",
        },
        dataZoom: [
          {
            type: "inside",
            start: 0,
            end: 100,
          },
          {
            start: 0,
            end: 20,
          },
        ],
        series: this.series,
      };
    },
  },
  methods: {
    drawLine() {
      let chart = this.$echarts.init(this.$refs.chart);
      chart.setOption(this.option);
    },
    refreshData() {
      const keys = Object.keys(this.propsData);
      for (let item in keys) {
        if (typeof this.propsData[keys[item]] != "string") {
          this.loadData.push(this.propsData[keys[item]]);
          this.series.push({
            name: keys[item],
            data: this.propsData[keys[item]].map((d) => d.value),
            type: "line",
            smooth: true,
          });
        }
      }
      console.log(this.series);
      this.data = this.propsData[keys[1]];
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
  