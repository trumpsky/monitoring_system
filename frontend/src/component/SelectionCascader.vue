<template>
  <div class="block">
    <el-cascader
      ref="cascader"
      :options="this.projectAllList"
      :props="this.props"
      :show-all-levels="false"
      clearable
      collapse-tags
      placeholder="请选择集群后点击右侧按钮查询"
      style="width: 350px"
    ></el-cascader>
    <el-button icon="el-icon-search" circle @click="getItems"></el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      projectAllList: [{}],
      props: {
        value: "value",
        label: "label",
        multiple: true,
        lazy: true,
        lazyLoad: (node, resolve) => {
          this.getChildrenContent(node, resolve);
        },
      },
    };
  },
  methods: {
    getFirstLevel() {
      const params = new URLSearchParams();
      this.$http
        .post("http://localhost:5000/dataGet/clusterName", params)
        .then((res) => {
          this.projectAllList = res.data.cluster;
        });
    },
    getChildrenContent(data, resolve) {
      const params = new URLSearchParams();
      params.append("mode", this.$store.getters.getObservedState);
      switch (data.level) {
        case 1:
          this.$http
            .post("http://localhost:5000/dataGet/getIndicatorName", params)
            .then((res) => {
              const nodes = res.data.indicators.map((item) => ({
                label: item.label,
                value: item.value,
                leaf: this.$store.getters.getObservedState === "cluster",
              }));
              resolve(nodes);
            });
          break;
        case 2:
          if (this.$store.getters.getObservedState === "cluster") {
            let end;
            resolve(end);
            return;
          }
          params.append("cluster_name", data.pathLabels[0]);
          this.$http
            .post("http://localhost:5000/dataGet/getNodeIP", params)
            .then((res) => {
              const nodes = res.data.node_ip.map((item) => ({
                label: item.label,
                value: item.value,
              }));
              resolve(nodes);
            });
          break;
        case 3:
          params.append("cluster_name", data.pathLabels[0]);
          params.append("node_ip", data.pathLabels[2]);
          this.$http
            .post("http://localhost:5000/dataGet/getNodeName", params)
            .then((res) => {
              const nodes = res.data.node_name.map((item) => ({
                label: item.label,
                value: item.value,
                leaf: this.$store.getters.getObservedState === "nodeSingle",
              }));
              resolve(nodes);
            });
          break;
        case 4:
          if (this.$store.getters.getObservedState === "nodeSingle") {
            let end;
            resolve(end);
            return;
          }
          params.append("cluster_name", data.pathLabels[0]);
          params.append("node_ip", data.pathLabels[2]);
          params.append("node_name", data.pathLabels[3]);
          this.$http
            .post("http://localhost:5000/dataGet/getDiskName", params)
            .then((res) => {
              const nodes = res.data.disk_name.map((item) => ({
                label: item.label,
                value: item.value,
                leaf: this.$store.getters.getObservedState === "nodeMultiple",
              }));
              resolve(nodes);
            });
          break;
        case 5:
          let end;
          resolve(end);
          return;
      }
    },
    getItems() {
      let result = [];
      const pathSet = this.$refs.cascader.getCheckedNodes();
      for (let item in pathSet) {
        if (
          pathSet[item].pathLabels.length ==
          pathSet[pathSet.length - 1].pathLabels.length
        ) {
          result.push(pathSet[item].pathLabels);
        }
      }
      this.$emit("submit", result);
    },
  },
  mounted() {
    this.getFirstLevel();
  },
};
</script>

<style></style>
