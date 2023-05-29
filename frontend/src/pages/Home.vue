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
            v-if="this.showComponent"
          ></selection-cascader>
        </el-header>
        <el-main>
          <el-button
            :type="this.$store.getters.getIsUpdate ? 'success' : 'primary'"
            :icon="
              this.$store.getters.getIsUpdate
                ? 'el-icon-video-pause'
                : 'el-icon-video-play'
            "
            circle
            v-if="this.initialData.length != 0 && this.showComponent"
            @click="clickFunction"
          ></el-button>
          <el-empty description="请点击右上方选择器选择数据集" v-if="this.initialData.length == 0 && this.showComponent"></el-empty>
          <div class="main-information">
            <router-view
              :initialData="initialData"
              @datazoom="dataZoomData"
              :key="initialData"
              @refresh="refreshData"
              @stop="stopData"
              ref="dataShow"
            ></router-view>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import SelectionCascader from "../component/SelectionCascader.vue";
import Sidebar from "../component/Sidebar";
import ClusterLevel from "./ClusterLevel";

export default {
  components: { ClusterLevel, Sidebar, SelectionCascader },
  data() {
    return {
      showComponent: false,
      initialData: [],
      selectPath: [],
    };
  },
  methods: {
    change(val) {
      this.showComponent = val == "2";
    },
    dataZoomData(data) {
      const params = new URLSearchParams();
      params.append("data", JSON.stringify(this.selectPath));
      params.append("start_time", data[0]);
      params.append("end_time", data[1]);
      this.$http.post(this.url, params).then((res) => {
        this.initialData = res.data.result_list;
      });
    },
    uploadTime(data, time) {
      let result = data;
      let endValue = this.$moment(data[1]).valueOf();
      endValue = endValue + time * 1000 * 60;
      endValue = this.$moment(endValue).format("YYYY/MM/DD HH:mm");
      result[1] = endValue;
      return result;
    },
    refreshData(data) {
      let dataCount = data;
      let time = 2;
      dataCount = this.uploadTime(dataCount, time);
      this.dataZoomData(dataCount);
      const timer = setInterval(() => {
        dataCount = this.uploadTime(dataCount, time);
        this.dataZoomData(dataCount);
      }, time * 1000);
      this.$on("clearInterval", () => {
        clearInterval(timer);
      });
    },
    stopData() {
      this.$emit("clearInterval");
    },
    getPostPath() {
      switch (this.$store.getters.getObservedState) {
        case "cluster":
          return "http://localhost:5000/dataShow/getClusterData";
        case "nodeSingle":
          return "http://localhost:5000/dataShow/getNodeSingleData";
        case "nodeMultiple":
          return "http://localhost:5000/dataShow/getNodeMultipleData";
      }
    },
    getChartsData(data) {
      this.selectPath = data;
      const params = new URLSearchParams();
      params.append("data", JSON.stringify(data));
      params.append("start_time", "2023/04/12 20:00");
      params.append("end_time", "2023/04/12 22:37");
      this.$http.post(this.url, params).then((res) => {
        this.initialData = res.data.result_list;
      });
    },
    clickFunction() {
      this.$refs.dataShow.clickFunction();
    },
  },
  watch: {
    "$store.getters.getObservedState": {
      deep: true,
      handler() {
        this.url = this.getPostPath();
        this.initialData = [];
      },
    },
  },
  mounted() {
    this.url = this.getPostPath();
    this.change(window.location.href.slice(-3,-2));
  },
};
</script>

<style scoped>
.el-header {
  background-color: #3f5b94;
  color: #fff;
  line-height: 7.5vh;
  display: flex;
  justify-content: flex-end;
}

.el-aside {
  background-color: #3f5b94;
  color: #333;
}
li.el-submenu {
  width: 240px;
}
.el-main {
  background-color: #fff;
  color: #333;
  height: 92.5vh;
  display: flex;
  justify-content: center;
}
.el-button {
  position: fixed;
  right: 3%;
  top: 15%;
}
.main-information {
  overflow: auto;
}
</style>
