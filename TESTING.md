## mealmotion - Testing

![Image showing mealmotion as displayed on multiple screen sizes](static/media/README/)

[Link to deployed mealmotion Website](https://meal-motion-958ec306f33c.herokuapp.com/)

## Contents
**[Automated Testing](#automated-testing)**
* [W3C Validator](#wc3-html--css-validator)
* [Python Validator](#python-validator)
* [Django Testing](#django-testing)


**[Performance Testing ( Wave & Lighthouse )](#performance-testing-lighthouse)**
* [Desktop](#desktop)
* [Mobile](#mobile)

**[Performance Results](#performance-results)**

**[Manual Testing](#manual-testing)**
* [Testing User Stories](#testing-user-stories)

**[Full Testing](#full-testing)**
* [Devices Tested On](#devices-tested-on)
* [Page Feature Testing](#page-feature-testing)

**[Solved & Known Bugs ](#solved--known-bugs)**

---

## Automated Testing
### WC3 HTML & CSS Validator
The W3C Validator was used to check and validate the HTML and CSS for all pages of the website. Validation was performed by direct input page’s web link into the tool.<br><br>

**HTML Validator**
* [Home Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstrength-stack-e65fe8f9116b.herokuapp.com%2F) - No errors or warnings.
* [Index Page]() - No errors or warnings.
* [Add & Edit Products]() - No errors or warnings.
* [Recipes]() - No errors or warnings.
* [Recipe Details]() - No errors or warnings.
* [Profile]() - No errors or warnings.
* [Shopping Bag]() - No errors or warnings.
* [Checkout]() - No errors or warnings.
* [Checkout Success]() - No errors or warnings.
* [Registration]() - No errors or warnings.
* [Login]() - No errors or warnings.
* [Logout]() - No errors or warnings.
* [404 Error Page]() - There are no other errors; the validator simply identified the 404 page.
* [500 Error Page]() - No errors or warnings.<br>


**CSS Validator**<br>
I just submitted the css directly through the WC3 CSS Validator.
* [base.css Validator](https://jigsaw.w3.org/css-validator/validator) - No Error Found.
* [checkout.css Validator](https://jigsaw.w3.org/css-validator/validator) - No Error Found
* [Internal CSS in the profile.html](https://jigsaw.w3.org/css-validator/validator) - No Error Found

### Python Validator
To validate all my Python code, I used the Code Institute [Python Linter](https://pep8ci.herokuapp.com/).<br>
All was clear with no errors found. Below, I’ve provided Python validations for 4 of my more detailed apps as examples.<br><br>

**"products" App :**

* [admin.py](static/media/TESTING/admin-products-PL.png)
* [forms.py](static/media/TESTING/forms-products-PL.png)
* [models.py](static/media/TESTING/models-products-PL.png)
* [urls.py](static/media/TESTING/urls-products-PL.png)
* [views.py](static/media/TESTING/views-products-PL.png) 

**"bag" App :**

* [context.py](static/media/TESTING/context-bag-PL.png)
* [views.py](static/media/TESTING/views-bag-PL.png)

**"checkout" App :**

* [admin.py](static/media/TESTING/admin-check-PL.png)
* [forms.py](static/media/TESTING/forms-check-PL.png)
* [models.py](static/media/TESTING/models-check-PL.png)
* [signals.py](static/media/TESTING/signals-check-PL.png)
* [urls.py](static/media/TESTING/urls-check-PL.png)
* [views.py](static/media/TESTING/views-check-PL.png)
* [webhook_handler.py](static/media/TESTING/webhand-check-PL.png)
* [webhooks.py](static/media/TESTING/webhook-check-PL.png)

**"profiles" App :**

* [forms.py](static/media/TESTING/forms-profile-PL.png)
* [models.py](static/media/TESTING/models-profile-PL.png)
* [urls.py](static/media/TESTING/urls-profile-PL.png)
* [views.py](static/media/TESTING/views-profile-PL.png)

### Django Testing
xxx
# Performance Testing ( Wave & Lighthouse )
**Wave Contrast Checker**

I used the WAVE Contrast Checker to verify if my webpages passed accessibility standards.
All pages pass the color contrast checker, ensuring accessibility and readability for all users.
I made sure text and background colors work together.

## Performance Results 
I used Lighthouse on ChromeDevTools to test perfomance of my website on desktop - page by page.
<br>The results are as shown below.

### Desktop
* [Home Page](staticfiles/images/TESTING%20images/home-%20lighthouse.png)
* [Index Page](staticfiles/images/TESTING%20images/index-%20lighthouse.png)
* [About Page](staticfiles/images/TESTING%20images/about-lighthouse.png)
* [Login Page](staticfiles/images/TESTING%20images/login-%20lighthouse.png)
* [Registration Page](staticfiles/images/TESTING%20images/signup-%20lighthouse.png)
* [Profile Page](staticfiles/images/TESTING%20images/profile%20-%20lighthouse.png)
* [Update Profile Page](staticfiles/images/TESTING%20images/profile-edit%20-%20lighthouse.png)
* [Dashboard](staticfiles/images/TESTING%20images/dash-%20lighthouse.png)
* [Update Workout Page](staticfiles/images/TESTING%20images/edit-workout-%20lighthouse.png)
* [Create Workout Page](staticfiles/images/TESTING%20images/create-workout-%20lighthouse.png)
* [Workout Details Page](staticfiles/images/TESTING%20images/view-workout-%20lighthouse.png)
* [Update Exercise Page](staticfiles/images/TESTING%20images/edit-ex-%20lighthouse.png)
* [Create Exercise Page](staticfiles/images/TESTING%20images/create-ex-%20lighthouse.png)
* [Logout Page](staticfiles/images/TESTING%20images/logout%20-%20lighthouse.png)
* [404 Error Page](staticfiles/images/TESTING%20images/404-lighthouse.png)
* [500 Error Page](staticfiles/images/TESTING%20images/500-lighthouse.png)

**To summarise :**  
Performance scores for the Index, Home, and 404 pages were some of the lowest at 73, the lowest being the 500 page at 71, which is below the desired level but passable.
I suspect that Chrome extensions may have impacted these results. 
Aside from that, most performance metrics were in the green.

SEO only dropped into the orange range on the 404 page.

Accessibility scores ranged from approximately 85 to the 90s.

Best Practices consistently scored 100, with only a few instances ranging between 90-100.

## Manual Testing
### Testing User Stories

| **User Story** | **How are they achieved?** | **Image** |
| :--- | :--- | :--- |
|`First Time Visitor`<br>" As a first-time visitor, I can register and log in using my email and password , so that I can securely access my account and track my workouts "|The website features full authentication, allowing users to create an account using a valid username and password.<br><br>Users can access their accounts anytime by logging in and viewing their personal dashboard.|![Login](staticfiles/images/README%20images/LoginPage.png) ![Register](staticfiles/images/README%20images/RegistrationPage.png)|
| `Returning Visitor`<br>" As a returning visitor, I can see a list of my previous workouts on the dashboard when I log in so that I can quickly access and review past sessions." |Upon logging in, you can access your dashboard through the welcome page.<br><br>After navigating to the dashboard, the user is presented with a list of previous workouts, if any exist.|![Welcome Page](staticfiles/images/README%20images/Index.png)<br>![Dashbboard](staticfiles/images/README%20images/Dash.png) |
| `Returning Visitor`<br>" As a returning visitor, I can create a new workout entry so that I can log my routine and begin tracking my progress." |The Create Workout button on the dashboard directs the user to a form where they can enter all relevant information. |![Create Workout Form](staticfiles/images/README%20images/create%20workout.png)|
| `Returning Visitor`<br>" As a returning visitor, I can view the full details of a selected workout so that I can review the exercises, sets, and reps involved" |Users can click the View Details button on any workout card they have created to see the full details of the exercises and other information involved.|![View Workout](staticfiles/images/README%20images/view.png)|
| `Returning Visitor`<br>" As a returning visitor, I can update or delete workout entries so that I can keep my records accurate and remove outdated information." |Each workout and exercise in the includes Update and Delete buttons.<br><br>The user can click the Update button to open a form where they can modify the details and save the changes.<br><br>Clicking the Delete button will prompt a confirmation alert to ensure the user wants to proceed.|![Edit](staticfiles/images/README%20images/edit%20exercise.png)<br><br>![Delete](staticfiles/images/README%20images/delete%20alert.png)|
|`Frequent Visitor`<br> "As a frequent visitor, I can see a visual representation of my workout history so that I can easily track my progress over time."|**This feature was not implemented due to time constraints, but the plan was to use Chart.js for its development in future.**| No Image |
|`Site Admin`<br> "As site admin I can create, read, update, and delete site information so that I can manage site content effectively.|Logged-in admins can create, view, update existing posts and delete them.| ![Admin](staticfiles/images/README%20images/admin.png) |
## Full Testing
### Devices Tested On

I tested the website across the following devices and browsers, and it displayed correctly on all of them.<br>The site was fully responsive and loaded properly in each case.

* **Laptop**
    * Lenovo Legion 5 15.6 in
---
* **Mobile**
    * Iphone 14 SE - Safari
    * Iphone 12
---
* **Browser**
    * Google Chrome
    * Microsoft Edge
    * Safari
    * Firefox

### Page Feature Testing
**Logged Out**

`Home/Index Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Mealmotion Title | Link redirects the user back to the Home page | Title Clicked | Redirected to Homepage | Pass |
| Home Link | Link directs the user to the Home Page | Home Link Clicked | Redirected to Home Page | Pass |
| Membership Link | Link directs the user to the Registration| Membership Link Clicked |Redirected to Registration Page| Pass |
| Profile Icon Link | Link directs the user to the Login Page | Login Link Clicked | Redirected to Login Page| Pass |
| Shop & Recipe Catalogue buttons | Link directs the Shop and Recipes Page respectively| Clicked on button | Redirected to Registration Page | Pass |
| All buttons hover effect| Button color changes on hover| Hover over button | Button color changes on hover | Pass |
| Social Media Icons Footer | Link directs the user to facebook , instagram , X or Threads , depending on which icon clicked.| Click social media Icon | Redirected to the home page of social platform clicked. | Pass |
---
---
`Login & Registration`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Login Functionality| Sign in button redirects user to thier account if correct details entered | Entered correct username and password | User redirected to thier accont Home Page | Pass |
| Registration Functionality| Register button redirects user to thier account if correct details entered | Created a valid username and password | User redirected to thier accont Home Page | Pass |
| Username Field | Message prompting that username Field must not be empty | Field not filled out | User Presented with message , "This field is required." | Pass |
| Password Field|Message prompting that password Field must not be empty | Field not filled out | User Presented with a small popup "Please Fill In This Field." | Pass |
| Incorrect Entry of both Fields | Message prompting that username and Password must be correct | Entered correct username and password|User Presented with a "The username and/or password you specified are not correct."| Pass |
| Password (again)* Field | Throws error message if Passwords dont match | Unidentical password entered | User Presented with message , "You must type the same password each time."| Pass |
---
---
**Logged In**

`Index Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Dashboard Link | Link directs the user to the Dashboard | Dashboard Link Clicked | Redirected to Dashboard Page | Pass |
| Profile Link| Link directs the user to the Profile Page| Profile Link Clicked |Redirected to Profile Page| Pass |
| Signout Link | Link directs the user to the Signout Page | Signout Link Clicked | Redirected to Signout Page| Pass |
---
---
`Profile & Update Profile Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Edit Profile Button | Button directs the user to the Edit Profile Form | Button Clicked | Redirected to Edit Profile Form | Pass |
| Upload Profile Image| Clicking "Choose File" opens your file explorer, allowing you to select and upload an image.| Choose File clicked | Choose File opens the file explorer. | Pass |
| Save Button |Displays a confirmation message, and if confirmed, saves the changes. |Save button clicked | Changes saved after confirmed | Pass |
---
---
`Dashboard`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| No Workouts | On first visit to the Dashboard page after creating a new account, display a message stating no workouts are posted yet. | Dashboard Button Clicked | User Presented with message on page , "No Workouts Added yet" | Pass |
| Create New Workout Button | Button directs the user to the Create Workout Form | Button Clicked | Redirected to Create Workout Form | Pass |
| View Workout Button| Button directs the user to the Workout Details Page | Button Clicked | Redirected to Create Workout Details Page | Pass |
| Delete Workout Button|Displays a confirmation message, and if confirmed, deletes the workout. |Button Clicked | Workout Deleted | Pass |
| Edit Workout Button|Button directs the user to the Edit Workout Form |Button Clicked | Redirected to Edit Workout Form | Pass |
---
---
`Create & Update Workout Pages `
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Asterisked Fields| All these fields must be filled out or message prompted | Save Button Clicked | User Presented with message , "This field is required."| Pass |
| Save Workout Button| The button redirects the user to the Dashboard, where they can view the new workout at the top of the list. | Button Clicked | Redirects to the Dashboard, with the new workout displayed as the first item on the list. | Pass |
| Fields Prepopulated on Edit Form|Displays form with previously entered information |Button Clicked | Displays a form with the previously entered information, which can be edited.| Pass |
---
---
`Workout Details Page `
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| No Exercises | On first visit to the Workout Details page after creating a workout, display a message stating no exercises are posted yet. | New workout Created & View Workout Button Clicked | User Presented with message on page , "No Exercises Added yet ! Add New Exercises Below." | Pass |
| Add Exercise Button | Button directs the user to the Add Exercise Form | Button Clicked | Redirected to Add Exercise Form | Pass |
| Delete Exercise Button|Displays a confirmation message, and if confirmed, deletes the exercise. |Button Clicked | Exercise Deleted | Pass |
| Edit Exercise Button|Button directs the user to the Edit Exercise Form |Button Clicked | Redirected to Edit Exercise Form | Pass |
---
---
`Create & Update Exercise Pages`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Asterisked Fields| All these fields must be filled out or message prompted | Save Button Clicked | User Presented with message , "This field is required."| Pass |
| Save Exercise Button| The button redirects the user to the Workout Details, where they can view the new exercise. | Button Clicked | Redirects to the Workout Details, with the new exercise displayed on the list. | Pass |
| Fields Prepopulated on Edit Form |Displays form with previously entered information |Button Clicked | Displays a form with the previously entered information, which can be edited.| Pass |
---
---
`Logout Page`
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Sign Out Button | Sign Out button redirects user back to the home page and signs them out of thier account| Sign Out button clicked | User signed out | Pass |

# Solved & Known Bugs  
## Solved Bugs
| No | Bug | How I solved the issue |
| :--- | :--- | :--- |
| 1| Registration form not submitting , thus not creating new user account.| <br><br> method='POST' attribute missing in form. Restored this. <br><br>[Bug-1](static/media/TESTING/bugs/bug-1.png) |
| 2 | Icon misalignment [Bug-2](static/media/TESTING/bugs/bug-2.png) |Adjusted margins and font size of bag price to fix misalignment.|
| 3| On mobile /tablet screen sizes , when search bar is open it comes out of the nav container with icons that follow it<br><br>[Bug-3](static/media/TESTING/bugs/bug-3.png)| For ease I just moved the search bar above the rest of the navbar and fixed some of the css overlaps. I also removed the JS script to toggle the searchbar when you click the search icon.|

## Known Bugs 

| No | Bug | Issue |
| :--- | :--- | :--- |
| 1 | On the login page, if you refresh after receiving an invalid username or password error, the error message should disappear - but currently, it remains displayed.<br>[Login](staticfiles/images/TESTING%20images/Login%20Error.png)| X |
| 2 | The "Remember me" on the Login and Registration page box does not save account details.| X |
---
[Back to the Top](#mealmotion---testing)
