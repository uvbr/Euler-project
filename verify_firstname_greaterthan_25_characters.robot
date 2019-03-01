*** Settings ***
Library        BuiltIn
Library        helloworld    WITH NAME    kjkk

*** Variables ***

*** Test Cases ***
verify_firstname_greaterthan_25_characters
    ${x}    Set Variable    1
    : For    ${i}    IN RANGE    0    ${x}
    \    Log    print 0 to 1    level=INFO
    \    Log    end for    level=INFO
    &{dict1}    Create Dictionary    name=siva    project=sapphire
    ${x}    Evaluate    1*2
    ${y}    Evaluate    int(${dict1})*int(${x})
    ${sas}    kjkk.tbb_one    sas    sas    saas
    ${1}    kjkk.tbb_one    1    2    ss3
    ${fhgf}    kjkk.tbb_one    fhgf    ffh    fhfh
    ${n1}    Set Variable    1
    ${n1}    Set Variable    5
    ${gjhghj}    kjkk.tbb_one    gjhghj    gjg    gjhgj
    ${hkhk}    kjkk.tbb_one    hkhk    hj    g
    Log    print ${y}    level=WARN
    ${hkhk}    kjkk.tbb_one
