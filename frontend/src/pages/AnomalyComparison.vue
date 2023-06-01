<template>
  <div>
    <single-chart :compare="selectData" :key="selectData"></single-chart>
    <el-dropdown @command="handleCommand" v-if="selected">
      <span class="el-dropdown-link">
        选择比较对象<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item v-for="(item, index) in top" :command="item" v-text="content[index]"></el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <el-input v-model="input" type="number" :max="20" :min="1" placeholder="请输入排名" @blur="getRank" v-else></el-input>
  </div>
</template>

<script>
import SingleChart from "../component/SingleChart.vue";
export default {
  components: { SingleChart },
  name: "AnomalyComparison",
  data() {
    return {
      top: [],
      selectData: this.$store.getters.getAlgorithm,
      content: [],
      input: "",
      selected: false,
    };
  },
  methods: {
    handleCommand(command) {
      this.selectData = parseInt(command);
    },
    getRank() {
      if (this.input >= 1 && this.input <= 20) {
        const params = new URLSearchParams();
        params.append("rank_number", this.input);
        params.append("algorithm", this.$store.getters.getAlgorithm);
        this.$http
          .post("http://localhost:5000/comparison/getRank", params)
          .then((res) => {
            for (let i = 0; i < res.data.length; i++) {
              this.top.push(res.data[i][0]);
              this.content.push(
                res.data[i][0] + "-" + res.data[i][1].toFixed(2)
              );
            }
            this.selected = true;
          });
      }
      else {
        this.selected = false;
        this.$message.error("请输入1-20之间的数字");
      }
    },
  },
  mounted() {
    this.selected = false;
    this.input = ''
  },
  watch: {
    "$store.getters.getAlgorithm": {
      deep: true,
      handler() {
          this.top = [],
          this.content = [],
          this.selectData = this.$store.getters.getAlgorithm,
          this.selected = false;
          this.input = "";
      },
    },
  },
};
</script>

<style scoped>
.el-dropdown {
  position: fixed;
  right: 5%;
  top: 25%;
}

.el-input {
  position: fixed;
  right: 5%;
  top: 25%;
  width: 10%;
}
</style>
