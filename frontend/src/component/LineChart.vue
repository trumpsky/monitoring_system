<template>
  <div class="about">
    <div ref="chart" style="width: 600px; height: 400px"></div>
  </div>
</template>
  
<script>
export default {
  props: {
    moduleName: String, //配合接口函数
  },
  data() {
    return {
      name: "集群层面",
      indicator: "健康情况",
      isLoading: false,
      data: this.refreshData(),
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
                this.isLoading = !this.isLoading
                console.log(this.isLoading);
              },
            },
          },
        },
        title: {
          left: "center",
          text: this.name + "-" + this.indicator,
        },
        xAxis: {
          type: "category",
          data: this.data.map((d) => d.time), // 将数据对象映射成数组
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
        series: [
          {
            data: this.data.map((d) => d.value),
            type: "line",
            smooth: true, // 是否平滑
            areaStyle: {},
            markPoint: {
              data: [
                { type: "max", name: "最大值" },
                { type: "min", name: "最小值" },
              ],
            },
          },
        ],
      };
    },
  },
  methods: {
    drawLine() {
      let chart = this.$echarts.init(this.$refs.chart);
      chart.setOption(this.option);
    },
    refreshData() {
      return [
        {
          time: "2023/4/12 21:15:00",
          value: Math.random() * 300,
        },
        {
          time: "2023/4/12 22:15:00",
          value: Math.random() * 300,
        },
        {
          time: "2023/4/12 23:15:00",
          value: Math.random() * 300,
        },
        {
          time: "2023/4/12 00:15:00",
          value: Math.random() * 300,
        },
        {
          time: "2023/4/12 01:15:00",
          value: Math.random() * 300,
        },
        {
          time: "2023/4/12 02:15:00",
          value: Math.random() * 300,
        },
        {
          time: "2023/4/12 03:15:00",
          value: Math.random() * 300,
        },
        {
          time: "2023/4/12 04:15:00",
          value: Math.random() * 300,
        },
      ];
    },
    getName() {
      let params = new URLSearchParams();
      params.append("module", moduleName);
      const url = "" + moduleName;
      this.$https.post(url).then((res) => {
        this.name = res.data.name;
        this.indicator = res.data.name;
      });
    },
  },
  mounted() {
    this.drawLine();
  },
  watch: {
    isLoading: function (val) {
      if (val){
        this.data = this.refreshData();
      }
    },
  },
};
</script>
  