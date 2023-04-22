<template>
  <div>
    <el-menu :default-active="$route.path"
             class="el-menu-vertical-demo"
             background-color="#3f5b94"
             text-color="#FFFFFF"
             active-text-color="#000000"
             @open="handleOpen"
             @close="handleClose"
             router>
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>监控系统</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/menu/1-1">系统信息</el-menu-item>
          <el-menu-item index="/menu/1-2">系统指南</el-menu-item>
          <el-menu-item index="/menu/1-3">开发团队</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-setting"></i>
          <span>数据模式</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/menu/2-1">集群数据</el-menu-item>
          <el-menu-item index="/menu/2-2">节点单指标</el-menu-item>
          <el-menu-item index="/menu/2-3">节点多指标</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      isCollapse: true
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>
<style scoped>
</style>
