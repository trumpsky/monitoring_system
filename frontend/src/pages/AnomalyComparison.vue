<template>
  <div>
    <single-chart :compare="selectData" :key="selectData"></single-chart>
    <el-dropdown @command="handleCommand">
      <span class="el-dropdown-link">
        选择比较对象<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item v-for="(item, index) in top" :command="item" v-text="content[index]"></el-dropdown-item>
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
      top: [],
      selectData: this.$store.getters.getAlgorithm,
      content: []
    }
  },
  methods: {
    handleCommand(command)  {
      this.selectData = parseInt(command)
    },
    getRank(){
      const params = new URLSearchParams();
      params.append("algorithm", this.$store.getters.getAlgorithm);
      this.$http.post("http://localhost:5000/comparison/getRank", params).then((res) => {
        for(let i=0;i<res.data.length;i++){
          this.top.push(res.data[i][0])
          this.content.push(res.data[i][0]+ '-' + res.data[i][1].toFixed(2))
        }
      });
    }
  },
  mounted(){
    this.getRank()
  },
  watch: {
    "$store.getters.getAlgorithm": {
      deep: true,
      handler() {
        this.top = [],
        this.content = [],
        this.selectData = this.$store.getters.getAlgorithm,
        this.getRank()
      },
    },
  },
}
</script>

<style scoped>
.el-dropdown{
  position: fixed;
  right: 5%;
  top: 25%;
}
</style>
