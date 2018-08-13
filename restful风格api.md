#### RESTful：表述性状态传递

Resource Representational State Transfer：通俗来讲就是：资源在网络中以某种表现形式进行状态转移。

**URL定位资源，用HTTP动词（GET,POST,DELETE,PUT等）描述操作。**

既然说到了是用HTTP动词进行操作。那么需要了解这里列出的4.5个非常重要的HTTP动作，这里的0.5个是指PATCH，因为它在功能上与PUT非常类似，剩下4个通常被API开发人员两两结合使用

- GET（SELECT）：从服务器获取一个指定资源或一个资源集合；

- POST（CREATE）：在服务器上创建一个资源；      

- PUT（UPDATE）：更新服务器上的一个资源，需要提供整个资源；

- PATCH（UPDATE）：更新服务器上的一个资源，只提供资源中改变的那部分属性；

- DELETE（DELETE）：移除服务器上的一个资源；

  还有两个不常见的HTTP动作：

- HEAD – 获取一个资源的元数据，例如一组hash数据或者资源的最近一次更新时间；

- OPTIONS – 获取当前用户（Consumer）对资源的访问权限；