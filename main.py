from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import toml
import time
import pyautogui
import pyperclip

# from pywinauto import Application, Desktop
def load_config():
    return toml.load("config.toml")

def login_and_navigate(username, password):
    driver = webdriver.Chrome()  # 请确保已安装 ChromeDriver
    driver.get("https://ai.supercat.cash/openapi/kb/pushData")
    
    # 显式等待元素可见并输入用户名和密码
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
        
        # 等待并点击登录按钮
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='登录']")))
        login_button.click()  # 提交表单

        # 等待新的页面加载
        time.sleep(5)  # 等待页面加载
        
        # 可以在这里添加更多逻辑，比如验证是否成功登录
        print("登录成功，页面加载完成。")
        
        # 等待知识库按钮可点击并点击它
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='知识库']"))).click()
        print("成功点击知识库。")
        
        # 点击知识库中的特定选项
        wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{knowledge_warehouse}']"))).click()
        print(f"成功点击选项: {knowledge_warehouse}")
        
        # 点击导入数据
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='导入数据']"))).click()
        print("成功导入数据。")
        
        # 根据导入方式选择按钮
        import_options = {
            0: "直接分段",
            1: "QA 拆分",
            2: "CSV 导入",
            3: "Excel 导入"
        }
        
        selected_option = import_options.get(import_way)
        print(f"选择的导入方式: {selected_option}")
        if selected_option:
            # visible_elements = driver.find_elements(By.XPATH, "//*[not(@style='display: none;')]")
            # for elem in visible_elements:
            #     print(elem.text)
            # 使用XPath点击导入方式
            wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{selected_option}')]"))).click()
            print(f"成功点击导入方式: {selected_option}")
        else:
            print("无效的导入方式选择。")

        
        #选择文件
        time.sleep(2)  # 暂停5秒
        select_file_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'css-o4n2u0') and text()='选择文件']")))
        select_file_button.click()
        
        # 查找文件输入框并上传文件
        pyperclip.copy(file_path)
        time.sleep(2)
        pyautogui.hotkey('Ctrl', 'V')
        time.sleep(2)
        
        # 模拟按下回车键，或者点击“打开”按钮
        print("点击打开")
        pyautogui.press('enter')
        
        time.sleep(5)  # 适当调整时间，观察网页行为
        print("成功选择文件。")

        
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        driver.quit()  # 确保在最后关闭浏览器

if __name__ == "__main__":
    # with open("config.toml", "r", encoding="utf-8") as f:
    config = load_config()
    
    username = config["credentials"]["username"]
    password = config["credentials"]["password"]
    knowledge_warehouse=config["settings"]["knowledge_warehouse"]
    import_way=config["settings"]["import_way"]
    file_path = config['settings']['file_path'].replace('\\\\','\\')
    
    login_and_navigate(username, password)
