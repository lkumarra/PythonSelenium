[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8fa910a99a7a496a8054fed2a1a8a9a4)](https://www.codacy.com/manual/lkumarra/PythonSelenium?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lkumarra/PythonSelenium&amp;utm_campaign=Badge_Grade)
# To Run the Test Cases Following Dependencies are needed.
1. **pip install selenium(Selenium Dependency).**
2. **pip install pytest(pytest Dependency).**
3. **pip install selenium-page-factory( Page Factory Depedencies).**
4. **pip install 	webdriver-manager(Webdriver Manager Dependency).**
5. **pip install pytest-html(Html Report Generate Dependency).**
6. **pip install python-jenkins(To Trigger The Build Using Python).**

# Test Cases can be executed in following ways.
1. **By running ruuner.py and Clicking on start button.**
2. **By Running SeleniumExecutable.exe.**
3. **By Running TestRunner.exe which will also install dependencies before Running it will be  useful in running tests for the first time.**
	
# Jenkins Build can also Triggred Using Following Steps:
1.**Provide the Jenkins Details in Jenkins Utils and Jenkins Runner Package**
2.**Run jenkins_runner.py and click on start button to start execution.**
3.**Click on stop to stop the execution.**
	
# The Framework Contains 3 Reporting:
1. **Html Reporting**
2. **Junit Xml Reporting**
3. **Allure Reporting**

# All the test_reports are generated in test_report package

# To generate all 3 reports command can be found in RunnerAllureReport.bat file.

