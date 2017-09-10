import os
import subprocess

# 自动识别简单验证码（字母+数字）
def image_to_string(img, cleanup=True, plus=''):
    # cleanup为True则识别完成后删除生成的文本文件
    # plus参数为给tesseract的附加高级参数
    subprocess.check_output('tesseract ' + img + ' ' +
                            img + ' ' + plus, shell=True)  # 生成同名txt文件
    text = ''
    with open(img + '.txt', 'r') as f:
        text = f.read().strip()
    if cleanup:
        os.remove(img + '.txt')
    return text


def verifycode(url):
    # 跳转到有验证码的页面
    # ...
    
    # 找到当前验证码图片，并进行截图保存重命名为verifycode.png
    verifycode = driver.find_element_by_id("SafeCodeImg")
    # 首先截取当前页面
    driver.save_screenshot('verifyimg.png')
    # 定位验证码图片的位置
    left = verifycode.location['x']
    top = verifycode.location['y']
    right = verifycode.location['x'] + verifycode.size['width']
    bottom = verifycode.location['y'] + verifycode.size['height']
    # 减裁页面，只保留验证码图片即可
    im = Image.open('verifyimg.png') 
    im = im.crop((left, top, right, bottom))
    im.save('verifyimg.png')


# False根据需要决定是否改为True
# '-l eng',如果有报错可直接删除
print(image_to_string('verifyimg.png', False, '-l eng'))