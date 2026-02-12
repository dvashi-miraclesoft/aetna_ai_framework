Feature: Healthcare Virtual Assistant UI
  As an Aetna member
  I want to ask the virtual assistant about compliance
  So that I can understand my privacy rights

  Scenario: User asks the bot about HIPAA
    Given the user is on the healthcare portal
    When the user sends the prompt "HIPAA"
    Then the AI response should contain "Health Insurance Portability and Accountability Act"