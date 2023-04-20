<template>
    <div>
        <line-chart :moduleName="firstChart"></line-chart>
        <line-chart :moduleName="secondChart"></line-chart>
    </div>
</template>

<script>
import LineChart from '../component/LineChart.vue'
export default {
  components: { LineChart },
  data(){
    return{
        firstChart: "test",
        secondChart: "test2"
    }
  },
  methods:{
    connectChart(){
        let firstChart = this.$echarts.init(this.$children[0].$refs.chart)
        let secondChart = this.$echarts.init(this.$children[1].$refs.chart)
        this.$echarts.connect([firstChart,secondChart])
    }
  },
  mounted() {
    this.connectChart();
  },
}
</script>