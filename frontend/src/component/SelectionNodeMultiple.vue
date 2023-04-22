<template>
    <div class="block">
    <span class="demonstration">请选择您要查看的数据</span>
    <el-cascader
      :options="options"
      :props="{ multiple: true, checkStrictly: true }"
      clearable
    ></el-cascader>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
