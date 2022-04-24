The purpose of this repository is to document the code I used to scrape all of the problem names and solutions from the [HDLBits website](https://hdlbits.01xz.net/wiki/Main_Page). That I then published in the following repository:

* https://github.com/trevortaulien/HDLBits_Solutions

The script uses the [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) in combination with [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to collect all of the HDL that I have written. It outputs all of the HDL problems into their own .v file titled the problem name and number. The script works by logging into your account and then going through each problem one by one scraping your HDL. The script was built to work with the Firefox browser.
 
