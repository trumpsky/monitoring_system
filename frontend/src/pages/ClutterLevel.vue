<template>
  <div>
    <line-chart v-for="(item, index) in items" :moduleName="item.message" :key="index"></line-chart>
  </div>
</template>

<script>
import LineChart from '../component/LineChart.vue'
export default {
  components: { LineChart },
  data() {
    return {
      items: [
        { message: '活跃分片总数' },
        { message: '集群健康状态' },
        { message: '集群健康节点' }
      ]
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
  },
}
</script>