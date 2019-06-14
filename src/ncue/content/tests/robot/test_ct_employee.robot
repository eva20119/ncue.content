# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ncue.content -t test_employee.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ncue.content.testing.NCUE_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ncue/content/tests/robot/test_employee.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Employee
  Given a logged-in site administrator
    and an add Employee form
   When I type 'My Employee' into the title field
    and I submit the form
   Then a Employee with the title 'My Employee' has been created

Scenario: As a site administrator I can view a Employee
  Given a logged-in site administrator
    and a Employee 'My Employee'
   When I go to the Employee view
   Then I can see the Employee title 'My Employee'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Employee form
  Go To  ${PLONE_URL}/++add++Employee

a Employee 'My Employee'
  Create content  type=Employee  id=my-employee  title=My Employee

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Employee view
  Go To  ${PLONE_URL}/my-employee
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Employee with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Employee title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
