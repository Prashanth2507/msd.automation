from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from libraryfiles.locators import HomePageLocators, YooxHomePageLocators, RecommendationPopUpLocators

import requests

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        
class HomePage(BasePage):
    def clickStyleitwith(self):
        try:
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(HomePageLocators.wImg_Stylewithit))
            actions = ActionChains(self.driver)
            actions.click(self.driver.find_element(*HomePageLocators.wImg_Stylewithit)).perform()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RecommendationPopUpLocators.wE_PopUpWrapper))
        except Exception:
            print("Error occurred while clicking Style it with button. Error: " + str(Exception))
        
    #this method validates the source & text of all the 'Style it with'buttons in the page
    #also verifies if the x - position of style it button matches that of product title element(tag-div)
    def validateStyleitwith(self):
        try:
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(HomePageLocators.wImg_Stylewithit))
            count_of_products = len(self.driver.find_elements_by_xpath("//div[@id='Collection']/ul[@class='grid grid--uniform grid--view-items']/li"))
    
            for counter in range(0,count_of_products):
                print("Validation of Style it with button #: " + str(counter + 1))
                wE_style = self.driver.find_element_by_xpath("//div[@id='Collection']/ul[@class='grid grid--uniform grid--view-items']/li[" + str(counter+1) + "]/div/div/img")
                image_text = wE_style.get_attribute("alt")
                image_source = wE_style.get_attribute("src")
                
                wE_producttitle = self.driver.find_element_by_xpath("//div[@id='Collection']/ul[@class='grid grid--uniform grid--view-items']/li[" + str(counter+1) + "]/div/div[@class='h4 grid-view-item__title product-card__title']")
                if image_text == "Style it with" and image_source == "https://s3.amazonaws.com/vuedotai/images/button-styles/vuecomm/style1.png": 
                    print("Text and source of Style it with image is verified successfully")
                else:
                    print("Text and source of Style it with image is verified and there seems to be an issue.")
                    
                if wE_style.location.get('x') == wE_producttitle.location.get('x'):
                    print("Style it with button is aligned properly with the product")
                else:
                    print("Style it with button is NOT aligned properly with the product")
        except Exception:
            print("Error occurred while validating style it with buttons. Error: " + str(Exception))
    
    def fetchProductNameitem3(self):
        try:
            return self.driver.find_element(*HomePageLocators.wE_ItemName_3).get_attribute("text")
        except Exception:
            print("Error occurred while fetching the product name. Error: " + str(Exception))

class RecommendationPopUpPage(BasePage):
    def fetchMainProductName(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RecommendationPopUpLocators.wE_PopUpWrapper))
            return self.driver.find_element(*RecommendationPopUpLocators.wE_MainProductText).get_attribute("text")
        except Exception:
            print("Error occurred while fetching main product name. Error: " + str(Exception))
            
    # This method prints the y position of all the products in recommendation pop up
    def validateproductsposition(self):
        try:
            self.submethod_printproductverticalposition(0, 4)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RecommendationPopUpLocators().wE_NextArrow)).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(RecommendationPopUpLocators().wE_ProductItem_5))
            self.submethod_printproductverticalposition(4, 8)
        except Exception:
            print("Error occurred while validating products position. Error: " + str(Exception))
            
    #reusable function
    def submethod_printproductverticalposition(self,fro,to):
        try:
            for counter in range(fro,to):
                position = self.driver.find_element_by_xpath("//div[@data-item-id='occasion_" + str(counter) + "']/div/div[@class='vue-carousel-slide-item-card']").location.get('y')
                print("Product # " + str(counter+1) + " is positioned at " + str(position) + " vertically.")
        except Exception:
            print("Error occurred while printing products vertical position. Error: " + str(Exception))
            
    #This method sends request to the href attribute of each product and prints the status code
    def validateCarousel(self):
        try:
            print(self.driver.find_element_by_xpath("//div[@class='vue-popup-heading vue-font-bold' and text()='Similar Products']").is_displayed())
            print("Validation of requests when navigated to each product in recommendation pop up")
            self.submethod_sendhttprequests(0, 4)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RecommendationPopUpLocators().wE_NextArrow)).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(RecommendationPopUpLocators().wE_ProductItem_5))
            self.submethod_sendhttprequests(4, 8)
        except Exception:
            print("Error occurred while validating carousel. Error: " + str(Exception))    
        
    #resuable function
    def submethod_sendhttprequests(self,fro,to):
        try:
            for counter in range(fro,to):
                url = self.driver.find_element_by_xpath("//div[@data-item-id='occasion_" + str(counter) + "']//a").get_attribute("href")
                print("Status code on sending the endpoint of product " + str(counter+1) + " is " + str(requests.head(url).status_code))        
        except:
            print("Error occurred while validating requests. Error: " + str(Exception))

    #This method validates the href attribute of the product with the page url once the product is clicked
    def validateProductDisplay(self):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(RecommendationPopUpLocators().wE_ProductItem_1))
            expected_pageurl = element.get_attribute('href')
            element.click()
            WebDriverWait(self.driver, 30).until(EC.new_window_is_opened)
            WebDriverWait(self.driver, 30).until(EC.number_of_windows_to_be(2))
            we_windows = self.driver.window_handles
            self.driver.switch_to_window(we_windows[1])
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(YooxHomePageLocators.wE_Logo))
            
            if expected_pageurl in self.driver.current_url:
                print("Page navigation is successful. URL matches with the expected")
            else:
                print("User is navigated to different page. Incorrect URL") 
        except Exception:
            print("Error occurred while validating the products displayed. Error: " + str(Exception))