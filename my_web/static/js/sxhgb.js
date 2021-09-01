// 我们采用的时ES6的语法
// 创建Vue对象 vm
let vm = new Vue({
    el: '#app', // 通过ID选择器找到绑定的HTML内容
    // 修改Vue读取变量的语法
    delimiters: ['[[', ']]'],
    data: { // 数据对象
        // v-model
        username: '',
        password: '',
        yourname: '',


        // v-show
        // error_name: false,
        // error_password: false,
        // error_yourname: false,
        is_click: false,
        is_not_click: true,


        // error_message
        // error_name_message: '',
        // error_password_message: '',
        // error_yourname_message: '',
        click_message: '开始学习'
    },
//     mounted() {
//         this.generate_image_code();
//     },
    methods: {
//             let url = '/sms_codes/' + this.mobile + '/?image_code=' + this.image_code + '&uuid=' + this.uuid;
//             axios.get(url, {
//                 responseType: 'json'
//             })
//                 .then(response => {
//                     if (response.data.code == '0') {
//                         //展示倒计时60秒效果
//                         let num = 60;
//                         let t = setInterval(() => {
//                             if (num == 1) {//即将停止倒计时
//                                 clearInterval(t);//停止回调函数的执行
//                                 this.sms_code_tip = '获取短信验证码';//还原sms_code_tip 提示文字
//                                 this.generate_image_code();//重新生成图形验证码
//                                 this.send_flag = false;
//
//                             } else {             //正在倒计时
//                                 num -= 1;
//                                 this.sms_code_tip = num + '秒';
//                             }
//
//                         }, 1000)
//
//                     } else {
//                         if (response.data.code == '4001') {//图形验证码错误
//                             this.error_image_code_message = response.data.errmsg;
//                             this.error_image_code = true;
//                         }
//                         this.send_flag = false;
//
//                     }
//
//                 })
//                 .catch(error => {
//                     console.log(error.response)
//                 })
//         },
//
        // 监听表单提交事件
        on_submit() {
            this.is_click = true;
            this.is_not_click = false;


        }
    }
});