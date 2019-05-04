# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_help.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(942, 590)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(1, 0, 941, 591))
        self.frame.setStyleSheet("QLabel{\n"
"    \n"
"    font: 30pt \"Helvetica Neue\";\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(328, 10, 351, 61))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(20, 80, 901, 461))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(820, 550, 113, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "        帮助手册"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">情感分析或意见挖掘是人们的观点，情绪，评估对诸如产品，服务，组织等实体的态度。该领域的发展和快速起步得益于网络上的社交媒体，例如产品评论，论坛讨论，微博，微信的快速发展，因为这是人类历史上第一次有如此巨大数字量的形式记录。自2000年初以来，情绪分析已经成长为自然语言处理（NLP）中最活跃的研究领域之一。也是在数据挖掘，Web挖掘，文本挖掘和信息检索方面有广泛的研究。事实上，它已经从计算机科学蔓延到管理科学和社会科学，如市场营销，金融，政治学，通讯，医疗科学，甚至是历史，由于其重要的商业性引发整个社会的共同关注。这种扩散是由于意见是事实的中心，几乎所有的人类活动，在相当程度上，很在意在别人怎么看。出于这个原因，无论何时我们需要做出决定，我们都会经常寻找别人的意见。这不仅是对企业而言对个人也是如此。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">如今，如果一个人想购买消费产品，其不再局限于问一个人的朋友和家人的意见，因为有很多用户评论和对产品讨论在网络上的公共论坛，我们可以在评论中找出我们想知道的问题，可能还会有令人意想不到的收获。对于一个组织，它可能不再需要进行调查，民意调查和重点人群，以收集公众的意见，因为有丰盈</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">这样的信息公开。近年来，我们目睹了那些帖子通过社交媒体重塑企业形象，讨论明星生活，左右公众的情绪和情感，其中有深刻地影响我们的社会和政治制度，这样的帖子还动员群众政治的变化。当我们在感叹人言可畏的同时，我们也不得不承认社交网络的快速发展带来的巨大的道德问题。由此情感分析孕育而生，我们可以通过情感分析或者是舆情系统来帮助政府监控群众的情感变化或者是舆论趋势，来避免发生恶性事件或者是虚假事件的发生。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">通常来说，</span><a href=\"https://baike.baidu.com/item/%E6%83%85%E6%84%9F/189257\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; text-decoration: underline; color:#136ec2;\">情感</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333;\">分析的目的是为了找出说话者/作者在某些话题上或者针对一个文本两极的观点的态度。这个态度或许是他或她的个人判断或是评估，也许是ta当时的情感状态（就是说，作者在做出这个言论时的情绪状态），或是作者有意向的情感交流（就是</span><a href=\"https://baike.baidu.com/item/%E4%BD%9C%E8%80%85\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; text-decoration: underline; color:#136ec2;\">作者</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333;\">想要读者所体验的</span><a href=\"https://baike.baidu.com/item/%E6%83%85%E7%BB%AA/770\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; text-decoration: underline; color:#136ec2;\">情绪</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333;\">）。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">按照处理文本的粒度不同,情感分析大致可分为词语级、句子级、篇章级三个研究层次。</span></p>\n"
"<p style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px; background-color:#ffffff;\"><a name=\"2_1\"></a><span style=\" font-family:\'Microsoft YaHei,SimHei,Verdana\'; font-size:large; color:#333333;\">篇</span><span style=\" font-family:\'Microsoft YaHei,SimHei,Verdana\'; font-size:large; color:#333333;\">章级</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">篇章级别的情感分类是指定一个整体的情绪方向/极性，即确定该文章（例如，完整的在线评论）是否传达总体正面或负面的意见。在这种背景下，这是一个二元分类任务。它也可以是回归任务，例如，从1到5星的审查推断的总体评分。也可以认为这是一次5级分类任务。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">我们可以将自然语言处理技术与模糊逻辑技术相结合，基于手动创建的模糊情感词典，对新闻故事和电影评论进行情感分析。定义情感种类，在模糊情感词典中标注情感类别及其强度。每个词语可以属于多个情感类别。在实验中，可以对比采用词频、与长度相关的特征、语义倾向、情感PMI—IR、强调词和特殊符号等不同特征时的结果。最后对文章的主动性/被动性和积极/消极性进行了判断。</span></p>\n"
"<p style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px; background-color:#ffffff;\"><a name=\"2_2\"></a><span style=\" font-family:\'Microsoft YaHei,SimHei,Verdana\'; font-size:large; color:#333333;\">句</span><span style=\" font-family:\'Microsoft YaHei,SimHei,Verdana\'; font-size:large; color:#333333;\">子级</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">由于句子的情感分析离不开构成句子的词语的情感，其方法划分为三大类：(1)基于知识库的分析方法；(2)基于网络的分析方法；(3)基于语料库的分析方法。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">我们在对文本信息中句子的情感进行识别时，通常创建的情感数据库会包含一些情感符号、缩写、情感词、修饰词等等。我们在具体的实验中会定义几种情感（生气、憎恨、害怕、内疚、感兴趣、高兴、悲伤等），对句子标注其中一种情感类别及其强度值来实现对句子的情感分类。</span></p>\n"
"<p style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px; background-color:#ffffff;\"><a name=\"2_3\"></a><span style=\" font-family:\'Microsoft YaHei,SimHei,Verdana\'; font-size:large; color:#333333;\">词</span><span style=\" font-family:\'Microsoft YaHei,SimHei,Verdana\'; font-size:large; color:#333333;\">语级</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">词语的情感是句子或篇章级情感分析的基础。早期的文本情感分析主要集中在对文本正负极性的判断。词语的情感分析方法主要可归纳为三类：(1)基于词典的分析方法；(2)基于网络的分析方法；(3)基于语料库的分析方法。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">基于词典的分析方法利用词典中的近义、反义关系以及词典的结构层次，计算词语与正、负极性种子词汇之间的语义相似度，根据语义的远近对词语的情感进行分类。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">基于网络的分析方法利用万维网的搜索引擎获取查询的统计信息，计算词语与正、负极性种子词汇之间的语义关联度，从而对词语的情感进行分类。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">基于语料库的分析方法，运用机器学习的相关技术对词语的情感进行分类。机器学习的方法通常需要先让分类模型学习训练数据中的规律，然后用训练好的模型对测试数据进行预测。</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#3366cc;\"> [1]</span><a name=\"ref_[1]_19943925\"></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#136ec2;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">文本情感分析的一个基本步骤是对文本中的某段已知文字的两极性进行分类，这个分类可能是在句子级、功能级。分类的作用就是判断出此文字中表述的观点是积极的、消极的、还是中性的情绪。更高级的“超出两极性”的情感分析还会寻找更复杂的情绪状态，比如“生气”、“悲伤”、“快乐” 等等。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">在文本情感分析领域，早期做出研究贡献的有 Turney和 Pang他们运用了多种方法探测商品评论和电影影评的两极观点。此研究是建立在文档级所进行的分析。另一种文档意见的分类方式可以是多重等级的，Pang和 Snyder(among others):延伸了早先的基础两极意见研究，将电影影评分类并预测为3至4星的多重级别，而 Snyder就餐馆评论做了个深度分析，从多种不同方面预测餐馆的评分，比如食物、气氛等等 （在一个5星的等级制度上）。尽管在大多数统计方面的分类方式中，“中性” 类是经常被忽略的，因为“中性”类的文本经常是处于一个两极分类的边缘地带，但是很多研究者指出，在每个两极化问题当中，都应该识别出三个不同的类别。进一步的说，一些现有的分类方式 例如 Max Entropy和 SVMs可以证明，在分类过程中区分出“中性”类可以帮助提高分类算法的整体准确率。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">另一种判定文本情绪的方法是利用比例换算系统。当一个词普遍被认为跟消极、中性或是积极的情感有关联时，将这个词赋予一个-10到+10之中的数字级别（最消极到最正向情感），在使用自然语言处理来分析一个非结构化文本数据后，余下的的概念也可以被分析来得出词与概念的相关性。接下来，每一个概念都可以被赋予一个分数，这个分数是基于情感词汇和这个概念的关联度，以及他们本身的分数而得出的。这个方法让文本情感的理解晋升到一个更加智能的层面，并且是基于一个11分的等级范围的。另外一种方法是，计算出文本正向的和消极的情感力度分数， 如果研究的目的是要判定一个文本的感情，而不是总体文本集的两极分布或文字的力度。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">另一个研究方向是“主观/客观 识别”。这个研究通常被定义为将一个已知文本（一般是句子）分类成两个类：主观和客观。这个问题有些时候比两极化分类问题更难解决。主观词汇和短语可能是基于前后文语意联系，而一个客观文档有可能包含主观语句（e.g. 一篇新闻引用了某人的观点）。此外， Su也曾提到过，得到的结论在很大程度上依赖于注释文本时对“主观”的定义。不过， Pang证实了如果两极分类前去除文件中的客观语句，会提高算法的表现。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">一个更加优化的分析模型叫做“功能/属性为基础的情感分析（feature/aspect-based sentiment analysis）”。这是指判定针对一个实体在某一个方面或者某一功能下表现出来的意见或是情感， e.g. 一个实体可能是一个手机，一个电子相机，或者空白。一个“功能”或者“方面”是一件实体的某个属性或者组成部分，e.g.一个手机的屏幕，一个相机的成像质量，等等。 这个问题涉及到若干个子问题，譬如，识别相关的实体，提取他们的功能/属性，然后判断是否在提及这个功能/属性时有正面或者负面或者中性的情绪或意见。更多关于这个层面的文本情感分析可以参照NLP手册“情感分析和主观性”这一章。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Form", "关闭"))


