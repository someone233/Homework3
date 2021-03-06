总体构想:
==
项目名称：南小二——南大闲置物品交易信息发布平台
--
项目背景：
--
    淘宝二手平台近期一份用户调研显示，几
    乎人人都有闲置物品，而超过一半的用户
    倾向于让闲置物品放在一边不作处理。导
    致这种局面的原因，是因为大部分用户没
    有闲余时间及精力再去倒卖闲置物品，而
    小部分用户则是不知道倒卖二手商品的渠
    道。我们的南小二致力于解决南大本校学
    生闲置物品无处安放的苦恼。小程序功能
    与淘宝之前推出的闲鱼app的功能类似，
    但是我们将其迁移到了微信小程序中，使
    其在保留原有功能的基础上更加方便快捷。
    这款微信小程序，会实现许多南大学生变
    闲为现的想法，也响应了当今社会低碳生
    活的号召。
使用方法：
----
    用户在打开小程序并使用微信登录后会弹
    出我们的主页，主页上详细列出了网民们
    出售的闲置物品列表，这些闲置物品会被
    我们分类成化妆品、服饰装扮、食品饮料
    演出门票、数码电子、其他等类别，用户
    点击进入后可以浏览这些商品，也可以在
    检索栏中直接输入商品名称或卖家名称进
    行检索。除了浏览和购买其他人发布的物
    品之外，用户也可以自己通过我们的发布
    物品功能来出售自己的闲置物品，点击发
    布按钮，便可轻松设置转让价、所在地、
    联系方式、物品基本情况等信息。发布成
    功之后如果有人对卖家发布的闲置物品感
    兴趣，在点击物品详情后，可以得到物品
    出售者的联系方式。在完成线下交易后卖
    家或买家任意一方确认交易之后该物品将
    会从待出售的物品清单中删除。本次交易
    成功完成。
设计思路：
==
项目总体结构：
--
    整个项目由欢迎页面、主页、发布页、个
    人信息页及其附属页面（我发布的、我卖
    出的、我买到的、我收藏的、我关注的、
    收到的评价）组成。
各页面之间交互关系：
--
    * 欢迎页：
    只有单个按钮链接到商品主页。
    
    * 主页：
    进入主页后我们可以看到一个轮播图以及下
    方的多个物品的简介，每张图片对应着一个
    物品的详情页面，我们点击心仪物品的图片
    就可链接到该物品的详情，以及发布者的联
    系方式。首页上除了多个物品的简介及推荐
    轮播图之外，还有两个按钮，分别连接到物
    品发布页及个人信息页。
    
    * 物品发布页：
    只有一个发布按钮，用户在输入想要发布的
    物品的名称、价格、描述及上传图片之后点
    击发布，会提示发布成功。之后跳转到主页
    。这时物品栏中会多出一项用户刚刚发布成
    功的物品。
    
    * 个人信息页：
    个人信息页有六个超链接，分别为我发布的、
    我卖出的、我买到的、我收藏的、我关注的、
    收到的评价。除了超链接之外还会显示用户
    信息（昵称、所属院系、联系方式）。
各数据表结构及其作用：
--
用户表：
--
        1.	昵称
        2.	头像
        3.	院系
        4.	timeStamp（主码）
        5.	手机号码
        6.	QQ号
        7.	微信号
        8.	验证邮箱
        9.	性别
    
        * 作用：保存用户的个人信息（微信昵称、院系、
        联系方式、该用户之前买到过的所有商品、以
        及该用户正在出售或已经售出的所有商品清单）
        以便在查找信息之时可以及时的搜索到与该用
        户相关的所有消息。
    
商品表：
--
        1.	商品编号（timeStamp，主码）
        2.	名称
        3.	描述
        4.	价格
        5.	State
        6.	Categories
        7.	Seller
        8.	Buyer
        9.	点击量
        10.	交易完成时间
    
        * 作用：以商品编号作为主码，每一行对应一件
        商品以及与这件商品相关的所有信息。（编号、
        价格、名称、描述、类型、出售者、买家、点击
        量、交易完成时间）。构建商品表的目的是通过
        商品的编号来快速查找及调用与该编号商品有关
        的所有信息。
    
评论表：
--
        1.	被评论用户
        2.	评论用户
        3.	内容
        4.	评论时间
    
        * 作用：因用户可以对另一个用户作出评价，所
        以评论表里保存的是当一个用户对另一个用户作
        出评价时，评论者与被评论者的昵称、评论的内
        容以及评论时间。建立评论表是为了让其他用户
        可以查看其他用户对卖家作出的评价，以便能够
        在进行购买时作出更理智的选择。
    
关注表：
--
        1.	关注者
        2.	被关注者
    
        * 作用：用户可以关注自己感兴趣的商家，商家
        若发布了新的商品，用户从个人信息页面中的“我
        的关注”就可以得知自己关注商家的最新动态。而
        关注表中存的就是关注者与被关注者的昵称信息。
    
收藏表：
--
        1.	用户
        2.	收藏的商品
    
        * 作用：与关注表的功能类似，只不过收藏表是针
        对于某一种特定商品。用户收藏了该商品，下次就
        可以从个人信息页面中我的收藏页面中快捷定位到
        自己之前收藏过的商品，完成购买。收藏表中存储
        的是用户的昵称信息与被收藏物品的商品编号（主
        码）。
    
商品图片表：
--
        1.	商品编号
        2.	图片
    
        * 作用：主页中与商品详情页面中都有每个商品所
        对应的一个或多个图片，商品图片表就是用来存储
        商品编号，以及该编号的商品所对应的一个或多个
        图片。以便在上述页面中可以方便的调出商品图片。
    






