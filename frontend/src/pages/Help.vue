<template>
  <div>
    <el-card :body-style="{ padding: '0px' }">
      <img src="./../assets/images/stream.png" class="image" />
      <div style="padding: 14px">
        <span>用户操作流程图</span>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "Help"
}
</script>

<style scoped>
.image {
  width: 100%;
}
.el-card {
  display: flex;
  align-items: center;
}
</style>
