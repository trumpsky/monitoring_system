<template>
  <div>
    <line-chart
      v-for="(item, index) in initialData"
      :moduleName="item.indicator"
      :key="index"
      :propsData="item"
      @datazoom="pushTime"
      @refresh="refreshData"
      @stop="stopData"
      ref="chart"
    ></line-chart>
  </div>
</template>

<script>
import LineChart from "../component/LineChart.vue";

export default {
  components: { LineChart },
  props: ["initialData"],
  data() {
    return {};
  },
  methods: {
    connectChart() {
      let chartArray = [];
      for (const element of this.$children) {
        const chart = this.$echarts.init(element.$refs.chart);
        chartArray.push(chart);
      }
      this.$echarts.connect(chartArray);
    },
    pushTime(data) {
      this.$emit("datazoom", data);
    },
    refreshData(data) {
      this.$emit("refresh", data);
    },
    stopData() {
      this.$emit("stop");
    },
    clickFunction() {
      if (this.$store.getters.getIsUpdate) {
        this.$refs.chart[0].stopFunction();
      } else {
        this.$refs.chart[0].clickFunction();
      }
    },
  },
  mounted() {
    this.connectChart();
  },
};
</script>
