<template>
  <div>
    <el-container>
      <el-aside width="240px">
        <sidebar @menu="change"></sidebar>
      </el-aside>
      <el-container>
        <el-header>
          <selection-cascader :key="this.$store.getters.getObservedState" @submit="getChartsData"></selection-cascader>
        </el-header>
        <el-main>
          <div class="main-information">
            <cluster-level ref="cluster"></cluster-level>
            <!-- <router-view></router-view> -->
          </div>
        </el-main>
        <el-footer>
          <show-footer></show-footer>
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import SelectionCascader from '../component/SelectionCascader.vue';
import ShowFooter from '../component/ShowFooter.vue';
import Sidebar from "../component/Sidebar";
import ClusterLevel from "./ClusterLevel";

export default {
  components: { ClusterLevel, Sidebar, ShowFooter,  SelectionCascader, },
  data() {
    return {
      showComponent: false
    }
  },
  methods: {
    change(val) {
      this.showComponent = (val == 2)
    },
    getChartsData(data){
      console.log(data)
      const params = new URLSearchParams();
      params.append("data",JSON.stringify(data))
      params.append("start_time","2023/04/01: 00:00")
      params.append("end_time","2023/04/12 23:25")
      this.$http
        .post("http://localhost:5000/dataShow/getClusterData", params)
        .then((res) => {
          console.log()
        });
    }
  },
  mounted() {
  },
}
</script>

<style scoped>
.el-header {
  background-color: #3f5b94;
  color: #fff;
  line-height: 60px;
  display: flex;
  justify-content: flex-end
}

.el-footer {
  background-color: #3f5b94;
  color: #fff;
  line-height: 60px;
}

.el-aside {
  background-color: #3f5b94;
  color: #333;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  height: 680px;
}

.main-information {
  overflow: auto;
}</style>
