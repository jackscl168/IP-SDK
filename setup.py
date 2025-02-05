import setuptools  # ����setuptools�������

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IP-SDK",  # ���Լ������滻���е�YOUR_USERNAME_
    version="2.3.0",  # ���汾�ţ�����ά���汾,��֤ÿ�η������ǰ汾����Ψһ��
    author="YuZhou.Inc",  # ���ߣ�����д�Լ�������
    author_email="chonglun.shi@nigilent.com",  # ������ϵ��ʽ����д�Լ��������ַ
    description="IP-SDK is used for RainDrop Instruments Program Control",  # ���ļ���
    long_description=long_description,  # ������ϸ���ܣ�һ����README.md�ļ���
    long_description_content_type="text/markdown",
    url="https://github.com/Lvan826199/mwjApiTest",  # �Լ���Ŀ��ַ������github����Ŀ��ַ
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts" : ['IP-SDK = IP-SDK.manage:run']
    }, #��װ�ɹ���������������mwjApiTest ���൱��ִ����mwjApiTest.manage.py�е�run��
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # ��python����Ͱ汾Ҫ��
)