
### 10.31
1. code object, frame object 
2. 调试部署demo至稳定
3. 数据持久化--挂载遇到的问题
4. tj的架构(node节点角度)

### Q
1. service包含多个pod是 挂载失败的原因？
2. mysql redis 的主从复制在k8s内怎么做到
3. 为什么没有使用statefulset资源

### A
1. 为什么使用“原始”的挂载方式？PV PVC的缺点
2. 随之而来的 固定mysql到某个节点

### 11.7
token 通过请求体返回，登录时的vcode-version也通过请求体发送
应该考虑转移到请求头上
基本实现了 账户和 收藏链接的crud 以及用户登录接口

11.16
测试jenkins
add sth and push, 触发webhook jenkins build