'''
@Description: A text embedding model and reranking model produced by YouDao Inc., which can be use for dense embedding retrieval and reranking in RAG workflow.
@Author: shenlei
@Date: 2023-11-28 17:53:45
@LastEditTime: 2024-01-03 17:35:55
@LastEditors: shenlei
'''
from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name='BCEmbedding',
    version='0.0.4',
    license='apache-2.0',
    description='A text embedding model and reranking model produced by Netease Youdao Inc., which can be use for dense embedding retrieval and reranking in RAG workflow.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Netease Youdao, Inc.',
    author_email='shenlei02@corp.netease.com',
    url='https://gitlab.corp.youdao.com/ai/BCEmbedding',
    packages=find_packages(),
    install_requires=[
        'torch>=1.8.1, <=2.1.0',
        'transformers==4.36.0',
        'datasets==2.16.0',
        'faiss-cpu==1.7.4',
        'mteb==1.1.1',
    ]
)
