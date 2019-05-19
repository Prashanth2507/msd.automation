import unittest
from selenium import webdriver
from libraryfiles import businessactions

class PythonMadStreetDen(unittest.TestCase):

    def setUp(self):
        print("Executing test case")
        print("----------------------------------------------------------------------")
        self.driver = webdriver.Chrome(executable_path='C:\python\chromedriver')
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(45)
        self.driver.get("https://madstreetden.myshopify.com/collections/top-wear")
        self.driver.maximize_window()
      
    def test_1validate_styleitwith(self):
        print("This test is to validate if Style it with buttons are rendered properly")
        print("----------------------------------------------------------------------")
        main_page = businessactions.HomePage(self.driver)
        #Validates the source and text of all the 'Style it with' images in the page
        main_page.validateStyleitwith() 
        print("----------------------------------------------------------------------")
            
    def test_2validate_recommendationpopup(self):
        print("This test is to validate the recommendation pop up is rendered correctly")
        print("----------------------------------------------------------------------")
        main_page = businessactions.HomePage(self.driver)
        #Fetching the third product name to see if it matches with the main product in recommendation pop up 
        product_name = main_page.fetchProductNameitem3() 
        main_page.clickStyleitwith() #Click on the third 'Style it with' button
        popup = businessactions.RecommendationPopUpPage(self.driver)
        actual_product_name = popup.fetchMainProductName()
        if product_name == actual_product_name : print("The product that I clicked on the previous screen is getting displayed in popup as expected") 
        else : print("Seems to be an issue with pop up") 
        popup.validateproductsposition()
        print("----------------------------------------------------------------------")

    def test_3validate_carousel(self):
        print("This test is to validate the products in carousel")
        print("----------------------------------------------------------------------")
        main_page = businessactions.HomePage(self.driver)
        main_page.clickStyleitwith()
        popup = businessactions.RecommendationPopUpPage(self.driver)
        #Validation of products in carousel
        popup.validateCarousel()
        print("----------------------------------------------------------------------")
    
    def test_4navigation_yoox(self):
        print("This test is to validate if the product display page opens in a new tab")
        print("----------------------------------------------------------------------")
        main_page = businessactions.HomePage(self.driver)
        main_page.clickStyleitwith()
        popup = businessactions.RecommendationPopUpPage(self.driver)        
        #Navigation to yoox.com - product display -
        popup.validateProductDisplay()
        
    def tearDown(self):
        print("Test execution completed") 
        
if __name__ == "__main__":
    unittest.main()