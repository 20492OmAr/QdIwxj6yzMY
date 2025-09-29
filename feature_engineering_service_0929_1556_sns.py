# 代码生成时间: 2025-09-29 15:56:41
import pandas as pd
from sanic import Sanic
from sanic.response import json
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif


# 创建Sanic应用
app = Sanic('FeatureEngineeringService')


# 特征工程处理类
class FeatureEngineeringService:
    def __init__(self):
        # 初始化标准化、归一化、PCA、特征选择对象
        self.scaler = StandardScaler()
        self.minmax_scaler = MinMaxScaler()
        self.pca = PCA()
        self.feature_selector = SelectKBest(f_classif)

    def scale_data(self, data):
        """标准化数据"""
        try:
            scaled_data = self.scaler.fit_transform(data)
            return scaled_data
        except Exception as e:
            return str(e)

    def normalize_data(self, data):
        """归一化数据"""
        try:
            normalized_data = self.minmax_scaler.fit_transform(data)
            return normalized_data
        except Exception as e:
            return str(e)

    def reduce_dimensions(self, data, n_components):
        """使用PCA降低数据维度"""
        try:
            reduced_data = self.pca.fit_transform(data)
            if n_components is not None and n_components < reduced_data.shape[1]:
                self.pca.n_components = n_components
                reduced_data = self.pca.fit_transform(data)
            return reduced_data
        except Exception as e:
            return str(e)

    def select_features(self, data, k):
        "