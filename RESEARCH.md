# 掌上高考API签名机制研究

> **法律声明**：本项目仅用于Web API安全技术研究，不涉及任何掌上高考的业务数据或用户隐私。所有分析基于公开可见的网络请求。

## 研究目标

1. 逆向分析掌上高考API的签名算法
2. 研究复合加密（HMAC-SHA1 + Base64 + MD5）的实现原理
3. 评估API安全防护机制的有效性
4. 提供Web API安全设计的最佳实践参考

## 技术亮点

### 签名算法逆向
```python
# 签名生成流程
def generate_signature(query_str):
    decoded = unquote(query_str)
    hmac_sha1 = hmac.new(key, decoded, hashlib.sha1)
    base64_str = base64.b64encode(hmac_sha1.digest()).decode()
    return hashlib.md5(base64_str.encode()).hexdigest()
