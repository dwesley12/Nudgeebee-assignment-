# Nudgeebee-assignment-

Test Planning 
What would I test and why ?
1.	Registration – Valid and Invalid inputs, duplicate accounts, email, Passwords 
Why – First entry point for every user and impact highly on user experience
Risk – Invalid data handling , email verification failures, duplicate acconts

2.	Login – correct and incorrect inputs like email and password, multiple login 
Why – Gives core access control to user
Risk – authentication failures, session handling failures

3.	Profile Update – Edit fields, validation, boundary value analysis
Why – It ensures data quality and integrity 
Risk – data integrity issues, validation failures 

4.	Password reset – correct and incorrect input, old password input, reset success or failure
Why – It is critical recovery path for every user
Risk – OTP issues , weak password policy  

5.	Account deletion – Success and unsuccessful deletion, login after deletion, data removal 
Why – security and compliance 
Risk- unauthorized deletion, incomplete data deletion, 

Test Prioritization
High priority 
1.	Registration, 
2.	login, 
3.	password reset
4.	Account deletion 
Medium priority 
1.	profile update 
2.	session management, UI feedback 
3.	validation and negative scenarios  
Low priority 
1.	Cosmetic changes 
2.	Multiple device compatibility 


What to automate vs manual 

Automate
1.	Regression suite like login, registration, account deletion, form field validation
Why – automate what is stable and repetative, saves time, quick feedbacks 
Manual 
1.	UI Validation, Exploratory testing, edge cases and negative scenarios, rare scenarios to break the flow 
Why – human touch and human judgement is necessary because it helps uncover unexpected issues

Bug Report   
Mistake in bug report 
1.	Unclear title 
2.	Unclear description 
3.	No expected and actual clarity 
4.	Multiple bugs mixed together 
Rewritten bug report
1.	Checkout fails with error after adding items to cart 
TITLE - Checkout failure with error after adding item to cart 	

Description – user is unable to procced with checkout after adding items to cart. Error message is displayed and checkout does not complete 

Steps to reproduce 
1.	Lopgin with valid credentials 
2.	Add 2 items to cart 
3.	Navigate to cart page 
4.	Click on checkout 
Expected result – user should be redirected to payment page successfully 
Actual result – error message is displayed and check out process stops 
Severity – High 
Environment
1.Browser – chrome 
2. OS – windows 12
3. Device laptop


2.	Incorrect price display in the cart
TITLE – Price mismatch in product page and checkout page 

Description – the price is displayed in cart page mismatched in product page 

Steps to reproduce 
1.	Login in valid credential 
2.	Go to product page
3.	Add a product to cart 
4.	Navigate to product page 
Expected result – price should remain consistent across pages 
Actual result – price is inconsistent across pages 
Severity – critical 
 Environment
1.Browser – chrome 
2. OS – windows 12
3. Device laptop

3.	Product filter not working correctly 
TITLE – Product filters is not working on product listing page inconsistent behaviour

Description – Filters sometimes do not apply or update  result correctly 

Steps to reproduce 
1.	Login with valid credentials
2.	Navigate to product listing page 
3.	Apply any filter`
Expected result – Filtered result should update consistently
Actual result – Filters sometimes do not apply, inconsistent behaviour 
Severity – medium 
Environment
1.Browser – chrome 
2. OS – windows 12
3. Device laptop


4. Mobile UI Layout Issue (Needs Validation)
Title - UI layout appears broken on mobile devices (needs confirmation)
Description - Potential UI issue on mobile devices where layout appears broken.
Steps to Reproduce
	1.Open website on different devices 
Expected Result - Responsive layout should render correctly.
Actual Result - UI appears misaligned or broken.
Severity – Medium/low



 

