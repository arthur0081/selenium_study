import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
#定位采用火狐的firepath插件对xpath快速定位
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(8)

# 网址登录页面
driver.get("http://192.168.50.232:3003/login")
# 输入用户名
driver.find_element_by_xpath(".//*[@id='normal_login_account']").send_keys("13033010001")
# 输入密码
driver.find_element_by_xpath(".//*[@id='normal_login_password']").send_keys("123456")
time.sleep(3)
# 点击登录
driver.find_element_by_xpath(".//*[@id='root']/div/section/main/div/form/div[4]/div/div/span/div/button").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='root']/div/section/header/div/div[2]/ul/li[12]").click()

# 得到源代码
doc = driver.page_source
emails = re.findall(r'[\w]+@[\w\.-]+',doc)
# 打印页面包含的邮箱地址
for eamil in emails:
    print(eamil)

# driver.find_element_by_class_name("ant-menu-item menu_item_twodom ant-menu-item-selected").click()
# 后退页面
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)

# 刷新页面
try:
    driver.refresh()
    print("刷新了下")
except Exception as e:
    print("刷新失败了")

# 退出重新登录
"""time.sleep(3)
driver.find_element_by_xpath(".//*[@id='item_0$Menu']/li").click()
driver.find_element_by_xpath(".//*[@id='root']/div/section/main/div/form/div[4]/div/div/span/div/button").click()
error_msg = driver.find_element_by_xpath(".//*[@id='root']/div/section/main/div/form/div[1]/div/div/div").text
try:
    assert error_msg==u"请填写用户名"
    print("test pass")
except Exception as e:
    print("test fail")"""


# 打印网址
print(driver.current_url)
# 打印标题
print(driver.title)
# 新开一个tab页面    导入keys方法实现ctrl+t快捷操作
ele=driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL+"t")
print(ele)

# 全选文字/ctrl+a操作
ele1=driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL+"a")
print(ele1)

# 设置浏览器页面大小
driver.set_window_size(800,400)
time.sleep(3)
print(driver.get_window_size())
driver.quit()