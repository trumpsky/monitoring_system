<template>
  <div>
    <el-container>
      <el-aside width="240px">
        <sidebar @menu="change"></sidebar>
      </el-aside>
      <el-container>
        <el-header>
          <selection-node-single v-if="showComponent"></selection-node-single>
        </el-header>
        <el-main>
          <div class="main-information">
            <router-view></router-view>
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
import SelectionNodeSingle from '../component/SelectionNodeSingle.vue';
import ShowFooter from '../component/ShowFooter.vue';
import Sidebar from "../component/Sidebar";
import ClusterLevel from "./ClusterLevel";

export default {
  components: {ClusterLevel, Sidebar, ShowFooter, SelectionNodeSingle,},
  data() {
    return {
      showComponent: false
    }
  },
  methods: {
    change(val){
        this.showComponent = (val == 2)
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
}
</style>
