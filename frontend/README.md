# frontend

> Monitoring system

## 0. 环境配置

- 安装nodejs(v16.16.0)
  - 方法1: 直接安装
    https://nodejs.org/zh-cn/
  - 方法2: 使用nvm安装
    - 安装nvmhttps://github.com/coreybutler/nvm-windows/releases
    - 安装nodejs(需要管理员权限)

    > nvm install 16.16.0
    > nvm use 16.16.0
    >
- 配置npm镜像源

> npm config set registry https://registry.npm.taobao.org

- 配置npm全局和缓存位置

> npm config set prefix "D:\nodeJs\nodeJs_install\node_global"
> npm config set cache "D:\nodeJs\nodeJs_install\node_cache"

## 1. 项目搭建

- 使用webpack搭建项目

> vue init webpack _frontend

- 注: 除了vue-router, 其他选项均不安装

## 2. 运行步骤

- 进入frontend目录

> cd frontend

- 安装npm依赖

> yarn install

- 运行项目

> yarn run dev

## 3. 项目结构

```
frontend
├─ README.md
├─ build // 构建工具
├─ config // 配置文件
├─ index.html
├─ package-lock.json
├─ package.json
├─ postcss.config.js
├─ src
│  ├─ App.vue // 所有页面的总组件
│  ├─ assets // 存放静态资源
│  │  ├─ css 
│  │  ├─ images
│  │  └─ js
│  │     └─ index.js // 存放常用js函数
│  ├─ components // 多次使用或共用的组件
│  │  ├─ footer.vue
│  │  └─ header.vue
│  ├─ main.js // 项目入口以及总配置
│  ├─ pages // 页面
│  │  ├─ tests // 多个相关页面放在同一个文件夹
│  │  │  ├─ test1.vue
│  │  │  └─ test2.vue
│  │  └─ Test.vue // 测试页面
│  └─ router // 路由跳转
│     └─ index.js
└─ static
   └─ .gitkeep
```

## 4. 全局配置

1. 跨域配置

   - 在config/index.js中配置proxyTable
   - 例如:

   ```javascript
   proxyTable: {
     '/api': {
       target: 'http://localhost:8080',
       changeOrigin: true,
       secure: false,
       pathRewrite: {
           '^/api': ''
       }
     }
   }
   ```

   - 说明:
     - 前端请求时使用/api替代target
     - changeOrigin表示是否跨域
     - pathRewrite表示重写url
     - secure表示是否https协议
2. 组件全局配置

   - 在main.js中配置
   - 例如:

   ```javascript
   import elementUI from 'element-ui'
   import 'element-ui/lib/theme-chalk/index.css'
   Vue.use(elementUI)
   ```

## 5. 项目规范

1. 请求接口

   - 已在main.js中配置axios
     '''javascript
     import axios from 'axios'
     Vue.property.$http = axios
     '''
   - 前端请求方式

   ```javascript
       const params = new URLSearchParams()
       params.append('username', 'admin')
       this.$http.post('/api/test', params).then(res => {
           console.log(res)
       }).catch(err => {
           console.log(err)
       })
   ```
2. 路由管理

   - src/router/index.js

   ```javascript
       export default new Router({
           routes: [
               {
                   path: '/',
                   name: 'Test',
                   component: () => import('@/pages/Test')
               }
           ]
       })
   ```
3. vue文件结构

   ```vue
   <template>
   <div></div>
   </template>

   <script>
   export default {
       components: {},
       data() {
       return {};
       },
       methods: {},
       mounted() {}
   };
   </script>

   <style scoped>
   </style>
   ```
4. vue规范

- Vue 官方为组件选项推荐的默认顺序

  - 定义（提供组件的选项）

    - `is`
  - 列表渲染（创建多个变化的相同元素)

    - `v-for`
  - 条件渲染（元素是否渲染/显示）

    - `v-if`
    - `v-else-if`
    - `v-else`
    - `v-show`
    - `v-cloak`
  - 渲染方式（改变元素的渲染方式）

    - `v-pre`
    - `v-once`
  - 全局感知

    - `id`
  - 唯一的 attribute（需要唯一值的 attribute）

    - `ref`
    - `key`
  - 双向绑定（把绑定和事件结合起来）

    - `v-model`
  - 事件（组件事件监听器）

    - `v-on`
  - 内容（覆写元素的内容）

    - `v-html`
    - `v-text`
  - 不推荐同时使用 `v-if` 和 `v-for`。
- 使用 `data` 里的变量时请先在 `data` 里面初始化；
- `props` 指定类型，也就是 `type`；
- 不在 `mounted`、`created` 之类的方法里直接写取异步数据的逻辑，将方法抽象出来，只在此处调用；

5. 命名规范
   - 文件夹名为小写字母，多个单词用下划线连接
   - 页面、组件均使用大驼峰命名
   - 变量、方法、属性使用小驼峰命名
   - props、emit使用小驼峰命名
