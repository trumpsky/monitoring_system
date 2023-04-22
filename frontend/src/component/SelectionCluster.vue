<template>
<div class="block">
  <span class="demonstration">请选择您要查看的数据</span>
  <el-cascader
    :options="options"
    :props="{ multiple: true, checkStrictly: true }"
    clearable></el-cascader>
</div>


</template>

<script>
  export default {
    data() {
      return {
        options: [{
          value: 'cc-cc408-hya',
          label: 'cc-cc408-hya',
          children: [{
            value: 'elasticsearch_cluster_health_active_shards',
            label: 'elasticsearch_cluster_health_active_shards',
          }, {
            value: 'elasticsearch_cluster_health_number_of_nodes',
            label: 'elasticsearch_cluster_health_number_of_nodes',
          },{
            value: 'elasticsearch_cluster_health_status',
            label: 'elasticsearch_cluster_health_status',
          }]
        }, {
          value: 'cc-cc553-interestPrice',
          label: 'cc-cc553-interestPrice',
          children: [{
            value: 'elasticsearch_cluster_health_active_shards',
            label: 'elasticsearch_cluster_health_active_shards',
          }, {
            value: 'elasticsearch_cluster_health_number_of_nodes',
            label: 'elasticsearch_cluster_health_number_of_nodes',
          },{
            value: 'elasticsearch_cluster_health_status',
            label: 'elasticsearch_cluster_health_status',
          }]
        }, ]
      };
    }
  };
</script>
