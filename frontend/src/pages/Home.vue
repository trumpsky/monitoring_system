<template>
    <div>
        <el-container>
            <el-aside width="200px">
              <sidebar></sidebar>
            </el-aside>
            <el-container>
                <el-header>Header</el-header>
                <el-main>
                    <line-chart></line-chart>
                </el-main>
                <el-footer>Footer</el-footer>
            </el-container>
        </el-container>
    </div>
</template>

<script>
import LineChart from '../component/LineChart.vue'
import Sidebar from "../component/Sidebar";
export default {
  components: {Sidebar, LineChart },
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

<style scoped>
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
    width: 15%;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 500px;
  }
</style>
