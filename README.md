## 前端运行方式

- 进入frontend目录输入以下命令

> yarn install
> yarn run dev

## 后端运行方式

- 进入backend目录输入以下命令

> 创建虚拟环境
>
> pip install -r requirements.txt
>
> 编写配置文件
>
> python app.py

## 开发流程

### 开发前：

1. 新建issue并进行任务分配

### 开发：

1. 切换到本地main分支，删除上一次开发分支

```
    git checkout main
    git branch -D 你的分支名
```

2、拉取远端main分支

```
    git pull origin main
```

3、建立并切换到自己的分支

```
    git checkout -b 你的名字缩写_issue#序号
```

4、提交并上传代码

```
    git add .
    git commit -m "Add:your message. Closes #序号."(提交信息使用中文)
    git pull --rebase origin main
    git push origin 你的分支名
```

5、自行开发

6、发起merge request

- Titles格式规范与commit message保持一致。
- Description基本格式：
  - Closes #你的issueID

## 常见问题总结

### 前端:

1. yarn install报错

   - 方法1：删除node_modules文件夹，重新执行npm install
   - 方法2：检查yarn镜像源, 设置成淘宝镜像源
     > https://registry.npm.taobao.org
     >
   - 方法3：重新安装nodejs, 统一使用v16.16.0
2. nvm use报错

   > exit status 1: XXXXX(乱码)
   >

   - 方法: 使用管理员运行cmd
3. yarn run serve报错

   - 原因: 项目使用的是webpack, 需要用yarn run dev

### 后端:
