<template>
  <div>
    <el-container>
      <el-aside width="200px">
        <sidebar></sidebar>
      </el-aside>
      <el-container>
        <el-header>Header</el-header>
        <el-main>
          <div class="charts">
            <clutter-level></clutter-level>
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
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  /*line-height: 700px;*/
  width: 15%;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
}
</style>
