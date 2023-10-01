# Validator Testing

## HTML

Validator used - [W3 Markup Validator](https://validator.w3.org/). All pages were tested. Initially 2 errors were found due to button
tag within a tag (closing button on room & booking details) and p tag within span (search bar tooltip). After fixing these home page is rendering no errors.

![HTML Validator](docs/testing/html_val.png)

There are errors showing on forms pages (Create Room and New Booking) related to the form implementation. Validator also highlights errors in the Font Awesome code as rendered in the Elements of Chrome Developer Tools. Hopefully, this is acceptable, as it's not my own custom HTML. The code had to be copied from Elements section of Chrome Dev Tools and validated as text direct input due to the use of templating.

![HTML form error](docs/readme_images/html_validator_form_error.png)

## CSS

Custom CSS code rendered no errors in the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/).

![CSS validation](docs/readme_images/css_validation.png)

## Python
Initially small errors like trailing whitespaces, no new line at end of document were detected and corrected. All python files with the exception of settings.py are showing no errors.
In settings.py the django auto generated code for AUTH_PASSWORD_VALIDATORS and also cloudinary storage path are showing up as lines too long. I could not find a way to split these lines but since they were auto generated and not my own custom code, I hope this is acceptable.

![Python validation](docs/readme_images/pep8.png)

# Accessibility

Care was taken to ensure sufficient level of accessibility and user friendliness by using semantic HTML elements, aria-labels, appropriate color contrast, different hover and active states. Initial test via [Wave](https://wave.webaim.org/) returned an error with Search button (navbar) contrast, this was corrected by applying a lighter background. Also a warning was displayed about underline on carousel slides, where active class was applied - underline has been removed from carousel active to correct this.

![Accessibility](docs/readme_images/accessibility.png)

# Responsiveness

All pages were checked for responsiveness on different sizes inspected via Chrome Developer tools. Designed layout behaviour was ensured by adding some media queries, where tests shown that elements were overlapping or too cluttered.

# Lighthouse Report

Initial results of the report showed poorer performance than desired. This has been rectified by applying the below guidelines from the report:

- further compression of images
- preloading background image
- moving fontawesome script tags from head to the bottom of body element

To improve SEO score, link was added to the site logo thanks to another suggestion from the report.

![Lighthouse](docs/readme_images/lighthouse.png)

# Bugs

## Solved:
- Stripe webhooks not working - SECRET expired, problem solved after updating the key
- Broken link after user pressed Confirm button on the page displayed from email confirmation link - additional Allauth URL settings added to settings.py to ensure user is logged in after email verification
- djrichtextfield in forms showing HTML tags on website preview - fields were replaced with CharFields

## Unsolved due to deadline:
- search functionality returns double results
- multiselect widget not working on StoryForm (same settings applied as for ProductForm, where it is working)

Back to [Readme](README.md)

