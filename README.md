# 我的ai相关学习笔记

- ai相关数学知识
- 数据分析与可视化
- 机器学习
- python

## 数学基础

- [高等数学](math/高等数学.md)
- [线性代数](math/线性代数.md)
- [概率统计](math/概率统计.md)

## 数据处理分析与可视化

jupyter notebook ,numpy,pandas,matplotlib

- [开发环境](datahandling/开发环境.md)
- [数据领域中的专业术语](datahandling/数据领域中的专业术语.md)
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
- pandas
    - [dataframe创建、基本属性与索引切片](datahandling/23-PandasDataframeBasic/dataframeBasic.ipynb)
    - [dataframe中的方法与索引技巧](datahandling/24-PandasDataframeMethodAndIndex/dataframeMethodAndIndex.ipynb)
    - [dataframe统计运算和逻辑运算](datahandling/25-PandasDataframeStatAndLogic/dataframeStatAndLogic.ipynb)
    - [dataframe数据计算](datahandling/26-PandasDataframeCompute/dataframe_compute.ipynb)
    - [时间序列](datahandling/27-PandasTime/pandas_time.ipynb)
    - [io的读取和存储、缺失值处理、离散化处理](datahandling/28-PandasIoAndNanAndDiscrete/pandasIoNan.ipynb)
- matplot
    - [matplot基础](datahandling/31-Matplotlib-Basics/Matplotlib-Basics.ipynb)
    - [matplot其他](datahandling/32-Matplot/matplot.ipynb)

## 机器学习

- knn
    - [knn理论、公式](machinelearning/knn.md)
    - [实现自己的knn](machinelearning/knn/01-kNNBasics/kNNBasics.ipynb)
    - [sklearn中的knn](machinelearning/knn/02-kNNInScikitLearn/kNNinScikitlearn.ipynb)
    - [训练数据集和测试数据集拆分](machinelearning/knn/03-TrainTestSplit/TrainTestSplit.ipynb)
    - [结果准确度](machinelearning/knn/04-AccuracyScore/AccuracyScore.ipynb)
    - [超参数寻找](machinelearning/knn/05-HyperParameters/HyperParameters.ipynb)
    - [网格搜索超参数](machinelearning/knn/06-GridSearch/GridSearch.ipynb)
    - [数据归一化和标准化](machinelearning/knn/07-FeatureScaling/FeatureScaling.ipynb)
    - [sklearn中的标准化](machinelearning/knn/08-ScalerinScikitLearn/ScalerInScikitLearn.ipyn)
- 线性回归法
    - [线性回归理论、公式](machinelearning/线性回归.md)
    - [简单线性回归实现](machinelearning/linearRegression/01-SimpleLinearRegressionImplementation/SimpleLinearRegressionImplementation.ipynb)
    - [向量化运算效率高](machinelearning/linearRegression/02-Vectorization/Vectorization.ipynb)
    - [衡量回归算法的标准，MSE、MAE](machinelearning/linearRegression/03-RegressionMetricsMSE-vs-MAE/RegressionMetricsMSE-vs-MAE.ipynb)
    - [最好的衡量线性回归法的指标：R Squared ](machinelearning/linearRegression/04-R-Squared/R-Squared.ipynb)
    - [正规方程法实现多元线性回归](machinelearning/linearRegression/05-OurLinearRegression/OurLinearRegression.ipynb)
    - [sklearn中解决线性回归](machinelearning/linearRegression/06-RegressionInScikitLlearn/RegressionInScikitlearn.ipynb)
    - [模拟欠拟合与过拟合、正则化处理](machinelearning/linearRegression/08-UnderfittingAndOverfitting/underfittingAndOverfitting.ipynb)

- 梯度下降法
    - [梯度下降法理论、公式](machinelearning/梯度下降法.md)
    - [模拟实现梯度下降法(单变量)](machinelearning/gradientDescent/01-GradientDescentSimulations/01-GradientDescentSimulations.ipynb)
    - [在线性回归中实现梯度下降法](machinelearning/gradientDescent/02-ImplementGradientDescentInLinearRegression/02-ImplementGradientDescentInLinearRegression.ipynb)
    - [梯度下降向量化公式及性能和正规方程对比](machinelearning/gradientDescent/03-VectorizeGradientDescent/03-VectorizeGradientDescent.ipynb)
    - [随机梯度下降法](machinelearning/gradientDescent/04-StochasticGradientDescent/04-StochasticGradientDescent.ipynb)
    - [sklearn中的随机梯度下降法](machinelearning/gradientDescent/05-SGDInScikitLearn/SGDInScikitLearn.ipynb)
    - [关于梯度的计算调试](machinelearning/gradientDescent/06-DebugGradient/DebugGradient.ipynb)
- 多项式回归与模型泛化
  - [什么是多项式回归](machinelearning/polynomialRegressionAndModelGeneralization/01-whatIsPolynomialRegression/whatIsPolynomialRegression.ipynb)
  - [scikit-learn中的多项式回归和Pipeline](machinelearning/polynomialRegressionAndModelGeneralization/02-PolynomialRegressionInScikitLearn/polynomialRegressionInScikitLearn.ipynb)
  - [过拟合与欠拟合](machinelearning/polynomialRegressionAndModelGeneralization/03-OverfittingAndUnderfitting/overfittingAndUnderfitting.ipynb)
  - [为什么使用测试数据集](machinelearning/polynomialRegressionAndModelGeneralization/04-WhyTrainTestSplit/WhyTrainTestSplit.ipynb)
  - [学习曲线](machinelearning/polynomialRegressionAndModelGeneralization/05-LearningCurve/LearningCurve.ipynb)
  - [k折交叉验证](machinelearning/polynomialRegressionAndModelGeneralization/06-ValidationAndCrossValidation/validationAndCrossValidation.ipynb)
  - [岭回归](machinelearning/polynomialRegressionAndModelGeneralization/08-ModelRegularizationAndRidgeRegression/modelRegularizationAndRidgeRegression.ipynb)
  - [LASSO回归](machinelearning/polynomialRegressionAndModelGeneralization/09-LASSORegression/LASSO-Regression.ipynb)
- PCA
  - [PCA理论、公式](machinelearning/PCA与梯度上升法.md)
  - [使用梯度上升法实现PCA](machinelearning/pcaAndGradientAscent/01-Implement-PCA-in-BGA/Implement-PCA-in-BGA.ipynb)
  
- 逻辑回归
    - [逻辑回归理论、公式](machinelearning/逻辑回归.md)

- 朴素叶贝斯

### 案例

#### 推荐系统相关

- [推荐系统快速入门](machinelearning/推荐系统入门.md)
- [用户口味、余弦相似性](machinelearning/recommand/01consine_simiartiy/consine_similarty.ipynb)
- [用户消费能力、标准化欧式距离](machinelearning/recommand/02distance/distance.ipynb)
- [NearestNeighbors、余弦相似性找出最相似的用户](machinelearning/recommand/03NearestNeighborsAndConsineSimiarity/NearestNeighbors_and_consine_simiarity.ipynb)

## links

- 高等数学第6版上册
- 基于Python的数据分析与可视化-掘金小册
- 重学线性代数-极客时间
- Python核心技术与实战-极客时间
- 数据分析实战45讲-极客时间
- 机器学习(公式推导与代码实现)
- 从零开始机器学习的数学原理和算法实践




