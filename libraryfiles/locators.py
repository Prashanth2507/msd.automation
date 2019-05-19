from selenium.webdriver.common.by import By

class HomePageLocators(object):
    wImg_Stylewithit = (By.XPATH, "//img[@alt='Style it with']")
    wE_ItemName_3 = (By.XPATH, "//div[@id='Collection']/ul[@class='grid grid--uniform grid--view-items']/li[3]/div/a/span")
    
class RecommendationPopUpLocators(object):
    wLbl_SimilarProducts = (By.XPATH, "//div[@class='vue-popup-heading vue-font-bold' and text()='Similar Products']")
    wE_PopUpWrapper = (By.XPATH,"//div[@class='vue-popup-meta-data-wrapper']")
    wE_MainProductText = (By.XPATH,"//div[@class='vue-popup-meta-data-wrapper']//div[@class='meta-card-prod-title']/div")
    wE_NextArrow = (By.XPATH,"//a[@class='vue-next-nav-wrapper']")
    wE_ProductItem_5 = (By.XPATH,"//div[@data-item-id='occasion_4']//a")
    wE_ProductItem_1 = (By.XPATH,"//div[@data-item-id='occasion_0']//a")
        
class YooxHomePageLocators(object):
    wE_Logo = (By.XPATH,"//div[@id='logo']")