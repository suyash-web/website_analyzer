*** Settings ***
Documentation     Website Analyzer
Library           RPA.Browser.Selenium
Library           RPA.HTTP
Library           ShopifyAnalizer.py
Library           WordDoc.py
Library           GetFiles.py
Library           UploadFiles.py

*** Variables ***
${URL}=           https://www.ggbexhaust.com/
${NUM_IMAGES}=    0

*** Task ***
Open Browser
    [Documentation]    Opening the browser
    Open Available Browser    https://gtmetrix.com/
    Input Text    xpath://input[@name="url"]    ${URL}
    Click Button    Test your site
    Wait Until Page Contains Element    xpath://div[@class="report-performance clear"]    timeout=120

Take Screenshot
    [Documentation]    None
    Screenshot    xpath://div[@class="report-scores"]    ${CURDIR}${/}output${/}Gtmetrix${/}screenshot1.png
    BuiltIn.Sleep    2
    Screenshot    xpath://div[@class="report-page-details"]    ${CURDIR}${/}output${/}Gtmetrix${/}screenshot2.png
    BuiltIn.Sleep    2
    [Teardown]    Close Browser

Shopify Analyze website
    [Documentation]    Analyze website on shopify analyzer
    # ${url}=    Convert To String    ${URL}
    # Analyze Website    ${url}
    # BuiltIn.Sleep    4
    # [Teardown]    Close Browser
    ${var}=    Check For Images
    IF    ${var} == ${NUM_IMAGES}
        Create Document 1    ${URL}
    ELSE
        Upload And Show Saved Bits
        Create Document 2    ${URL}
    END

*** Keywords ***
Check For Images
    [Documentation]    Checking for oversized images
    ${num}=    Analyze Website    ${URL}
    [Return]    ${num}

Get Images
    [Documentation]    Getting number of oversized images
    ${img}=    Get Files
    [Return]    ${img}
