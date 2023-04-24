<template>
  <footer class="footer">
    <div class="footer__main">
      <a href="https://git.code.tencent.com/Shiqi_Chen/monitoring_system">
        <h4 class="footer__nav-title">加入我们</h4>
      </a>
      <h4 class="footer__nav-title" @click="showModal">联系我们</h4>
      <el-dialog :visible.sync="visible" width="50%" :before-close="handleClose">
        <span class="information">团队信息</span>
        <el-table :data="data" style="width: 100%">
          <el-table-column prop="name" label="姓名" width="180">
          </el-table-column>
          <el-table-column prop="age" label="学号" width="180">
          </el-table-column>
          <el-table-column prop="address" label="邮箱">
          </el-table-column>
        </el-table>
        <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="visible = false" class="button">确 定</el-button>
        </span>
      </el-dialog>
    </div>
    <div class="footer__copyright">
      <h4>2022 NKU软件测试与维护-大数据集群监控系统</h4>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      visible: false,
      data: [
        {
          name: "陈子昂",
          age: 2012217,
          address: "1812432358@qq.com",
        },
        {
          name: "陈世祺",
          age: 2012661,
          address: "2902529887@qq.com",
        },
        {
          name: "张家冉",
          age: 2012685,
          address: "xiaoni2001@icloud.com",
        },
      ],
    };
  },
  methods: {
    showModal() {
      this.visible = true;
    },
    handleOk(e) {
      console.log(e);
      this.visible = false;
    },
  },
};
</script>

<style scoped>
.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
}

.footer__main {
  display: flex;
}

a {
  margin-right: 10px;
  text-decoration: none;
}

h4 {
  color: rgba(255, 255, 255, 0.8);
  cursor: pointer;
}

.information {
  display: flex;
  color: rgb(63,91,148);;
  margin-left: 10px;
}
.button {
  background-color: rgb(63,91,148);
  color: #fff;
}
</style>
