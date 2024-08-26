## 我的ai相关学习笔记

每个知识点都按步骤有序记录下来，并尽可能的在notebook中写全代码注释，以及在markdown文档中记录算法推导过程。


### 数学基础

- [高等数学](math/高等数学.md)
- [线性代数](math/线性代数.md)

### 数据分析与可视化

jupyter notebook ,numpy,pandas,matplotlib

- [开发环境](datahandling/docs/开发环境.md)
- [numpy数据基础](datahandling/01-NumpyArrayBasics/01-NumpyArrayBasics.ipynb)
- [numpy数组创建](datahandling/02-NumpyCreateArray/02CreateNumpyArray.ipynb)
- [numpy数组基本操作](datahandling/03-NumpyArrayBasicOperations/03-NumpyArrayBasicOperations.ipynb)
    - 数组的访问、切片、bool索引、条件索引
- [numpy数组运算](datahandling/04-NumpyComputationArray/04-ComputationNumpyArray.ipynb)
    - 数组加减乘除、矩阵运算、矩阵的逆、伪逆、矩阵转置、数组升维
- [numpy数据合并和拆分](datahandling/05-NumpyConcatenateAndSplit/05-ConcatenateAndSplit.ipynb)
- [numpy统计运算](datahandling/06-NumpyAggregationOperator/06-AggregationOperator.ipynb)
- [numpy排序找索引操作](datahandling/07-NumpyArgAndSortOperation/07-ArgAndSortOperation.ipynb)
- [numpy比较和神奇索引](datahandling/08-ComparisonAndFancyIndexing/08-ComparisonAndFancyIndexing.ipynb)
- [pandas中的数据结构](datahandling/20-PandasDataFrameSeriesPanel/pandasDataFrameSeriesPanel.ipynb)
- [Series创建、属性、计算](datahandling/21-SeriesBasic/seriesBasic.ipynb)
- [Series的索引与基本操作](datahandling/22-SerieIndexAndOperation/22-seriesIndexAndOperation.ipynb)


### 机器学习

- knn
  - [knn理论、公式](machinelearning/01knn.md)  
  - [实现自己的knn](machinelearning/knn/01-kNNBasics/kNNBasics.ipynb)
  - [sklearn中的knn](machinelearning/knn/02-kNNInScikitLearn/kNNinScikitlearn.ipynb)
  - [训练数据集和测试数据集拆分](machinelearning/knn/03-TrainTestSplit/TrainTestSplit.ipynb)
  - [结果准确度](machinelearning/knn/04-AccuracyScore/AccuracyScore.ipynb)
  - [超参数寻找](machinelearning/knn/05-HyperParameters/HyperParameters.ipynb)
  - [网格搜索超参数](machinelearning/knn/06-GridSearch/GridSearch.ipynb)
  - [数据归一化和标准化](machinelearning/knn/07-FeatureScaling/FeatureScaling.ipynb)
  - [sklearn中的标准化](machinelearning/knn/08-ScalerinScikitLearn/ScalerInScikitLearn.ipynb)
  
- 线性回归法
  - [线性回归理论、公式](machinelearning/02线性回归.md)
  - [简单线性回归实现](machinelearning/linearRegression/01-SimpleLinearRegressionImplementation/SimpleLinearRegressionImplementation.ipynb)
  - [向量化运算效率高](machinelearning/linearRegression/02-Vectorization/Vectorization.ipynb)
  - [衡量回归算法的标准，MSE、MAE](machinelearning/linearRegression/03-RegressionMetricsMSE-vs-MAE/RegressionMetricsMSE-vs-MAE.ipynb)
  - [最好的衡量线性回归法的指标：R Squared ](machinelearning/linearRegression/04-R-Squared/R-Squared.ipynb)
  - [正规方程法实现多元线性回归](machinelearning/linearRegression/05-OurLinearRegression/OurLinearRegression.ipynb)
  - [sklearn中解决线性回归](machinelearning/linearRegression/06-RegressionInScikitLlearn/RegressionInScikitlearn.ipynb)
- 梯度下降法
  - [梯度下降法理论、公式](machinelearning/03梯度下降法.md)
  - [模拟实现梯度下降法(单变量)](machinelearning/gradientDescent/01-GradientDescentSimulations/01-GradientDescentSimulations.ipynb)
  - [在线性回归中实现梯度下降法](machinelearning/gradientDescent/02-ImplementGradientDescentInLinearRegression/02-ImplementGradientDescentInLinearRegression.ipynb)
  - [梯度下降向量化公式及性能和正规方程对比](machinelearning/gradientDescent/03-VectorizeGradientDescent/03-VectorizeGradientDescent.ipynb)
  - [随机梯度下降法](machinelearning/gradientDescent/04-StochasticGradientDescent/04-StochasticGradientDescent.ipynb)



## links
- [基于Python的数据分析与可视化](https://juejin.cn/book/7240731597035864121)
- [sklearn官网](https://scikit-learn.org/stable/index.html)
- [Python3入门机器学习 经典算法与应用](https://coding.imooc.com/class/chapter/169.html)
- 书籍
  - 机器学习(公式推导与代码实现)
  - 从零开始机器学习的数学原理和算法实践
  - 跟着迪哥学python数据分析与机器学习实战




