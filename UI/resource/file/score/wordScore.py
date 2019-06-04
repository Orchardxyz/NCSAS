'''
Created on 2019年4月30日

@author: cws

计算形容词得分
'''
import jpype
import os


def word_score(word):
    '''计算词的情感趋势值
    
    Args:
        word: 需要计算趋势值的词
        
    Returns：
                    词的情感趋势值
                    
    '''

    filepath = os.path.dirname (os.path.abspath (__file__))
    java_package_dir = os.path.join(filepath, "similarity.jar")
    java_dependency_dir = os.path.join(filepath, "dependency")

    if not jpype.isJVMStarted():
        jpype.startJVM (jpype.getDefaultJVMPath (), "-Djava.class.path="+java_package_dir,
                        "-Djava.ext.dirs="+java_dependency_dir)

    HownetWordTendencyClass = jpype.JClass("org.xm.tendency.word.HownetWordTendency")
    tendencyInstance = HownetWordTendencyClass()  # 创建计算词情感趋势的实例
    wordScore = tendencyInstance.getTendency(word)
    return wordScore


if __name__ == "__main__":
    print(word_score("稳定"))


