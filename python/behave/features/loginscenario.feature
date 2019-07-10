# Created by mprakash at 09/07/2019
Feature: Login scenarios with correct and incorrect credentials

  Scenario Outline: Login Scenarios with correct and incorrect credentials
    Given User with <logintype> credentials
    When the user enters <username> username
    And the user enters <password> password
    And clicks on Login button
    Then the user is presented with  <message> based on <logintype>

  Examples: credentials
    | username            |   password   |    logintype               |      message                |
    | test@drugdev.com    | supers3cret  |  Correct Credentials       | Welcome Dr I Test           |
    | incorrect@user.com  | incorrectpwd | Incorrect Credentials      | Credentials are incorrect   |
    | incorrect@user.com  | undefined    |      No password           | Credentials are incorrect   |
    | undefined           | incorrectpwd |      No username           | Credentials are incorrect   |