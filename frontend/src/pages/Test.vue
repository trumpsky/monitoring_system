<template>
    <div>
        home
        <div>
            {{ msg }}
        </div>
        <!-- 登录 -->
        <div class="login-form">
            <div class="title">登录即送999</div>
            <el-form :model="form" :rules="rules" ref="form" label-width="80px">
                <el-form-item label="用户名" prop="username">
                    <el-input v-model="form.username"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-input type="password" v-model="form.password"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="login">登录</el-button>
                </el-form-item>
            </el-form>
        </div>
        <img :src="imgUrl" alt="111111" />
    </div>
</template>
<script>
export default {
    components: {
    },
    data() {
        return {
            msg: '',
            form: {
                username: '',
                password: ''
            },
            rules: {
                username: [
                    { required: true, message: '请输入用户名', trigger: 'blur' }
                ],
                password: [
                    { required: true, message: '请输入密码', trigger: 'blur' }
                ]
            },
            imgUrl: ''
        }
    },
    methods: {
        login () {
            this.$refs.form.validate((valid) => {
                if (valid) {
                    let params = new URLSearchParams()
                    params.append('username', this.form.username)
                    params.append('password', this.form.password)
                    this.$http.post('http://localhost:5000/dataShow/login', params).then(res => {
                        console.log(res)
                        if (res.data === 'good') {
                            this.$message.success('登录成功')
                        } else {
                            this.$message.error('登录失败')
                        }
                    })
                } else {
                    this.$message.error('请填写完整信息')
                    return false
                }
            })
        }
    },
    mounted() {
        // this.$http.post('http://localhost:5000/').then(res => {
        //     this.msg = res.data
        // })
        // this.imgUrl = this.HOST + 'test/1.jpg'
    }
}
</script>
<style scoped>
.login-form {
    width: 400px;
    background: rgb(250, 242, 208);
    margin: 10px auto;
    padding: 20px;
}
.login-form .title {
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    margin: 20px;
}
</style>
