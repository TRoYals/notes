---
title: system-design-101读书笔记
date: 2024-01-09 07:39
article: true
tags: 
link: https://github.com/ByteByteGoHq/system-design-101
---

![](https://github.com/ByteByteGoHq/system-design-101/raw/main/images/banner.jpg)

[System-101](https://github.com/ByteByteGoHq/system-design-101) 的读书笔记

## Communication Protocols (API)
![](https://github.com/ByteByteGoHq/system-design-101/raw/main/images/api-architecture-styles.png)

### API design (RestAPI vs. GraphQL)
![](https://github.com/ByteByteGoHq/system-design-101/raw/main/images/graphQL.jpg)

### gRPC 是什么
![](https://github.com/ByteByteGoHq/system-design-101/raw/main/images/grpc.jpg)  
Step 1: A REST call is made from the client. The request body is usually in JSON format.
> client 请求

Steps 2 - 4: The order service (gRPC client) receives the REST call, transforms it, and makes an RPC call to the payment service. gRPC encodes the **client stub** into a binary format and sends it to the low-level transport layer.
> "client stub" 是客户端用来透明地与远端 gRPC 服务进行通信的本地代表。它隐藏了网络通信的复杂性，让远程服务调用看起来像是本地方法调用一样简单。

Step 5: gRPC sends the packets over the network via HTTP2. Because of binary encoding and network optimizations, gRPC is said to be 5X faster than JSON.
> 为什么要用 gRPC 

Steps 6 - 8: The payment service (gRPC server) receives the packets from the network, decodes them, and invokes the server application.

Steps 9 - 11: The result is returned from the server application, and gets encoded and sent to the transport layer.

Steps 12 - 14: The order service receives the packets, decodes them, and sends the result to the client application.

### Webhook 是什么
![](https://github.com/ByteByteGoHq/system-design-101/raw/main/images/webhook.jpeg)

假设我们有个 eCommerce Web, 我们要完成一次交易, 需要向 payment service provider(PSP) 请求.

1. short polling(短轮巡)  
short polling 的两个缺点
- 要不断的向 payment service 请求
- 外部直接访问交易服务, 不安全
2. Webhook  
We can register a webhook with the external service. It means: call me back at a certain URL when you have updates on the request. When the PSP has completed the processing, it will invoke the HTTP request to update the payment status.

What if the PSP never calls back? We can set up a housekeeping job to check payment status every hour.

webhook 又被称为*reverse APIs*, 使用 webhook 需要注意的三件事情
- design proper API
- API gateway for security
- register the correct URL at the external service

### 提高 API performance
![](https://github.com/ByteByteGoHq/system-design-101/raw/main/images/api-performance.jpg)

Pagination  
分页, 从数据库或服务请求大量结果时，为了提高服务的响应性，不是一次性将所有结果发送给客户端，而是将结果分批次逐渐地发送给客户端。
> shopee 的店家页面, 货品信息的 api 全部是按照页面设计

异步日志 (Asynchronous Logging)  
**异步日志记录**则采用了不同的策略。当应用程序产生日志时，它首先将日志信息发送到一个内存中的缓冲区，通常是一个无锁的队列。这个操作相比磁盘 I/O 要快得多，因此应用程序几乎可以立即返回继续执行。然后，一个单独的后台进程或线程会负责定期地将缓冲区中的日志数据批量写入磁盘。这种方法大大减少了 I/O 开销，因为它减少了磁盘操作的次数，并且可以利用批处理和其他优化技术来提高效率。

缓存 (Caching)