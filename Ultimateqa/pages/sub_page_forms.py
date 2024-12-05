from playwright.sync_api import Page


class SubPageForms:
    def __init__(self, page: Page):
        self.page = page
        self.name = self.page.locator("#et_pb_contact_name_0")
        self.email = self.page.locator("#et_pb_contact_email_0")
        self.message = self.page.locator("#et_pb_contact_message_0")
        self.section = page.locator('.et_pb_contact_form_0')
        self.question = self.section.locator('.et_pb_contact_captcha_question')
        self.calc_result = self.page.locator('input[name="et_pb_contact_captcha_0"]')
        self.submit = self.section.locator('[name=et_builder_submit_button]')
        self.submit_response = self.section.get_by_text("Thanks for contacting us")
        self.submit_fail_response = self.section.get_by_text("You entered the wrong number in captcha.")

    def set_name(self, name: str):
        self.name.fill(name)

    def set_email(self, email: str):
        self.email.fill(email)

    def set_message(self, message: str):
        self.message.fill(message)

    def extract_and_calculate_result(self):
        exercise = self.question.text_content()
        num_list = exercise.split("+")
        result = int(num_list[0]) + int(num_list[1])
        print(f'result is: {result}')
        return str(result)

    def set_result(self, result: str):
        self.calc_result.fill(result)

    def click_submit(self):
        self.submit.click()

    def get_submit_response(self):
        return self.submit_response.text_content()

    def get_submit_fail_response(self):
        return self.submit_fail_response.text_content()


