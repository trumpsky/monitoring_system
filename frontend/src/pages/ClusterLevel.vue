<template>
  <div>
    <line-chart v-for="(item, index) in initialData" :moduleName="item.indicator" :key="index" :propsData="item"></line-chart>
  </div>
</template>

<script>
import LineChart from "../component/LineChart.vue";

export default {
  components: { LineChart },
  props: ["initialData"],
  data() {
    return {
    }
  },
  methods: {
    connectChart() {
      let chartArray = []
      for (let i = 0; i < this.$children.length; i++) {
        const chart = this.$echarts.init(this.$children[i].$refs.chart)
        chartArray.push(chart)
      }
      this.$echarts.connect(chartArray)
    }
  },
  mounted() {
    this.connectChart();
  }
}
</script>
