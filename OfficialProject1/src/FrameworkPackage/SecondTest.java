package FrameworkPackage;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class SecondTest extends FirstTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.setProperty("webdriver.gecko.driver", "C:\\Users\\Charles\\Desktop\\java stuff\\geckodriver-v0.29.0-win64\\geckodriver.exe");
		WebDriver driver = new FirefoxDriver();
		
		driver.quit();
	}

}
