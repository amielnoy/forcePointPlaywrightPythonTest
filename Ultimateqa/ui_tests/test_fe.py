import pytest
import Ultimateqa.ui_tests.consts as consts
from Ultimateqa.ui_tests.base_test import BaseTest

class TestUI(BaseTest):

    def test_count_buttons(self):
        count_of_buttons = self.sub_page_buttons.count_buttons()
        assert count_of_buttons == consts.NUN_OF_BUTTONS_TO_FIND, \
            f"Found: {count_of_buttons} buttons, expected: {consts.NUN_OF_BUTTONS_TO_FIND}"

    def test_count_buttons_using_css(self):
        count_all_buttons_using_css = self.sub_page_buttons.all_buttons.count()
        assert count_all_buttons_using_css == consts.NUN_OF_BUTTONS_TO_FIND, \
            f"Found: {count_all_buttons_using_css} buttons, expected: {consts.NUN_OF_BUTTONS_TO_FIND}"
    #One link of facebook is not equal
    # Expected  'https://www.facebook.com/Ultimateqa1/'
    # Actual   :'https://www.facebook.com/Ultimateqa1'
    def test_verify_href_link(self):
        facebook_buttons = self.sub_page_social_media.page.query_selector_all('a[title="Follow on Facebook"]')
        for button in facebook_buttons:
            href = button.get_attribute('href')
            assert href == consts.SOCIAL_MEDIA_LINK, f"href is: {href}, expected: {consts.SOCIAL_MEDIA_LINK} "

    @pytest.mark.parametrize('name, email, message, exercise_result, message_after_submit', [
        ('Haim Moshe', 'haim.moshe@gmail.com', 'I am singer', None, 'Thanks for contacting us'),
        ('Haim Cohen', 'adam@gmail.com', 'I am Adam', None, 'Thanks for contacting us'),
        ('Asaf Levi', 'asaf@gmail.com', 'I am Asaf', '0', 'You entered the wrong number in captcha.'),
    ])
    def test_forms(self, name, email, message, exercise_result, message_after_submit):
        self.sub_page_forms.set_name(name)
        self.sub_page_forms.set_email(email)
        self.sub_page_forms.set_message(message)

        if exercise_result != '0':
            exercise_result = self.sub_page_forms.extract_and_calculate_result()

        self.sub_page_forms.set_result(result=str(exercise_result))
        self.sub_page_forms.click_submit()

        if exercise_result != '0':
            response_message = self.sub_page_forms.get_submit_response()
        else:
            response_message = self.sub_page_forms.get_submit_fail_response()

        assert response_message == message_after_submit