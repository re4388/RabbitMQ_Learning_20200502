
# RabbitMQ Learning

## Installing on Windows
https://www.rabbitmq.com/install-windows.html

## 在 Ubuntu Linux 中安裝與使用 RabbitMQ 訊息佇列
https://blog.gtwang.org/linux/ubuntu-linux-install-rabbitmq/

## 以 RabbitMQ 實作工作佇列（Work Queues）（Python 版本）
https://blog.gtwang.org/programming/rabbitmq-work-queues-in-python/

## 以 RabbitMQ 實作 Publish/Subscribe 模型（Python 版本）
https://blog.gtwang.org/programming/rabbitmq-publish-subscribe-pattern-python/


## Probelm solved
1. `TypeError: basic_consume() got multiple values for argument 'queue'`
https://blog.csdn.net/weixin_43178103/article/details/89472378?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1

2. python3 need to encode and decode to solve byte and str convertion
https://stackoverflow.com/questions/33003498/typeerror-a-bytes-like-object-is-required-not-str
use `.decode('utf-8')` and `.encode('utf-8')` 