# 二、编写一个函数，分别统计出传入的字符串中（可能不止一个）英文字母、空格、数字和其他字符的个数。
def kind (words):
    ZM = 0
    KG = 0
    SZ = 0
    QT = 0
    for w in words:
        if 'a'<=w<='z' or 'A'<=w<='Z':
            ZM += 1
        elif w == ' ':
            KG += 1
        elif '0'<=w<='9':
            SZ += 1
        else:
            QT += 1
    print('英文字母有:%d个' % (ZM))
    print('空格有:%d个' % (KG))
    print('数字有:%d个' % (SZ))
    print('其他字符有:%d个' % (QT))
words = input('请输入任意内容：')
kind(words)