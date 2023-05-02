<template>
  <div>
    <el-container>
      <el-aside width="240px">
        <sidebar @menu="change"></sidebar>
      </el-aside>
      <el-container>
        <el-header>
          <selection-cascader
            :key="this.$store.getters.getObservedState"
            @submit="getChartsData"
          ></selection-cascader>
        </el-header>
        <el-main>
          <div class="main-information">
            <router-view :initialData="initialData"></router-view>
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
import SelectionCascader from "../component/SelectionCascader.vue";
import ShowFooter from "../component/ShowFooter.vue";
import Sidebar from "../component/Sidebar";
import ClusterLevel from "./ClusterLevel";

export default {
  components: { ClusterLevel, Sidebar, ShowFooter, SelectionCascader },
  data() {
    return {
      showComponent: false,
      initialData: [],
    };
  },
  methods: {
    change(val) {
      this.showComponent = val == 2;
    },
    getChartsData(data) {
      console.log(data);
      const params = new URLSearchParams();
      params.append("data",JSON.stringify(data))
      params.append("start_time","1970/1/1 00:00")
      params.append("end_time","2023/05/01 22.37")
      this.$http
        .post("http://localhost:5000/dataShow/getClusterData", params)
        .then((res) => {
          console.log(res.data)
        });
      // this.initialData = [
      //   {
      //     indicator: "'elasticsearch_cluster_health_active_shards'",
      //     "master-vm-01": [
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //     ],
      //     "master-vm-02": [
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //       {
      //         time: 1681292087,
      //         value: 2038520.0,
      //       },
      //     ],
      //   },
      // ];
    },
  },
  mounted() {},
};
</script>

<style scoped>
.el-header {
  background-color: #3f5b94;
  color: #fff;
  line-height: 60px;
  display: flex;
  justify-content: flex-end;
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
  background-color: #e9eef3;
  color: #333;
  height: 680px;
}

.main-information {
  overflow: auto;
}
</style>
