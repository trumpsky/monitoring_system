<template>
  <div>
    <selection-cluster></selection-cluster>
    <selection-node-single></selection-node-single>
    <selection-node-multiple></selection-node-multiple>
    <line-chart v-for="(item, index) in items" :moduleName="item.message" :key="index"></line-chart>
  </div>
</template>

<script>
import LineChart from "../component/LineChart.vue";
import SelectionCluster from "../component/SelectionCluster.vue";
import SelectionNodeSingle from "../component/SelectionNodeSingle.vue";
import SelectionNodeMultiple from "../component/SelectionNodeMultiple.vue";
export default {
  components: { LineChart, SelectionCluster, SelectionNodeSingle, SelectionNodeMultiple },
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
  }
}
</script>
