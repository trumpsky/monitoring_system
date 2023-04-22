<template>
  <div>
    <el-container>
      <el-aside width="240px">
        <sidebar></sidebar>
      </el-aside>
      <el-container>
        <el-header>Header</el-header>
        <el-main>
          <div class="main-information">
            <router-view></router-view>
          </div>
        </el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Sidebar from "../component/Sidebar";
import ClutterLevel from "./ClutterLevel";

export default {
  components: {ClutterLevel, Sidebar},
  data() {
    return {
    }
  },
  methods: {
  },
  mounted() {
  },
}
</script>

<style scoped>
.el-header, .el-footer {
  background-color: #3f5b94;
  color: #333;
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
