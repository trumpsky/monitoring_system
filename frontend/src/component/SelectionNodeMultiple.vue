<template>
  <div class="block">
    <span class="demonstration">请选择您要查看的数据</span>
    <el-cascader :options="this.projectAllList" :props="this.props" :show-all-levels="false" clearable
      collapse-tags></el-cascader>
  </div>
</template>

<script>

export default {
  data() {
    return {
      projectAllList: [{

      }],
      props: {
        value: 'value',
        label: 'label',
        multiple: true,
        lazy: true,
        lazyLoad: (node, resolve) => {
          this.getChildrenContent(node, resolve);
        }
      }
    };
  },
  methods: {
    getFirstLevel() {
      const params = new URLSearchParams();
      this.$http.post('http://localhost:5000/dataShow/clusterName', params).then(res => {
        this.projectAllList = res.data.cluster;
        console.log(this.projectAllList);
      })
    },
    getChildrenContent(data, resolve) {
      console.log(data)
      const params = new URLSearchParams();
      switch (data.level) {
        case 1:
          this.$http.post('http://localhost:5000/dataShow/indicatorName', params).then(res => {
            console.log(res.data)
            const nodes = res.data.indicators.map(item => ({
              label: item.label,
              value: item.value,
              leaf: true,
            }));
            // 通过调用resolve将子节点数据返回，通知组件数据加载完成
            resolve(nodes);
          })
          break;
        case 2:
          let end;
          resolve(end);
          return;
      }
    },
  },
  mounted() {
    this.getFirstLevel()
  }
};
</script>

<style></style>
