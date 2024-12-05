from dotenv import load_dotenv
import os
import pytest
import sys
sys.path.append('C:/Users/Ido/Documents/ForcePoint/Ultimateqa')

from playwright.sync_api import Page
from Ultimateqa.pages.sub_page_buttons import SubPageButtons
from Ultimateqa.pages.sub_page_social_media import SubPageSocialMedia
from Ultimateqa.pages.sub_page_forms import SubPageForms
import Ultimateqa.tests.consts as consts


def test_count_buttons(page: Page, goto):
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    goto(base_url)
    sub_page_buttons = SubPageButtons(page)

    count_of_buttons = sub_page_buttons.count_buttons()
    assert count_of_buttons == consts.NUN_OF_BUTTONS_TO_FIND, \
        f"Found: {count_of_buttons} buttons, expected: {consts.NUN_OF_BUTTONS_TO_FIND}"


def test_verify_href_link(page: Page, goto):
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    goto(base_url)
    sub_page_social_media = SubPageSocialMedia(page)

    facebook_buttons = sub_page_social_media.section.query_selector_all('a[title="Follow on Facebook"]')

    for button in facebook_buttons:
        href = button.get_attribute('href')
        assert href == consts.SOCIAL_MEDIA_LINK, f"href is: {href}, expected: {consts.SOCIAL_MEDIA_LINK} "

@pytest.mark.parametrize('name, email, message, exercise_result, message_after_submit', [
    ('Haim Moshe', 'haim.moshe@gmail.com', 'I am singer', None, 'Thanks for contacting us'),
    ('Haim Cohen', 'adam@gmail.com', 'I am Adam', None, 'Thanks for contacting us'),
    ('Asaf Levi', 'asaf@gmail.com', 'I am Asaf', '0', 'You entered the wrong number in captcha.'),
])
def test_forms(page: Page, goto, name, email, message, exercise_result, message_after_submit):
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    goto(base_url)
    sub_page_social_forms = SubPageForms(page)

    sub_page_social_forms.set_name(name)
    sub_page_social_forms.set_email(email)
    sub_page_social_forms.set_message(message)

    if exercise_result != '0':
        exercise_result = sub_page_social_forms.extract_and_calculate_result()

    sub_page_social_forms.set_result(result=str(exercise_result))
    sub_page_social_forms.click_submit()

    if exercise_result != '0':
        response_message = sub_page_social_forms.get_submit_response()
    else:
        response_message = sub_page_social_forms.get_submit_fail_response()

    assert response_message == message_after_submit


