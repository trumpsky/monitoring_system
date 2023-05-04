<template>
  <div>
    <el-empty description="请等待开发结束"></el-empty>
    <el-row>
      <el-col
        :span="8"
        v-for="(o, index) in 1"
        :key="o"
        :offset="index > 0 ? 2 : 0"
      >
        <el-card :body-style="{ padding: '0px' }">
          <img src="./../assets/images/skm.jpg" class="image" />
          <div style="padding: 14px">
            <span>好吉利的数字</span>
            <div class="bottom clearfix">
              <time class="time">{{ currentDate }}</time>
              <el-button type="text" class="button" @click="thanks"
                >我已助力！</el-button
              >
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { Message } from "element-ui";

export default {
  name: "Product",
  methods: {
    thanks() {
      Message.success("感谢您的助力！系统好感度 +1 ！");
    },
  },
};
</script>

<style scoped>
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>
