Feature: Search for pets by category

As a pet shop customer
I need to be able to search for a pet by category
So that I only see the category of pet I'm interested in buying

Scenario: Search for dogs
	Given I am on the "Home Page"
	When I set the "Category" to "dog"
	And I click the "Search" button
	Then I should see the message "Success"
	And I should see "Fide" in the results
