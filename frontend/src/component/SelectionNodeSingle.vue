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
  data() {
    return {
      options: [
        {
          value: "cc-cc408-hya",
          label: "cc-cc408-hya",
          children: [
            {
              value: "elasticsearch_indices_indexing_index_time_seconds_total",
              label: "elasticsearch_indices_indexing_index_time_seconds_total",
              children: [
                {
                  value: "9.9.2.156",
                  label: "9.9.2.156",
                  children: [
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-14",
                      label: "data-node-14",
                    },
                    {
                      value: "data-node-19",
                      label: "data-node-19",
                    },
                  ],
                },
                {
                  value: "9.9.2.154",
                  label: "9.9.2.154",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                    {
                      value: "data-node-17",
                      label: "data-node-17",
                    },
                  ],
                },
                {
                  value: "9.9.2.157",
                  label: "9.9.2.157",
                  children: [
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                    {
                      value: "data-node-15",
                      label: "data-node-15",
                    },
                    {
                      value: "data-node-20",
                      label: "data-node-20",
                    },
                  ],
                },
                {
                  value: "9.9.2.155",
                  label: "9.9.2.155",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-13",
                      label: "data-node-13",
                    },
                    {
                      value: "data-node-18",
                      label: "data-node-18",
                    },
                  ],
                },
                {
                  value: "9.9.2.153",
                  label: "9.9.2.153",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                    {
                      value: "data-node-16",
                      label: "data-node-16",
                    },
                  ],
                },
                {
                  value: "9.9.3.150",
                  label: "9.9.3.150",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.3.151",
                  label: "9.9.3.151",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.3.152",
                  label: "9.9.3.152",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_indices_search_query_time_seconds",
              label: "elasticsearch_indices_search_query_time_seconds",
              children: [
                {
                  value: "9.9.2.156",
                  label: "9.9.2.156",
                  children: [
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-14",
                      label: "data-node-14",
                    },
                    {
                      value: "data-node-19",
                      label: "data-node-19",
                    },
                  ],
                },
                {
                  value: "9.9.2.154",
                  label: "9.9.2.154",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                    {
                      value: "data-node-17",
                      label: "data-node-17",
                    },
                  ],
                },
                {
                  value: "9.9.2.157",
                  label: "9.9.2.157",
                  children: [
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                    {
                      value: "data-node-15",
                      label: "data-node-15",
                    },
                    {
                      value: "data-node-20",
                      label: "data-node-20",
                    },
                  ],
                },
                {
                  value: "9.9.2.155",
                  label: "9.9.2.155",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-13",
                      label: "data-node-13",
                    },
                    {
                      value: "data-node-18",
                      label: "data-node-18",
                    },
                  ],
                },
                {
                  value: "9.9.2.153",
                  label: "9.9.2.153",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                    {
                      value: "data-node-16",
                      label: "data-node-16",
                    },
                  ],
                },
                {
                  value: "9.9.3.150",
                  label: "9.9.3.150",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.3.151",
                  label: "9.9.3.151",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.3.152",
                  label: "9.9.3.152",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_os_load5",
              label: "elasticsearch_os_load5",
              children: [
                {
                  value: "9.9.2.156",
                  label: "9.9.2.156",
                  children: [
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-14",
                      label: "data-node-14",
                    },
                    {
                      value: "data-node-19",
                      label: "data-node-19",
                    },
                  ],
                },
                {
                  value: "9.9.2.154",
                  label: "9.9.2.154",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                    {
                      value: "data-node-17",
                      label: "data-node-17",
                    },
                  ],
                },
                {
                  value: "9.9.2.157",
                  label: "9.9.2.157",
                  children: [
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                    {
                      value: "data-node-15",
                      label: "data-node-15",
                    },
                    {
                      value: "data-node-20",
                      label: "data-node-20",
                    },
                  ],
                },
                {
                  value: "9.9.2.155",
                  label: "9.9.2.155",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-13",
                      label: "data-node-13",
                    },
                    {
                      value: "data-node-18",
                      label: "data-node-18",
                    },
                  ],
                },
                {
                  value: "9.9.2.153",
                  label: "9.9.2.153",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                    {
                      value: "data-node-16",
                      label: "data-node-16",
                    },
                  ],
                },
                {
                  value: "9.9.3.150",
                  label: "9.9.3.150",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.3.151",
                  label: "9.9.3.151",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.3.152",
                  label: "9.9.3.152",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_process_cpu_percent",
              label: "elasticsearch_process_cpu_percent",
              children: [
                {
                  value: "9.9.2.156",
                  label: "9.9.2.156",
                  children: [
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-14",
                      label: "data-node-14",
                    },
                    {
                      value: "data-node-19",
                      label: "data-node-19",
                    },
                  ],
                },
                {
                  value: "9.9.2.154",
                  label: "9.9.2.154",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                    {
                      value: "data-node-17",
                      label: "data-node-17",
                    },
                  ],
                },
                {
                  value: "9.9.2.157",
                  label: "9.9.2.157",
                  children: [
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                    {
                      value: "data-node-15",
                      label: "data-node-15",
                    },
                    {
                      value: "data-node-20",
                      label: "data-node-20",
                    },
                  ],
                },
                {
                  value: "9.9.2.155",
                  label: "9.9.2.155",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-13",
                      label: "data-node-13",
                    },
                    {
                      value: "data-node-18",
                      label: "data-node-18",
                    },
                  ],
                },
                {
                  value: "9.9.2.153",
                  label: "9.9.2.153",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                    {
                      value: "data-node-16",
                      label: "data-node-16",
                    },
                  ],
                },
                {
                  value: "9.9.3.150",
                  label: "9.9.3.150",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.3.151",
                  label: "9.9.3.151",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.3.152",
                  label: "9.9.3.152",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_transport_rx_size_bytes_total",
              label: "elasticsearch_transport_rx_size_bytes_total",
              children: [
                {
                  value: "9.9.2.156",
                  label: "9.9.2.156",
                  children: [
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-14",
                      label: "data-node-14",
                    },
                    {
                      value: "data-node-19",
                      label: "data-node-19",
                    },
                  ],
                },
                {
                  value: "9.9.2.154",
                  label: "9.9.2.154",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                    {
                      value: "data-node-17",
                      label: "data-node-17",
                    },
                  ],
                },
                {
                  value: "9.9.2.157",
                  label: "9.9.2.157",
                  children: [
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                    {
                      value: "data-node-15",
                      label: "data-node-15",
                    },
                    {
                      value: "data-node-20",
                      label: "data-node-20",
                    },
                  ],
                },
                {
                  value: "9.9.2.155",
                  label: "9.9.2.155",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-13",
                      label: "data-node-13",
                    },
                    {
                      value: "data-node-18",
                      label: "data-node-18",
                    },
                  ],
                },
                {
                  value: "9.9.2.153",
                  label: "9.9.2.153",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                    {
                      value: "data-node-16",
                      label: "data-node-16",
                    },
                  ],
                },
                {
                  value: "9.9.3.150",
                  label: "9.9.3.150",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.3.151",
                  label: "9.9.3.151",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.3.152",
                  label: "9.9.3.152",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_transport_tx_size_bytes_total",
              label: "elasticsearch_transport_tx_size_bytes_total",
              children: [
                {
                  value: "9.9.2.156",
                  label: "9.9.2.156",
                  children: [
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-14",
                      label: "data-node-14",
                    },
                    {
                      value: "data-node-19",
                      label: "data-node-19",
                    },
                  ],
                },
                {
                  value: "9.9.2.154",
                  label: "9.9.2.154",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                    {
                      value: "data-node-17",
                      label: "data-node-17",
                    },
                  ],
                },
                {
                  value: "9.9.2.157",
                  label: "9.9.2.157",
                  children: [
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                    {
                      value: "data-node-15",
                      label: "data-node-15",
                    },
                    {
                      value: "data-node-20",
                      label: "data-node-20",
                    },
                  ],
                },
                {
                  value: "9.9.2.155",
                  label: "9.9.2.155",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-13",
                      label: "data-node-13",
                    },
                    {
                      value: "data-node-18",
                      label: "data-node-18",
                    },
                  ],
                },
                {
                  value: "9.9.2.153",
                  label: "9.9.2.153",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                    {
                      value: "data-node-16",
                      label: "data-node-16",
                    },
                  ],
                },
                {
                  value: "9.9.3.150",
                  label: "9.9.3.150",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.3.151",
                  label: "9.9.3.151",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.3.152",
                  label: "9.9.3.152",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
          ],
        },
        {
          value: "cc-cc553-interestPrice",
          label: "cc-cc553-interestPrice",
          children: [
            {
              value: "elasticsearch_indices_indexing_index_time_seconds_total",
              label: "elasticsearch_indices_indexing_index_time_seconds_total",
              children: [
                {
                  value: "9.9.6.148",
                  label: "9.9.6.148",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                  ],
                },
                {
                  value: "9.9.6.147",
                  label: "9.9.6.147",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                  ],
                },
                {
                  value: "9.9.6.149",
                  label: "9.9.6.149",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                  ],
                },
                {
                  value: "9.9.5.159",
                  label: "9.9.5.159",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.5.160",
                  label: "9.9.5.160",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.5.161",
                  label: "9.9.5.161",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_indices_search_query_time_seconds",
              label: "elasticsearch_indices_search_query_time_seconds",
              children: [
                {
                  value: "9.9.6.148",
                  label: "9.9.6.148",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                  ],
                },
                {
                  value: "9.9.6.147",
                  label: "9.9.6.147",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                  ],
                },
                {
                  value: "9.9.6.149",
                  label: "9.9.6.149",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                  ],
                },
                {
                  value: "9.9.5.159",
                  label: "9.9.5.159",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.5.160",
                  label: "9.9.5.160",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.5.161",
                  label: "9.9.5.161",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_os_load5",
              label: "elasticsearch_os_load5",
              children: [
                {
                  value: "9.9.6.148",
                  label: "9.9.6.148",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                  ],
                },
                {
                  value: "9.9.6.147",
                  label: "9.9.6.147",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                  ],
                },
                {
                  value: "9.9.6.149",
                  label: "9.9.6.149",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                  ],
                },
                {
                  value: "9.9.5.159",
                  label: "9.9.5.159",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.5.160",
                  label: "9.9.5.160",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.5.161",
                  label: "9.9.5.161",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_process_cpu_percent",
              label: "elasticsearch_process_cpu_percent",
              children: [
                {
                  value: "9.9.6.148",
                  label: "9.9.6.148",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                  ],
                },
                {
                  value: "9.9.6.147",
                  label: "9.9.6.147",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                  ],
                },
                {
                  value: "9.9.6.149",
                  label: "9.9.6.149",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                  ],
                },
                {
                  value: "9.9.5.159",
                  label: "9.9.5.159",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.5.160",
                  label: "9.9.5.160",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.5.161",
                  label: "9.9.5.161",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_transport_rx_size_bytes_total",
              label: "elasticsearch_transport_rx_size_bytes_total",
              children: [
                {
                  value: "9.9.6.148",
                  label: "9.9.6.148",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                  ],
                },
                {
                  value: "9.9.6.147",
                  label: "9.9.6.147",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                  ],
                },
                {
                  value: "9.9.6.149",
                  label: "9.9.6.149",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                  ],
                },
                {
                  value: "9.9.5.159",
                  label: "9.9.5.159",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.5.160",
                  label: "9.9.5.160",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.5.161",
                  label: "9.9.5.161",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
            {
              value: "elasticsearch_transport_tx_size_bytes_total",
              label: "elasticsearch_transport_tx_size_bytes_total",
              children: [
                {
                  value: "9.9.6.148",
                  label: "9.9.6.148",
                  children: [
                    {
                      value: "data-node-02",
                      label: "data-node-02",
                    },
                    {
                      value: "data-node-05",
                      label: "data-node-05",
                    },
                    {
                      value: "data-node-08",
                      label: "data-node-08",
                    },
                    {
                      value: "data-node-11",
                      label: "data-node-11",
                    },
                  ],
                },
                {
                  value: "9.9.6.147",
                  label: "9.9.6.147",
                  children: [
                    {
                      value: "data-node-01",
                      label: "data-node-01",
                    },
                    {
                      value: "data-node-04",
                      label: "data-node-04",
                    },
                    {
                      value: "data-node-07",
                      label: "data-node-07",
                    },
                    {
                      value: "data-node-10",
                      label: "data-node-10",
                    },
                  ],
                },
                {
                  value: "9.9.6.149",
                  label: "9.9.6.149",
                  children: [
                    {
                      value: "data-node-03",
                      label: "data-node-03",
                    },
                    {
                      value: "data-node-06",
                      label: "data-node-06",
                    },
                    {
                      value: "data-node-09",
                      label: "data-node-09",
                    },
                    {
                      value: "data-node-12",
                      label: "data-node-12",
                    },
                  ],
                },
                {
                  value: "9.9.5.159",
                  label: "9.9.5.159",
                  children: [
                    {
                      value: "master-vm-01",
                      label: "master-vm-01",
                    },
                  ],
                },
                {
                  value: "9.9.5.160",
                  label: "9.9.5.160",
                  children: [
                    {
                      value: "master-vm-02",
                      label: "master-vm-02",
                    },
                  ],
                },
                {
                  value: "9.9.5.161",
                  label: "9.9.5.161",
                  children: [
                    {
                      value: "master-vm-03",
                      label: "master-vm-03",
                    },
                  ],
                },
              ],
            },
          ],
        },
      ],
    };
  },
};
</script>
    