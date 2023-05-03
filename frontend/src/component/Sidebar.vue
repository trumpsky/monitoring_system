<template>
  <div>
    <el-menu :default-active="$route.path"
             class="el-menu-vertical-demo"
             background-color="#3f5b94"
             text-color="#FFFFFF"
             @select="handleSelect"
             router>
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-info"></i>
          <span>系统简介</span>
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
          <span>数据监控</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/menu/2-1" @click="toCluster">集群模式</el-menu-item>
          <el-menu-item index="/menu/2-2" @click="toNodeSingle">节点单模式</el-menu-item>
          <el-menu-item index="/menu/2-3" @click="toNodeMultiple">节点多模式</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="4">
        <template slot="title">
          <i class="el-icon-setting"></i>
          <span>异常匹配</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/menu/4-1" @click="toDTW">DTW算法</el-menu-item>
          <el-menu-item index="/menu/4-2" @click="toFrechet">Frechet算法</el-menu-item>
          <el-menu-item index="/menu/4-3" @click="toHausdorff">Hausdorff算法</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-goods"></i>
          <span>商店</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/menu/3-1">会员</el-menu-item>
          <el-menu-item index="/menu/3-2">超级会员</el-menu-item>
          <el-menu-item index="/menu/3-3">豪华会员</el-menu-item>
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
    handleSelect(key,keyPath) {
      this.$emit("menu",key[6])
    },
    toCluster(){
      this.$store.commit("updateObservedState", "cluster")
    },
    toNodeSingle(){
      this.$store.commit("updateObservedState", "nodeSingle")
    },
    toNodeMultiple(){
      this.$store.commit("updateObservedState", "nodeMultiple")
    },
    toDTW(){
      this.$store.commit("updateAlgorithm", "DTW")
    },
    toFrechet(){
      this.$store.commit("updateAlgorithm", "Frechet")
    },
    toHausdorff(){
      this.$store.commit("updateAlgorithm", "Hausdorff")
    }
  },
}
</script>
<style scoped>
.el-menu-item.is-active {
  color: #fff !important;
  background: rgb(50,73,118) !important;
}
</style>
