**INSTALLATION**

`pip install pytest-allure-adaptor`


COMMON ISSUES

 * If  “\Java\jre1.8.0_71 was unexpected at this time”  error is encountered:

    Ensure Java is installed on the path without spaces on Windows.

 * Set a variable **%ALLURE_HOME%** and add in **%ALLURE_HOME%\bin** into %PATH% variable.

     The required version of Allure CommandLine (with ‘bin’ folder) can be found here: [Allure CommandLine](https://github.com/allure-framework/allure-core/releases/tag/allure-core-1.4.23.HOTFIX1)



**Selene + Pytest + Allure Reporting example project**


**TO RUN TESTS**

Open the console, navigate to the folder with the tests, run following command:

`python -m pytest todomvc_test.py -s --alluredir build\reports`

To make allure-report run:

`allure.bat generate -o build\reports\ build\reports\`

In the folder ***build\reports*** you`ll find the file ***index.html***, that has to be opened in a browser

[Reports example](https://bitbucket.org/K_elly/selene_todomvc/src/5114fb05ce1eb4fcd974aa8c1cb28a5a368fb703/reports.zip?at=master&fileviewer=file-view-default)"# todomvctest_selene" 
