# judge_coverage
检查服务端资源覆盖工具
主要应用于检查大规模服务端资源覆盖问题，主要检查中国大陆主流运营商服务端覆盖情况，当前只实现了以下几种情况：
a.判断是否跨运营商覆盖，如果跨运营商覆盖，则打印客户端IP 和对应的服务端IP、省份运营商情况；
b.判断是否是本地覆盖，如果非本地运营商，则打印非本地运营商覆盖，但是是相同运营商覆盖，请检查配置；
c.当前该工具主要应用于ipv4，IPV6未验证，如果使用，请注意自行验证。

这个项目主要用到几个工具，在这里做下简介：
1.dig 工具，主要应用了 +subnet=ip 和+short A 相关功能，核心命令 dig +subnet=clinetIP domain  @119.29.29.29 +short A 命令；
2.国内IP资源归属查询工具：https://ip.useragentinfo.com/json?ip=ip，这个是一个免费的，支持高并发的工具；
3.IPV4地址查询 http:cip.cc/ip 工具，但是此工具显示不是很友好，需要对返回数据进行处理，但是此工具也在主脚本中封装成了函数，可以作为后续选项2中查询出现歧义的一个补充校验工具（当前功能未实现，需要后续补充实现）
4.海外IP查询工具，待补充，期待有缘人补充。
