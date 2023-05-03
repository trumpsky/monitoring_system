<template>
  <div>
    <single-chart :compare="selectData" :key="selectData" :title="title"></single-chart>
    <el-dropdown @command="handleCommand">
      <span class="el-dropdown-link">
        选择比较对象<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item v-for="(item, index) in top" :command="item" v-text="item"></el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
import SingleChart from '../component/SingleChart.vue'
export default {
  components: { SingleChart },
  name: "AnomalyComparison",
  data(){
    return{
      top: [7,2,9,14,1],
      selectData: 0,
      title: '弗雷歇距离'
    }
  },
  methods: {
    handleCommand(command)  {
      this.selectData = parseInt(command)
    }
  }
}
</script>

<style scoped>
.el-dropdown{
  position: fixed;
  right: 5%;
  top: 25%;
}
</style>
